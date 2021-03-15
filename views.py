# from django.shortcuts import render,HttpResponse,redirect
# from .models import Admin,Achievements,Assignments,Assign_record,College,Comapnies,Department,Faculties,Projects,Students,Subjects,Timetable,User_info
# # Create your views here.
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages

# # class Student_Dashboard(View):
# # 	template_name="Student/index.html"

# # def initial_login(request):
#     # return render(request,"login.html")

# def StudentDashboardView(request):

#     return render(request,"Student/index.html")

# def StudentExamView(request):
#     return render(request,"Student/exams.html")    

# def StudentAssignmentView(request):
#     return render(request,"Student/assignments.html")

# def StudentProfileView(request):
#     if request.method == "POST":
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         gender = request.POST.get('gender')
#         dob = request.POST.get('dob')
#         email = request.POST.get('email')
#         mobile = request.POST.get('mobile')
#         role = request.POST.get('role')
#         dept = request.POST.get('dept')
#         form = Students(fname=fname,lname=lname,gender=gender,email=email,
#         mobile=mobile,role=role,dept=dept)
#         form.save()
#         return render(request,"Student/index.html")
#     # else:
#     #     return HttpResponse("<h1>not happening</h1>")
            
    
#     return render(request,"Student/form.html")   



# def StudentProjectView(request):
#     return render(request,"Student/projects.html")

# def StudentTimetableView(request):
#     return render(request,"Student/timetable.html")

# def StudentAchievementView(request):
#     return render(request,"Student/achievements.html")

# def StudentMaterialView(request):
#     return render(request,"Student/materials.html")






# def FacultyDashboardView(request):
#     return render(request,"Faculty/faculty_index.html")

# def FacultyProfileView(request):
#     return render(request,"Faculty/faculty_profile.html")    

# def FacultyMarksView(request):
#     return render(request,"Faculty/marks.html")


# def FacultyMaterialsView(request):
#     return render(request,"Faculty/materials.html")

# def FacultyStudentDataView(request):
#     return render(request,"Faculty/student_data.html")

# def FacultyAssignmentView(request):
#     return render(request,"Faculty/assign.html")

# def FacultyViewAssignmentView(request):
#     return render(request,"Faculty/assignment_view.html")



# def AdminLoginView(request):
#     if request.user.is_authenticated:
#         return redirect('/C_Admin/index')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password =request.POST.get('password')
#             user = authenticate(request, username=username, password=password)
            
#             if user is not None:
#                 login(request, user)
#                 return redirect('/C_Admin/index')
#             else:
#                 messages.info(request, 'Username OR password is incorrect')
#         context = {}
#         return render(request, 'C_Admin/login.html', context)

# def AdminLogoutView(request):
#     logout(request)
#     return redirect('/C_Admin/login')


# def AdminAddAdminView(request):
#     return render(request,"C_Admin/admin.html")

# def AdminCompanyView(request):
#     return render(request,"C_Admin/company_id.html")

# def AdminFacultyView(request):
#     return render(request,"C_Admin/faculty_id.html")

# def AdminStudentView(request):
#     return render(request,"C_Admin/student_id.html")