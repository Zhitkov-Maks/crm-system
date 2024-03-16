from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages


class MyLoginView(LoginView):
    """Класс для аутентификации пользователей."""
    redirect_authenticated_user: bool = True

    def get_success_url(self) -> reverse_lazy:
        """В случае успешной авторизации перенаправляем на главную страницу."""
        return reverse_lazy('index')

    def form_invalid(self, form) -> HttpResponse:
        """В случае неудачи возвращаем форму с введенным username."""
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class MyLogoutView(LogoutView):
    """Класс для выхода с сайта."""
    def get_success_url(self):
        """Если вышли, то перенаправляем на страницу входа."""
        return reverse_lazy("login")
