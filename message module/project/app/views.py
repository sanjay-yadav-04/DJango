from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
def landing(req):
    messages.info(req,"welcome to my site")
    messages.error(req,"Error Found")
    messages.debug(req,"Debug")
    messages.success(req,"success")
    messages.warning(req,"warning")
    messages.info(req,"info")
    return redirect('home')
def home(req):
    return render(req,'home.html')