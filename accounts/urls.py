from django.urls import path
from .views import ArSaLoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', ArSaLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
