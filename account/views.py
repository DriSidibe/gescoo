from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_views(request):
    return render(request, 'account/signup.html')

def login_views(request):
    return render(request, 'account/login.html')

@login_required
def logout_views(request):
    pass