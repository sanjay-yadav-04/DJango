from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp_list/',emp_list),                     # GET/POST
    path('emp_detail/<int:pk>/',detail),            # GET/PUT/PATCH/DELETE
    


]