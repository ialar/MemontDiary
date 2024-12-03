from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.forms import LoginCustomForm
from users.views import UserCreateView, ProfileView, confirm_register, LoginRequiredTemplateView, RegisterMessageView, \
    UserPasswordSentView, UserPasswordRecoveryView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', form_class=LoginCustomForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login_required/', LoginRequiredTemplateView.as_view(), name='login_required'),
    path('register/confirm/<str:code>/', confirm_register, name='confirm_register'),
    path('register/message/', RegisterMessageView.as_view(), name='register_message'),
    path('user_password_sent/', UserPasswordSentView.as_view(), name='user_password_sent'),
    path('password_reset/', UserPasswordRecoveryView.as_view(), name='password_reset'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
