import random
import string

from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import (UserPasswordResetForm, UserProfileForm,
                         UserRegisterForm)
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:register_message")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        code = "".join([str(random.randint(0, 9)) for _ in range(10)])
        user.verification_code = code
        current_host = self.request.get_host()
        user.save()

        send_mail(
            "Регистрация на сайте Memont",
            f"""Подтвердите свой профиль, перейдя по ссылке\n 
                  http://{current_host}/users/register/confirm/{code}/""",
            EMAIL_HOST_USER,
            [user.email],
        )
        return super().form_valid(form)


class RegisterMessageView(TemplateView):
    template_name = "users/register_message.html"


class LoginRequiredTemplateView(TemplateView):
    template_name = "users/login_required.html"


def confirm_register(code):
    user = get_object_or_404(User, verification_code=code)
    user.is_active = True
    user.save()
    return HttpResponseRedirect("/users/login")


class UserPasswordRecoveryView(FormView):
    form_class = UserPasswordResetForm
    template_name = "users/user_password_reset.html"
    success_url = reverse_lazy("users:user_password_sent")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = User.objects.get(email=email)
        characters = string.ascii_letters + string.digits
        new_password = "".join(random.choice(characters) for _ in range(10))
        user.password = make_password(new_password)
        user.save()
        send_mail(
            "Восстановление пароля на сайте Memont",
            f"Ваш новый пароль: {new_password}",
            EMAIL_HOST_USER,
            [user.email],
        )
        return super().form_valid(form)


class UserPasswordSentView(TemplateView):
    template_name = "users/user_password_sent.html"


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user
