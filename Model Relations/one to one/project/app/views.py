from django.shortcuts import render
from .models import Student, Aadhar
# Create your views here.
def landing(req):
    return render(req,'landing.html')
def forward(req):
    stu_data=Student.objects.all()
    for i in stu_data:
        print(i.name,i.email,i.contact,i.city,i.a_no.aadhar_no,i.a_no.create_date,i.a_no.create_by)
        return render(req,'landing.html',{'forward':True,'stu_data':stu_data})
def reverse(req):
    a_data=Aadhar.objects.all()
    for i in a_data:
        print(i.aadhar_no,i.create_date,i.create_by)
        print(i.Student.name,i.Student.email,i.Student.contact,i.Student.city)