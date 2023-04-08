import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Users

# Create your views here.

#@login_required(login_url='user_login')
@login_required
def index(request):
    return render(request,'dashboard/index.html')

#@login_required(login_url='user_login')
@login_required
def staff(request):
    return render(request,'dashboard/staff.html')
 
#@login_required(login_url='user_login')
@login_required
def users(request):
    return render(request,'dashboard/users.html')

#@login_required(login_url='user_login')
@login_required
def sales(request):
    return render(request,'dashboard/sales.html')