from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def firstpage(request):
    return render(request,'hs.html')

@login_required(login_url='login')
def appointment(request):
    return render(request,'ap.html')


def userlogin(request):
    return render(request,'user.html')


def signuppage(request):
    return render(request,'signup.html')






def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  
            if User.objects.filter(username=username).exists(): 
                messages.info(request, 'This username already exists!!!!!!')
                
                return redirect('signuppage')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                
                
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signuppage')   
        return redirect('login')
    else:
        return render(request,'signup.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.info(request, f'Hi {username}')
			return redirect('appointment')
		else:
			messages.info(request, 'Invalid Username or Password. Try Again.')
			return redirect('userlogin')
	else:
		
		return redirect('userlogin')


@login_required(login_url='login')
def logout(request):
	auth.logout(request)
	return redirect('firstpage')


def patient_details(request):
    if request.method=='POST':
        nme=request.POST['patient_name']
        ag=request.POST['age']
        gnd=request.POST['gender']
        em=request.POST['email']
        ph=request.POST['phone_number']
        dp=request.POST['department']
        dt=request.POST['date']

        patient=patient_details(patient_name=nme,
                                age=ag,
                                gender=gnd,
                                email=em,
                                phone_number=ph,
                                department=dp,
                                date=dt)



        patient.save()
        return redirect(appointment_success)

def appointment_success(request):        
    return render(request,'apsuccess.html')
