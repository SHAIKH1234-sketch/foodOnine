from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from  django.contrib import messages
# Create your views here.
def registerUser(request):
    if request.method=='POST':
        print(request.POST)
        form=UserForm(request.POST)
        if form.is_valid():
            #password hashing techinique 1
            #password=form.cleaned_data['password']
            #user=form.save(commit=False)
            #user.set_password(password)
            #user.role=User.Customer
            #user.save()
            #return redirect('registerUser')

            #password hashing techinique-2
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=user.Customer
            user.save()
            messages.success(request,'You have registered successfully!!!')
            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form=UserForm()
    context={
    'form':form
    }
    return render(request,'accounts/registerUser.html',context)
