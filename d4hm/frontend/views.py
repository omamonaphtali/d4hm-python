from django.shortcuts import render_to_response, render
from django.conf import settings
import requests
from .forms import SubmitEmployee
from .serializer import EmployeeSerializer
# Create your views here.


def index(request):
    return render_to_response('index.html')


def about(request):
    return render_to_response('about.html')


def gallery(request):
    return render_to_response('gallery.html')


def contact(request):
    return render_to_response('contact.html')


def profiles(request):
    employee = []
    temp = requests.get(url='http://dial4.herokuapp.com/employees')
    json = temp.json()
    serializer = EmployeeSerializer(data=json)
    if serializer.is_valid():
        for i in range(len(serializer)):
            if i % 1 == 0:
                names = serializer[i]
                employee.append(names)
            # else:
            #     names == serializer[i]
            #     employee.append(names)
    # else:
    #     return render(request, 'profiles.html')


# def profiles(request):
#     global employee
#     response = requests.get(url='http://dial4.herokuapp.com/employees/')
#     json = response.json()
#     serializer = EmployeeSerializer(data=json)
#     if serializer.is_valid():
#         employee = serializer.save()
#         return render(request, 'profiles.html', {
#             'name': employee['emp_name']
#             # 'title': employeesData['emp_title'],
#             # 'bio': employeesData['emp_bio'],
#             # 'image': employeesData['emp_image']
#         })
#     else:
#         return render(request, 'profiles.html')

# def profiles (requset):
#     employee = []
#     temp = requests.get(url='http://dial4.herokuapp.com/employees/')

# def save_employee(request):
#
#     if request.method == "POST":
#         form = SubmitEmployee(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             r = requests.get('http://dial4.herokuapp.com/employee/?key=' + settings.API_KEY)
#             json = r.json()
#             serializer = EmployeeSerializer(data=json)
#             if serializer.is_valid():
#                 employee = serializer.save()
#                 return render(request, 'profiles.html', {'name': employee})
#     else:
#         form = SubmitEmployee()
#
#     return render(request, 'index.html', {'form': form})
