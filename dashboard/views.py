from django.shortcuts import render,redirect
from food.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services

def login_required_decorator(func):
    return login_required(func,login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')

@login_required_decorator
def home_page(request):
    categories = services.get_category()
    products = services.get_products()
    customers = services.get_customer()
    orders = services.get_orders()
    ctx={
        'counts' : {
            'categories':len(categories),
            'products':len(products),
            'customers':len(customers),
            'orders':len(orders)
        }
    }
    return render(request, 'index.html', ctx)

# @login_required_decorator
# def faculty_create(request):
#     model = Faculty()
#     form = FacultyForm(request.POST or None, instance=model)
#     if request.POST and form.is_valid():
#         form.save()
#         return redirect('faculty_list')
#     ctx = {
#         "model":model,
#         "form":form
#     }
#     return render(request,'faculty/form.html',ctx)
#
# @login_required_decorator
# def faculty_edit(request,pk):
#     model = Faculty.objects.get(pk=pk)
#     form = FacultyForm(request.POST or None, instance=model)
#     if request.POST and form.is_valid():
#         form.save()
#         return redirect('faculty_list')
#     ctx = {
#         "model":model,
#         "form":form
#     }
#     return render(request,'faculty/form.html',ctx)
#
# @login_required_decorator
# def faculty_delete(request,pk):
#     model = Faculty.objects.get(pk=pk)
#     model.delete()
#     return redirect('faculty_list')
#
# @login_required_decorator
# def faculty_list(request):
#     faculties=services.get_faculties()
#     print(faculties)
#     ctx={
#         "faculties":faculties
#     }
#     return render(request,'faculty/list.html',ctx)
#
# # KAFEDRA
# @login_required_decorator
# def kafedra_create(request):
#     model = Kafedra()
#     form = KafedraForm(request.POST or None, instance=model)
#     if request.POST and form.is_valid():
#         form.save()
#
#         actions = request.session.get('actions',[])
#         actions += [f"You created kafedra: {request.POST.get('name')}"]
#         request.session["actions"] = actions
#
#         kafedra_count = request.session.get('kafedra_count', 0)
#         kafedra_count +=1
#         request.session["kafedra_count"] = kafedra_count
#
#         return redirect('kafedra_list')
#
#
#     ctx = {
#         "model":model,
#         "form":form
#     }
#     return render(request,'kafedra/form.html',ctx)
#
# @login_required_decorator
# def kafedra_edit(request,pk):
#     model = Kafedra.objects.get(pk=pk)
#     form = KafedraForm(request.POST or None, instance=model)
#     if request.POST and form.is_valid():
#         form.save()
#
#         actions = request.session.get('actions',[])
#         actions += [f"You edited kafedra: {request.POST.get('name')}"]
#         request.session["actions"] = actions
#         return redirect('kafedra_list')
#
#     ctx = {
#         "model":model,
#         "form":form
#     }
#     return render(request,'kafedra/form.html',ctx)
#
# @login_required_decorator
# def kafedra_delete(request,pk):
#     model = Kafedra.objects.get(pk=pk)
#     model.delete()
#     return redirect('kafedra_list')
#
# @login_required_decorator
# def kafedra_list(request):
#     kafedras=services.get_kafedra()
#     ctx={
#         "kafedras":kafedras
#     }
#     return render(request,'kafedra/list.html',ctx)
#
# #SUBJECT
# @login_required_decorator
# def subject_create(request):
#     model = Subject()
#     form = SubjectForm(request.POST or None, instance=model)
#     if request.POST and form.is_valid():
#         form.save()
#         return redirect('subject_list')
#     ctx = {
#         "model":model,
#         "form":form
#     }
#     return render(request,'subject/form.html',ctx)
#
# @login_required_decorator
# def subject_edit(request,pk):
#     model = Subject.objects.get(pk=pk)
#     form = SubjectForm(request.POST or None, instance=model)
#     if request.POST and form.is_valid():
#         form.save()
#         return redirect('subject_list')
#     ctx = {
#         "model":model,
#         "form":form
#     }
#     return render(request,'subject/form.html',ctx)
#
# @login_required_decorator
# def subject_delete(request,pk):
#     model = Subject.objects.get(pk=pk)
#     model.delete()
#     return redirect('subject_list')
#
# @login_required_decorator
# def subject_list(request):
#     subjects=services.get_subject()
#     ctx={
#         "subjects":subjects
#     }
#     return render(request,'subject/list.html',ctx)
#
# #TEACHER
# @login_required_decorator
# def teacher_create(request):
#     model = Teacher()
#     form = TeacherForm(request.POST or None, instance=model)
#     if request.POST and form.is_valid():
#         form.save()
#         actions = request.session.get('actions',[])
#         actions += [f"You added teacher: {request.POST.get('first_name')}"]
#         request.session["actions"] = actions
#
#         return redirect('teacher_list')
#     ctx = {
#         "model":model,
#         "form":form
#     }
#     return render(request,'teacher/form.html',ctx)
#
# @login_required_decorator
# def teacher_edit(request,pk):
#     model = Teacher.objects.get(pk=pk)
#     form = TeacherForm(request.POST or None, instance=model)
#     if request.POST and form.is_valid():
#         form.save()
#         return redirect('teacher_list')
#     ctx = {
#         "model":model,
#         "form":form
#     }
#     return render(request,'teacher/form.html',ctx)
#
# @login_required_decorator
# def teacher_delete(request,pk):
#     model = Teacher.objects.get(pk=pk)
#     model.delete()
#     return redirect('teacher_list')
#
# @login_required_decorator
# def teacher_list(request):
#     teachers=services.get_teacher()
#     ctx={
#         "teachers":teachers
#     }
#     return render(request,'teacher/list.html',ctx)
#
@login_required_decorator
def profile(request):
    return render(request,'profile.html')