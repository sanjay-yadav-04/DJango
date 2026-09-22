from django.shortcuts import render,redirect

# Create your views here.
def landing(req):
    return render(req,'landing.html')
def email(req):
    return redirect(req,'email.html')