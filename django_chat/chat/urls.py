from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views


urlpatterns = [
    path('', views.home, name='chat-home'),
    path('chat_now/', views.room_select, name='chat-select'),
    path('chat/<str:room_name>/', views.room, name='chat-room'),
    path('profile/', views.profile_view, name='chat-profile'),
    path('accounts/login/', views.UserLogin.as_view(), name='chat-login'),
    path('register/', views.UserRegister.as_view(), name='chat-register'),
    path('logout/', views.LogoutView.as_view(next_page='chat-login'), name='chat-logout'),
    path('reset_password/', PasswordResetView.as_view(template_name="chat/password_reset.html"), name='password_reset'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name="chat/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="chat/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name="chat/password_reset_complete.html"), name='password_reset_complete'),
]