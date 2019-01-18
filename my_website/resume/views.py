from django.shortcuts import render
#from resume.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
import os
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
# Create your views here.


def index(request):

        return render(request, 'resume/index.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'resume/logout.html')



@login_required
def show_resume(request):

    if request.method == 'POST':
        first = request.POST.get('lastname')
        last = request.POST.get('firstname')
        email = request.POST.get('email')
        company = request.POST.get('company')
        comment = request.POST.get('comment')

        send_from = 'vetautoreport@gmail.com'
        send_to =   'jacobcansler@gmail.com'
        subject = 'Webisite Comment'
        text = 'Name: '+ first + ' ' + last+ '\ncompany: ' + company + '\nComments: '+ comment +'\nEmail:  ' +email
        port= 465
        server = 'smtp.gmail.com'
        username='vetautoreport@gmail.com'
        password=''

        print('Name: '+ first + ' ' + last+ '\ncompany: ' + company + '\nComments: '+ comment +'\nEmail:  ' +email)

        isTls=True


        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime = True)
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.login(username,password)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()
        print('e-mail sent!')

    return render(request, 'resume/resume.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                #return HttpResponseRedirect(reverse('show_resume'))
                return render(request, 'resume/resume.html')
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("someone tried to login and failed")
            print("username:{}".format(username))
            return HttpResponse("invalid login")

    else:
        return render(request, 'resume/index.html')
