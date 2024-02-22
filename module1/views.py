import pytz
import requests
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render
import random,datetime
import string
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from .forms import *
from .models import*
from django.shortcuts import render,redirect


import matplotlib.pyplot as plt
import numpy as np

def weatherapgecall(request):
    return render(request,'weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'c22ba8c7a2e24a713e47e7e5fb7de15c'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})



def slidescall(request):
    return render(request,'slides.html')


def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})





# Create your views here.
def registerloginfunction(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            message1="Email already registered.Choose a different email."
            return render(request,'models_html.html',{'message1':message1})
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'models_html.html')


def modelsfunctioncall(request):
    return render(request,'models_html.html')


def getdate1(request):
    return render(request,'get_Date.html')
def get_Date(request):
    if request.method=='POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'get_Date.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'get_Date.html',{'form':form})

def tzfunctioncall(request):
    return render(request,'pytzexample.html')

'''def pytzexample(request):
    
     if request.method=='POST':
       inputa=request.POST['inputa']

       result=time1=pytz.timezone(inputa)
       print(result)
       context={'result':result}
     return render(request, 'pytzexample.html', {'context': context})'''



def ran(request):
    return render(request,'random123.html')
def random123(request):
    if request.method=='POST':
       input1=request.POST['input1']
       input2=int(input1)
       result_str=''.join(random.sample(string.digits,input2))
       print(result_str)
       context={'result_str':result_str}
    return render(request,"Random123.html",context)

def print1(request):
    return render(request,'print_to_console.html')

def print_to_console(request):
    if request.method=="POST":
        user_input=request.POST['kavya']
        print(f'user_input={user_input}')
    a1={'user_input':user_input}
    return render(request,'print_to_console.html',a1)

def travelpackage(request):
    return render(request,'travelpackage.html')

def newhomepage(request):
    return render(request,'newhomepage.html')

def hello(request):
    return render(request,'firsthtml.html')

def hello1(request):
    return HttpResponse("<center><font color=blue>Welcome to TTM Homepage</font></center>")

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')



def signup1(request):
    if request.method=='POST':
       username=request.POST['username']
       pass1=request.POST['password']
       pass2=request.POST['password1']
       if pass1==pass2:
           if User.objects.filter(username=username).exists():
              messages.info(request, 'OOPS! Username already taken')
              return render(request,'signup.html')
           else:
               user=User.objects.create_user(username=username,password=pass1)
               user.save()
               messages.info(request,'Account created Successfully!')
               return render(request,'newhomepage.html')
       else:
           messages.info(request,'Password does not match')
           return render(request,'signup.html')





def login1(request):
    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid Crendentials!')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')


def contactmailcall(request):
    return render(request,'feedback.html')

def contactmail(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        comment=request.POST['comment']
        tosend=comment+'--------------this is the comment box'
        data=contactus(firstname=firstname,lastname=lastname,email=email,comment=comment)
        data.save()
        return HttpResponse("<h1><center>thankyou for sending feedback</center></h1>")
