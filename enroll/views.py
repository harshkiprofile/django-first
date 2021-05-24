from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

# Home page
def home_view ( request ):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            new = User(name=nm, email=em, password=pw)
            new.save()
            fm = StudentRegistration()
    else: 
        fm = StudentRegistration()    
    db = User.objects.all()
    return render(request, 'enroll/home.html', {'form':fm ,'data':db})

def delete_view(request ,id):
    delete_entry = User.objects.get(pk = id)
    delete_entry.delete()
    return HttpResponseRedirect('/')

def edit_view(request, id):
    if request.method == 'POST':
        update_entry = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST, instance = update_entry)
        if fm.is_valid():
            fm.save()
            flag = True
    else:
        update_entry = User.objects.get(pk = id)
        fm = StudentRegistration(instance = update_entry)
        flag = False
    return render(request , 'enroll/update.html' , {'form' :fm ,'flag':flag})