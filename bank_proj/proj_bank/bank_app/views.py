from django.contrib import messages, auth
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bank_app.models import district, branch, person_info


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        cpw = request.POST['c_password']

        if pw == cpw:
            if User.objects.filter(username=un).exists():
                messages.info(request, 'username already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=un, password=pw)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password mismatch')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid user')
            # user.save()
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def dist_load(request):
    dist_obj = district.objects.all()
    return render(request, 'person_details.html', {'dist': dist_obj})


def load_brn(request, district_id):
    id = district.objects.get(id=district_id)
    brn = branch.objects.get(id=id)
    return render(request, 'person_details.html', {'brn': brn})


# def branch_load(request,id):
#     id = request.POST.get('id')
#     obj = branch.objects.filter(id=id)

def view_message(request):
    messages.info(request,'Application received')
    return render(request, 'success.html')


# def person(request,dist_id):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         dob = request.POST.get('dob')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         phone_number = request.POST.get('phone_number')
#         mail_id = request.POST.get('mail_id')
#         address = request.POST.get('address')
#         branches = request.POST.get('branches')
#         account_type = request.POST.get('account_type')
#         debit = request.POST.get('debit')
#         credit = request.POST.get('credit')
#         checkbook = request.POST.get('checkbook')
#         dist_id = request.POST.get()
#         details = person_info(name=name, dob=dob, age=age, gender=gender, phone_number=phone_number, mail_id=mail_id,
#                               address=address,dist_id=dist_id, branch=branches, account_type=account_type, debit=debit, credit=credit,
#                               checkbook=checkbook)
#
#         if details is not None:
#             details.save()
#             messages.info(request, "Application Received")
#             return redirect("person_details")
#         else:
#             messages.info(request, "Application failed")
#             return redirect("person_details")
#     return render(request, "person_details.html")
