from django.shortcuts import render, redirect
from .forms import StudentForm

# Create your views here.
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = StudentForm()
    return render(request, "student_form.html", {"form": form})


def success(request):
    return render(request, "success.html")
