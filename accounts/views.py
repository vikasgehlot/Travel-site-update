from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def login(request):
	return render(request,'login.html')

def accounts(request):
	return render(request,'accounts.html')

def register(request):

	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']
		email=request.POST['email']

		if username is not "" and first_name is not "" and email is not "":

			if password1==password2:

				if User.objects.filter(username=username).exists():
					messages.info(request,'Username taken')
					return redirect('register')

				elif User.objects.filter(username=username).exists():
				
					messages.info(request,'Email taken')
					return redirect('register')
				else:
					user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
					user.save()
					print('user created')
					return redirect('/')

			else:
				messages.info(request,'Password is not same')
				return redirect('register')

		else:
			messages.info(request,'Some fields are left Blank')
			return redirect('register')






		
		

	else:
		return render(request,'register.html')
