# from django.shortcuts import render,HttpResponse,redirect
# from .models import Admin,Achievements,Assignments,Assign_record,College,Comapnies,Department,Faculties,Projects,students,Subjects,Timetable,User_info
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView,View


# from ..decorators import students_required
from ..models import  Student, Events,Achievement,Exams,Project, User
from ..forms import DocumentForm

# @method_decorator([login_required, students_required], name='dispatch')
# class studentsDashboardView(View):
#     model = students
#     # form_class = studentsInterestsForm
#     template_name = 'students/index.html'
#     success_url = reverse_lazy('students:students_dashboard')

#     # def get_object(self):
#     #     return self.request.user.students

#     # def form_valid(self, form):
#     #     messages.success(self.request, 'Interests updated with success!')
#     #     return super().form_valid(form)


# # def studentsDashboardView(request):

# #     return render(request,"students/index.html")

# # def studentsExamView(request):
# #     return render(request,"students/exams.html")    

# # def studentsAssignmentView(request):
# #     return render(request,"students/assignments.html")

# # def studentsProfileView(request):
# #     if request.method == "POST":
# #         fname = request.POST.get('fname')
# #         lname = request.POST.get('lname')
# #         gender = request.POST.get('gender')
# #         dob = request.POST.get('dob')
# #         email = request.POST.get('email')
# #         mobile = request.POST.get('mobile')
# #         role = request.POST.get('role')
# #         dept = request.POST.get('dept')
# #         form = students(fname=fname,lname=lname,gender=gender,email=email,
# #         mobile=mobile,role=role,dept=dept)
# #         form.save()
# #         return render(request,"students/index.html")
# #     # else:
# #     #     return HttpResponse("<h1>not happening</h1>")
            
    
# #     return render(request,"students/form.html")   



# # def studentsProjectView(request):
# #     return render(request,"students/projects.html")

# # def studentsTimetableView(request):
# #     return render(request,"students/timetable.html")

# # def studentsAchievementView(request):
# #     return render(request,"students/achievements.html")

# # def studentsMaterialView(request):
# #     return render(request,"students/materials.html")


# @method_decorator([login_required, students_required], name='dispatch')
# class studentsEventView(View):
#     model = Events
#     # form_class = studentsInterestsForm
#     template_name = 'students/assignments.html'
#     success_url = reverse_lazy('students:students_event')


# @method_decorator([login_required, students_required], name='dispatch')
# class studentsAchievementView(View):
#     model = Achievement
#     # form_class = studentsInterestsForm
#     template_name = 'students/achievements.html'
#     success_url = reverse_lazy('students:students_achievements')


# @method_decorator([login_required, students_required], name='dispatch')
# class studentsExamView(View):
#     model = Exams
#     # form_class = studentsInterestsForm
#     template_name = 'students/exams.html'
#     success_url = reverse_lazy('students:students_exams')


# @method_decorator([login_required, students_required], name='dispatch')
# class studentsProjectView(View):
#     model = Project
#     # form_class = studentsInterestsForm
#     template_name = 'students/projects.html'
#     success_url = reverse_lazy('students:students_projects')


# @method_decorator([login_required, students_required], name='dispatch')
# class studentsProfileView(View):
#     model = students
#     # form_class = studentsInterestsForm
#     template_name = 'students/profile.html'
#     success_url = reverse_lazy('students:students_profile')

def shome(request):
    return redirect('/students/login')
def StudentLoginView(request):
    if request.user.is_authenticated:
        return redirect('/students/index')
    else:
        if request.method == 'POST':
            username = request.POST.get('susername')
            password =request.POST.get('spassword')
            if username == "" or password == "":
                messages.info(request,"Please fill all the fields")
                return redirect('/students/login')
            else:    
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_student:
                        login(request, user)
                        return redirect('/students/index')
                    else:
                        messages.info(request, 'You are not authorized as students')   
                else:
                    messages.info(request, 'Username Or Password is incorrect')
                    return redirect('/students/login')
            
        context = {}
        return render(request, 'students/login.html', context)


