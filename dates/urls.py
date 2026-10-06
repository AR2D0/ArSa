from django.urls import path
from . import views

app_name = 'dates'

urlpatterns = [
    # User
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('history/', views.HistoryView.as_view(), name='history'),

    # Date Mission flow
    path('mission/', views.MissionStartView.as_view(), name='mission_start'),
    path('mission/date/', views.MissionDateView.as_view(), name='mission_date'),
    path('mission/time/', views.MissionTimeView.as_view(), name='mission_time'),
    path('mission/location/', views.MissionLocationView.as_view(), name='mission_location'),
    path('mission/review/', views.MissionReviewView.as_view(), name='mission_review'),
    path('mission/success/', views.MissionSuccessView.as_view(), name='mission_success'),

    # Admin
    path('admin-panel/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin-panel/request/<int:pk>/', views.AdminRequestDetailView.as_view(), name='admin_request_detail'),
]
