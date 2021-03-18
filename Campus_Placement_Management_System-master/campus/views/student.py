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
    return render(request,'students/login.html')
def StudentLoginView(request):
    if request.user.is_authenticated:
        return redirect('/students/index')
    else:
        if request.method == 'POST':
            username = request.POST.get('susername')
            password =request.POST.get('spassword')
            if username == "" or password == "":
                messages.error(request,"Please fill all the fields")
                return redirect('/students/login')
            else:    
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_student:
                        login(request, user)
                        return redirect('/students/index')
                    else:
                        messages.error(request, 'You are not authorized as students')   
                else:
                    messages.error(request, 'Username Or Password is incorrect')
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

def StudentCertificateView(request):
    if request.user.is_authenticated and request.user.is_student:
        if request.method == "POST" and 'certi' in request.FILES:
            certificate_name = request.POST.get('name')
            issuer_name = request.POST.get('company')
            field = request.POST.get('field')
            certificate_img = request.FILES['certi']
            form = Achievement(student_name= request.user.username,certificate_name=certificate_name,issuer_name=issuer_name,field_type = field,certificate_img=certificate_img)
            # form = Achievements(request.POST,request.FILES)
            form.save()
            return redirect('/students/achievements')

        
        return render(request,"students/certificate.html")
    else:
        return redirect('students/login')

def StudentExamView(request):
    if request.user.is_authenticated and request.user.is_student:
        return render(request,"students/exams.html")
    else:
        return redirect('students/login')

def StudentAchievementView(request):
    if request.user.is_authenticated and request.user.is_student:
        achieve = Achievement.objects.filter(student_name = request.user.username)
        context = {
            'achievements':achieve
        }
        return render(request,"students/achievements.html",context)
    else:
        return redirect('students/login')    

def Studentproject(request):
    if request.user.is_authenticated and request.user.is_student:
        project = Project.objects.filter(student_name = request.user.username)
        context = {
            'projects':project
        }
        return render(request,"students/projects.html",context)
    else:
        return redirect('students/login')    


def StudentProjectView(request):
    if request.user.is_authenticated and request.user.is_student:
        if request.method == "POST":
            project_name = request.POST.get('name')
            description = request.POST.get('desc')
            url = request.POST.get('url')
            form = Project(student_name = request.user.username,project_name=project_name,description=description,url=url)
            form.save()
            return redirect('/students/projects')
        else:
            return render(request,"students/add_project.html")
    else:
        return redirect('students/login')

def studentsProfilesee(request):
    if request.user.is_authenticated and request.user.is_student:
        return render(request,"students/profile.html")
    else:
        return redirect('/login')

def decode_skill(skills):
    """
    Decode pizza pie toppings
    """
    skill = dict(Student.boolschoice)
    decoded = [skill[t] for t in skills]
    decoded.sort()
    return ', '.join(decoded)


def StudentProfileUpdateView(request,slug):
    if request.method == "POST" and 'ssc_result' in request.FILES or 'hsc_result' in request.FILES:
        skills = request.POST.get('skills')
        # skil = dict(Student.boolschoice)
        # skill = [skil[t] for t in skills]
        
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
        ssc_res = request.FILES['ssc_result']
        hsc = request.POST.get('hsc')
        hsc_res = request.FILES['hsc_result']
        
        interest = request.POST.get('interest')
            

        userr = User.objects.get(slug = slug)

        form = Student(Id_number= userr.username,fname=fname,lname=lname,gender=gender,dob=dob,email=email,
        mobile=mobile,dept=dept,enrollment=enrollment,id_no=id_no,
            permanent_address=permanent_address,state=state,resident_address=resident_address,
            pincode=pincode,city=city,country=country,ssc=ssc,ssc_result=ssc_res,
            hsc=hsc,hsc_result=hsc_res,skills=skills,interest=interest)
        form.save()
        messages.success(request,"Updated")
        url = '/students/profile/'+str(slug)
        return redirect(url)
    else:
        try:
            userr = Student.objects.get(slug=slug)
        except:
            userr = None
        context={
                'student' : userr
        }
        return render(request,"students/profile.html",context)
        


def StudentProfileView(request,slug):
    if request.user.is_authenticated and request.user.is_student:
        # if request.method == "POST" and 'ssc_result' in request.FILES or 'hsc_result' in request.FILES:

        #     fname = request.POST.get('fname')
        #     lname = request.POST.get('lname')
        #     gender = request.POST.get('gender')
        #     dob = request.POST.get('dob')
        #     email = request.POST.get('email')
        #     mobile = request.POST.get('mobile')
        #     # role = request.POST.get('role')
        #     dept = request.POST.get('dept')
        #     enrollment = request.POST.get('enrollment')
        #     id_no = request.POST.get('id_no')
        #     permanent_address = request.POST.get('permanent_address')
        #     state = request.POST.get('state')
        #     resident_address = request.POST.get('resident_address')
        #     pincode = request.POST.get('pincode')
        #     city = request.POST.get('city')
        #     country = request.POST.get('country')
        #     ssc = request.POST.get('ssc')
        #     ssc_res = request.FILES['ssc_result']
        #     hsc = request.POST.get('hsc')
        #     hsc_res = request.FILES['hsc_result']
        #     skills = request.POST.get('skills')
        #     interest = request.POST.get('interest')
            

        #     userr = User.objects.get(slug = slug)

        #     form = Student(Id_number= userr.username,slug = slug,fname=fname,lname=lname,gender=gender,dob=dob,email=email,
        #     mobile=mobile,dept=dept,enrollment=enrollment,id_no=id_no,
        #     permanent_address=permanent_address,state=state,resident_address=resident_address,
        #     pincode=pincode,city=city,country=country,ssc=ssc,ssc_result=ssc_res,
        #     hsc=hsc,hsc_result=hsc_res,skills=skills,interest=interest)
        #     form.save()
        #     url = '/students/profile/'+str(slug)
        #     return redirect(url)

        # else:
        try:
            userr = Student.objects.get(slug=slug)
        except:
            userr = None
        context={
                'student' : userr
        }
        return render(request,"students/profile.html",context)

        
        
        
    
          
    # else:
    #     return HttpResponse("<h1>not happening</h1>")
            
    else:
        return redirect('students/login')
     