from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

class RegisterView(CreateView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    authenticated_redirect_url = reverse_lazy('homepage')
    model = User

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        user = form.save(commit=False)
        user.email = email
        user.username = email
        user.set_password(password)
        user.save()

        messages.success(self.request, 'Student register successfully')

        return super(RegisterView, self).form_valid(form)

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('homepage')
    authenticated_redirect_url = reverse_lazy('homepage')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        pasword = form.cleaned_data['password']
        user = authenticate(username=email, password=pasword)
        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            messages.error(self.request, 'Invalid email or password')
            return redirect('login')


class LogoutView(TemplateView):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')