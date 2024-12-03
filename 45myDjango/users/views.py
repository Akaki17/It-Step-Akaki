from django.shortcuts import render, redirect
from .forms import UseRegistrationForm
from django.contrib.auth import logout, login

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UseRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_shope:index')
        else:
            return render(request, 'registration/registration.html', {'form': form})
    else:
        form = UseRegistrationForm()
        return render(request, 'registration/registration.html', {'form': form})
    
    
def logout_user(request):
    logout(request)
    
    return redirect('book_shope:index')