from django.urls import path
from . import views

urlpatterns = [
    path('login/', view=views.LoginView.as_view(), name='login'),
    path('api/google-login/', view=views.GoogleLoginView.as_view(), name='users-google-login')
]