def StudentLogoutView(request):
    return redirect('/logout')

def StudentForgetPassView(request):
    return redirect('/forgetPassword')


def StudentDashboardView(request):
    if request.user.is_authenticated and request.user.is_student:
        return render(request,"students/index.html")
    else:
        return redirect('students/login')

def StudentEventView(request):
    if request.user.is_authenticated and request.user.is_student:
        return render(request,"students/assignments.html")
    else:
        return redirect('students/login')
def StudentCertificateadd(request):
    if request.user.is_authenticated and request.user.is_student:
        return render(request,"students/certificate.html")
    else:
        return redirect('students/login')

def StudentCertificateView(request):
    if request.user.is_authenticated and request.user.is_student:
        if request.method == "POST" and 'certi' in request.FILES:
            certificate_name = request.POST.get('name')
            issuer_name = request.POST.get('company')
            certificate_img = request.FILES['certi']
            form = Achievement(certificate_name=certificate_name,issuer_name=issuer_name,certificate_img=certificate_img)
            # form = Achievements(request.POST,request.FILES)
            form.save()
            return redirect('/students/achievements')
            # return render(request,"students/achievements.html")
        else:
            return render(request,"students/certificate.html")
    else:
        return redirect('students/login')
def StudentProjectadd(request):
    if request.user.is_authenticated and request.user.is_student:
        return render(request,"students/add_project.html")
    else:
        return redirect('students/login')
def StudentExamView(request):
    if request.user.is_authenticated and request.user.is_student:
        return render(request,"students/exams.html")
    else:
        return redirect('students/login')

def StudentAchievementView(request):
    if request.user.is_authenticated and request.user.is_student:
        return render(request,"students/achievements.html")
    else:
        return redirect('students/login')    

def Studentproject(request):
    return render(request,"students/projects.html")


def StudentProjectView(request):
    if request.user.is_authenticated and request.user.is_student:
        if request.method == "POST":
            project_name = request.POST.get('name')
            description = request.POST.get('desc')
            url = request.POST.get('url')
            form = Project(project_name=project_name,description=description,url=url)
            form.save()
            return redirect('/students/projects')
            # return render(request,"students/projects.html")
        else:
            return render(request,"students/add_project.html")
    
        return redirect('students/login')

def StudentProfileadd(request):
    if request.user.is_authenticated and request.user.is_student:
        return render(request,"students/profile.html")
    else:
        return redirect('students/login')



def StudentProfileView(request):
    if request.user.is_authenticated and request.user.is_student:
        if request.method == "POST" or 'ssc_result' or request.FILES or 'hsc_result' in request.FILES:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            # role = request.POST.get('role')
            dept = request.POST.get('dept')
            enrollment = request.POST.get('enrollment')
            id_no = request.POST.get('id_no')
            permanent_address = request.POST.get('permanent_address')
            state = request.POST.get('state')
            resident_address = request.POST.get('resident_address')
            pincode = request.POST.get('pincode')
            city = request.POST.get('city')
            country = request.POST.get('country')
            ssc = request.POST.get('ssc')
            ssc_result = request.FILES['ssc_result']
            hsc = request.POST.get('hsc')
            hsc_result = request.FILES['hsc_result']
            skills = request.POST.get('skills')
            interest = request.POST.get('interest')
            

            

            form = Student(fname=fname,lname=lname,gender=gender,dob=dob,email=email,
            mobile=mobile,dept=dept,enrollment=enrollment,id_no=id_no,
            permanent_address=permanent_address,state=state,resident_address=resident_address,
            pincode=pincode,city=city,country=country,ssc=ssc,ssc_result=ssc_result,
            hsc=hsc,hsc_result=hsc_result,skills=skills,interest=interest)
            form.save()
            return redirect('/students/profile') 
            # return render(request,"students/index.html")

        
        # return render(request,"students/profile.html")
   
    else:
        return redirect('students/login')
     