from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from emp.models import model_employee
from datetime import datetime
from django.db.models import Q

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if not uname:
            return HttpResponse("<h1 style='color:red'>USERNAME IS REQUIRED...!!</h1>")
        elif not email:
            return HttpResponse("<h1 style='color:red'>EMAIL IS REQUIRED...!!</h1>")
        elif pass1 != pass2:
            return HttpResponse("<h1 style='color:red'>YOR PASSWORD AND CONFIRM PASSWORD ARE NOT SAME...!!</h1>")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("<h1 style='color:red'>USERNAME OR PASSWORD IS INCORRECT...!!</h1>")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = request.POST['dept']
        role = request.POST['role']
        location = request.POST['location']

        # VALIDATION
        """error_message = None
        if not first_name:
            error_message = 'First name is required...!!'
        elif len(first_name) < 4:
            error_message = 'First name must be 4 char long or more ..!!'
        elif len(last_name) < 4:
            error_message = 'Last name must be 4 char long or mare..!!'
        elif not phone:
            error_message = 'phone number required'
        elif len(phone) < 10:
            error_message = 'Phon Number must be 10 char long..!!'
        elif not dept:
            error_message = 'Department is required..!!'
        elif not role:
            error_message = 'Role is required..!!'
        elif not location:
            error_message = 'Location is required..!!'
        if not error_message:
            #print(first_name,last_name, phone, dept, role, location)
            customer = model_employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept=dept,role=role,location=location)
            customer.save()"""
        new_emp = model_employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus,
                                 phone=phone,
                                 dept=dept, role=role, hire_date=datetime.now(), location=location)

        new_emp.save()
        """else:
            return render(request, 'add_emp.html', {'error': error_message})"""
        return HttpResponse("<h1 style='color:green'>Employee Add Successfully</h1>")
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("<h1 style='color:red>An Exception Occurred! Employee has not been added</h1>")
    return render(request, 'add_emp.html')


def all_emp(request):
    emp = model_employee.objects.all()
    context = {
        'emp': emp
    }
    return render(request, 'all_emp.html', context)


'''def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = model_employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("<h1 style='color:green'>Employee Removed Successfully</h1>")
        except:
            return HttpResponse("<h1 style='color:red'>Please Enter A Valid EMP ID</h1>")
    emp = model_employee.objects.all()
    context = {
        'emp': emp
    }
    return render(request, 'remove_emp.html', context)'''


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emp = model_employee.objects.all()
        if name:
            emp = emp.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emp = emp.filter(dept__icontains=dept)
        if role:
            emp = emp.filter(role__icontains=role)

        context = {
            'emp': emp
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = model_employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("<h1 style='color:green'>Employee Removed Successfully</h1>")
        except:
            return HttpResponse("<h1 style='color:red'>Please Enter A Valid EMP ID</h1>")
    emp = model_employee.objects.all()
    context = {
        'emp': emp
    }
    return render(request, 'remove_emp.html', context)