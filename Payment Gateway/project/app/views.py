from django.shortcuts import render
from app.models import Add_to_cart
from django.forms.models import model_to_dict
# Create your views here.


def landing(req):
    return render(req,'landing.html')
def add_to_cart(req):
    if req.method=='POST':
        name=req.POST.get('name')
        des=req.POST.get('des')
        color=req.POST.get('color')
        quantity=req.POST.get('quantity')
        price=req.POST.get('price')
        category=req.POST.get('category')
        Add_to_cart.objects.create(name=name,des=des,color=color,quantity=quantity,price=price,category=category)
        data=Add_to_cart.objects.all()
        
        return render(req,'showdata.html',{'data':data})
def cart(req,pk):
        all_cart=[]
        data=Add_to_cart.objects.get(id=pk)
        d_data=model_to_dict(data)
        all_cart.append(d_data)
        print(all_cart)