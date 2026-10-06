"""
Views for ArSa Date Mission and dashboard.
"""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.utils import timezone

from .models import DateRequest
from .forms import DateSelectionForm, TimeSelectionForm, LocationSelectionForm
from accounts.models import User


def get_client_ip(request):
    """Extract client IP address, considering proxies."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class DashboardView(LoginRequiredMixin, TemplateView):
    """User dashboard after login."""
    template_name = 'dates/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        requests = DateRequest.objects.filter(user=user)
        context['total_requests'] = requests.count()
        context['latest_request'] = requests.first()
        context['user'] = user
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    """User profile page (read-only)."""
    template_name = 'dates/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class HistoryView(LoginRequiredMixin, ListView):
    """User's previous date requests."""
    model = DateRequest
    template_name = 'dates/history.html'
    context_object_name = 'requests'
    paginate_by = 10

    def get_queryset(self):
        return DateRequest.objects.filter(user=self.request.user)


# ---------------------------------------------------------------------------
# Date Mission multi-step flow (session-based)
# ---------------------------------------------------------------------------

class MissionStartView(LoginRequiredMixin, TemplateView):
    """Step 1: Would you go on a date with me?"""
    template_name = 'dates/mission/step1.html'

    def get(self, request, *args, **kwargs):
        # Clear any previous mission session data
        for key in list(request.session.keys()):
            if key.startswith('mission_'):
                del request.session[key]
        return super().get(request, *args, **kwargs)


class MissionDateView(LoginRequiredMixin, View):
    """Step 2: Pick a date."""
    template_name = 'dates/mission/step2.html'

    def get(self, request):
        form = DateSelectionForm(
            initial={'selected_date': request.session.get('mission_date')}
        )
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DateSelectionForm(request.POST)
        if form.is_valid():
            request.session['mission_date'] = form.cleaned_data['selected_date'].isoformat()
            return redirect('dates:mission_time')
        return render(request, self.template_name, {'form': form})


class MissionTimeView(LoginRequiredMixin, View):
    """Step 3: Pick a time."""
    template_name = 'dates/mission/step3.html'

    def dispatch(self, request, *args, **kwargs):
        if 'mission_date' not in request.session:
            messages.warning(request, "Please start from the beginning ❤️")
            return redirect('dates:mission_start')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = TimeSelectionForm(
            initial={'selected_time': request.session.get('mission_time')}
        )
        return render(request, self.template_name, {
            'form': form,
            'selected_date': request.session.get('mission_date'),
        })

    def post(self, request):
        form = TimeSelectionForm(request.POST)
        if form.is_valid():
            t = form.cleaned_data['selected_time']
            request.session['mission_time'] = t.strftime('%H:%M:%S')
            return redirect('dates:mission_location')
        return render(request, self.template_name, {
            'form': form,
            'selected_date': request.session.get('mission_date'),
        })


class MissionLocationView(LoginRequiredMixin, View):
    """Step 4: Choose location (text only — no map)."""
    template_name = 'dates/mission/step4.html'

    def dispatch(self, request, *args, **kwargs):
        if 'mission_date' not in request.session or 'mission_time' not in request.session:
            messages.warning(request, "Please start from the beginning ❤️")
            return redirect('dates:mission_start')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = LocationSelectionForm(initial={
            'location_name': request.session.get('mission_loc_name', ''),
        })
        return render(request, self.template_name, {
            'form': form,
            'selected_date': request.session.get('mission_date'),
            'selected_time': request.session.get('mission_time'),
        })

    def post(self, request):
        form = LocationSelectionForm(request.POST)
        if form.is_valid():
            request.session['mission_loc_name'] = form.cleaned_data['location_name']
            return redirect('dates:mission_review')
        return render(request, self.template_name, {
            'form': form,
            'selected_date': request.session.get('mission_date'),
            'selected_time': request.session.get('mission_time'),
        })


class MissionReviewView(LoginRequiredMixin, View):
    """Step 5: Review and submit."""
    template_name = 'dates/mission/step5.html'

    def dispatch(self, request, *args, **kwargs):
        required = ['mission_date', 'mission_time', 'mission_loc_name']
        if not all(k in request.session for k in required):
            messages.warning(request, "Please complete all steps first ❤️")
            return redirect('dates:mission_start')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {
            'selected_date': request.session.get('mission_date'),
            'selected_time': request.session.get('mission_time'),
            'location_name': request.session.get('mission_loc_name', ''),
        })

    def post(self, request):
        from datetime import datetime
        date_str = request.session['mission_date']
        time_str = request.session['mission_time']
        selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        selected_time = datetime.strptime(time_str, '%H:%M:%S').time()

        DateRequest.objects.create(
            user=request.user,
            selected_date=selected_date,
            selected_time=selected_time,
            latitude=0,
            longitude=0,
            location_name=request.session.get('mission_loc_name', ''),
            ip_address=get_client_ip(request),
        )

        # Clear mission session data
        for key in list(request.session.keys()):
            if key.startswith('mission_'):
                del request.session[key]

        return redirect('dates:mission_success')


class MissionSuccessView(LoginRequiredMixin, TemplateView):
    """Step 6: Celebration page."""
    template_name = 'dates/mission/step6.html'


# ---------------------------------------------------------------------------
# Admin Dashboard
# ---------------------------------------------------------------------------

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin_role


class AdminDashboardView(AdminRequiredMixin, TemplateView):
    """Admin statistics and recent requests."""
    template_name = 'dates/admin_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context['total_users'] = User.objects.count()
        context['total_requests'] = DateRequest.objects.count()
        context['requests_today'] = DateRequest.objects.filter(
            created_at__date=today
        ).count()
        context['recent_requests'] = DateRequest.objects.select_related('user')[:15]
        return context


class AdminRequestDetailView(AdminRequiredMixin, TemplateView):
    """View a single request (admin)."""
    template_name = 'dates/admin_request_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request_obj'] = get_object_or_404(
            DateRequest, pk=self.kwargs['pk']
        )
        return context