from django.shortcuts import render, redirect
from .forms import UseRegistrationForm
from django.contrib.auth import logout, login

from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UseRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shope:index')
        else:
            return render(request, 'registration/registration.html', {'form': form})
    else:
        form = UseRegistrationForm()
        return render(request, 'registration/registration.html', {'form': form})
    
class RegistrationView(FormView):
    form_class =    UseRegistrationForm
    template_name ='registration/registration.html'
    success_url = reverse_lazy('shope:index-cbv')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
        
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    
    
def logout_user(request, form):
    logout(request)
    
    return redirect('shope:index')

class LogoutView(FormView):
    
    @staticmethod
    def post(request, *args, **kwargs):
        logout(request)
        return redirect('/users/login/')
    
    
class LoginUserView(LoginView):
    template_name = 'registration/login.html'