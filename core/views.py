from django.shortcuts import render,redirect
from .forms import signUpForm
from django.contrib.auth import login
# Create your views here.
def frontpage(request):
    return render(request,'core/frontpage.html')

def signUpPage(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('frontpage')
    else:
        form = signUpForm()

    return render(request, 'core/signup.html', {'form':form})    