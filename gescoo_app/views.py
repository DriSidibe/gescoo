from django.shortcuts import render
from django.contrib.auth.decorators import login_required

app_name = 'gescoo_app'

# Create your views here.
def index(request):
    return render(request, 'index.html')