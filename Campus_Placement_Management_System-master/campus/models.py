from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from datetime import datetime
import uuid
from multiselectfield import MultiSelectField
from rest_framework import fields, serializers
# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    email = models.CharField(max_length=100)
    is_pass_change = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    college_name = models.CharField(max_length =100, default="BVM")

# class Admin(models.Model):
#     username = models.CharField(unique=True,primary_key=True,max_length=20)
#     # name= models.CharField(max_length = 100)
#     # mobile_no = models.CharField(max_length=12)
#     # email_id = models.CharField(max_length = 100)
#     password = models.CharField(max_length=100)
#     # college_name = models.CharField(max_length =100, default="BVM")

#     # class Meta:
#     #     db_table = "admin"




# class Students(models.Model):
#     boolChoice = (
#         ("Male","Male"),("Female","Female")
#         )
#     boolrchoice = (
#         ("Student","Student"),("Staff","Staff")
#     )
#     booldchoice  = (
#         ("Mechanical","Mechanical"),
#         ("EC","EC"),
#         ("Civil","Civil"),
#         ("IT","IT"),("EL","EL"),("EE","EE"),("Production","Production")
#     )
#     student_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     fname = models.CharField(max_length=100,null=True)
#     lname = models.CharField(max_length=100,null=True)
#     gender = models.CharField(max_length=10,choices=boolChoice,null=True)
#     dob = models.DateField(null=True)
#     email = models.EmailField(max_length = 254,null=True)
#     mobile = models.CharField(max_length=12,null=True)
#     role = models.CharField(max_length = 10,choices=boolrchoice,null=True)
#     batch_id = models.CharField(max_length=10)
#     # dept_name = models.CharField(max_length = 10,choices=booldchoice,null=True)
#     depart_name = models.CharField(max_length=100)
#     # city = models.CharField(max_length = 100)
#     # residential_addr = models.CharField(max_length = 255)
#     # permanant_addr = models.CharField(max_length=255)
#     # ssc_marks = models.CharField(max_length = 10,default = '0')
#     # hsc_marks = models.CharField(max_length=10,default = '0')
#     # sem_1 = models.CharField(max_length = 10,default = '0')
#     # sem_2 = models.CharField(max_length=10,default = '0')
#     # sem_3 = models.CharField(max_length = 10,default = '0')
#     # sem_4 = models.CharField(max_length=10,default = '0')
#     # sem_5 = models.CharField(max_length = 10,default = '0')
#     # sem_6 = models.CharField(max_length=10,default = '0')
#     # sem_7 = models.CharField(max_length = 10,default = '0')
#     # sem_8 = models.CharField(max_length=10,default = '0')
#     # dept_id = models.CharField(max_length=5)
#     # batch_id = models.CharField(max_length=5)
#     college_name = models.CharField(max_length =100, default="BVM")

#     def __str__(self):
#         return self.student_id
    # class Meta:
    #     db_table = "students"
class Skills(models.Model):
    boolschoice = (
        ("wd","Web Development"),("ad","App Development"),("cd","Cloud Computing"),
        ("excel","Excel"),("wp","Wordpress"),("react","React"),("dj","Django"),
        ("bc","Block Chain"),("dm","Data Mining"),("py","Python"),("c","C/C++"),
        ("j","Java")
    )
    a_skills = models.CharField(max_length=100,choices=boolschoice,null=True)



class Interests(models.Model):
    boolschoice = (
        ("wd","Web Development"),("ad","App Development"),("cd","Cloud Computing"),
        ("excel","Excel"),("wp","Wordpress"),("react","React"),("dj","Django"),
        ("bc","Block Chain"),("dm","Data Mining"),("py","Python"),("c","C/C++"),
        ("j","Java")
    )
    a_interest = models.CharField(max_length=100,choices=boolschoice,null=True)


class Student(models.Model):
    
    boolChoice = (
        ("Male","Male"),("Female","Female")
        )
   
    booldchoice  = (
        ("Mechanical","Mechanical"),
        ("EC","EC"),
        ("Civil","Civil"),
        ("IT","IT"),("EL","EL"),("EE","EE"),("Production","Production")
    )

    boolschoice = (
        ("wd","Web Development"),("ad","App Development"),("cd","Cloud Computing"),
        ("excel","Excel"),("wp","Wordpress"),("react","React"),("dj","Django"),
        ("bc","Block Chain"),("dm","Data Mining"),("py","Python"),("c","C/C++"),
        ("j","Java")
    )
    boolichoice = (
        ("wd","Web Development"),("ad","App Development"),("cd","Cloud Computing"),
        ("excel","Excel"),("wp","Wordpress"),("react","React"),("dj","Django"),
        ("bc","Block Chain"),("dm","Data Mining"),("py","Python"),("c","C/C++"),
        ("j","Java")
    )
    fname = models.CharField(max_length=100,null=True)
    lname = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=6,choices=boolChoice,null=True)
    dob = models.DateField()
    email = models.EmailField(max_length = 254,null=True)
    mobile = models.CharField(max_length=12,null=True)
    # role = models.CharField(max_length = 1,choices=boolrchoice,null=True)
    dept = models.CharField(max_length = 10,choices=booldchoice,null=True)
    enrollment = models.CharField(max_length=20,null=True)
    id_no = models.CharField(max_length=10,null=True)
    permanent_address = models.CharField(max_length=256,null=True)
    state = models.CharField(max_length=100,null=True)
    resident_address = models.CharField(max_length=100,null=True)
    pincode = models.CharField(max_length=6,null=True)
    city= models.CharField(max_length = 100,null=True)
    country = models.CharField(max_length = 100,null=True)
    ssc = models.CharField(max_length = 100,null=True)
    ssc_result = models.FileField(null=True)
    hsc = models.CharField(max_length = 100,null=True)
    hsc_result = models.FileField(null=True)
    skills = MultiSelectField(choices=boolschoice,null=True)
    interest = MultiSelectField(choices=boolichoice,null=True)
    # skills = fields.MultipleChoiceField(choices=boolschoice)
    # interest = fields.MultipleChoiceField(choices=boolschoice)



class Achievement(models.Model):
    achieve_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    student_name = models.CharField(max_length=100)
    certificate_name= models.CharField(max_length = 100,blank=True)
    field_type = models.CharField(max_length=100)
    issuer_name = models.CharField(max_length = 100,blank=True)
    certificate_img = models.FileField(upload_to='achievements/')
    college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "achievements"





class College(models.Model):
    index_no = models.CharField(max_length=100,primary_key=True)
    name= models.CharField(max_length = 100, default="BVM")
    university = models.CharField(max_length=100)
    city = models.CharField(max_length = 100)
    address = models.CharField(max_length=255)
    email_id = models.CharField(max_length=100)
    helpline_no = models.CharField(max_length =100)

    # class Meta:
    #     db_table = "college"




class Comapnies(models.Model):
    company_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    company_name = models.CharField(max_length = 100)
    field_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length = 100)
    coming_date = models.DateField()
    job_description = models.CharField(max_length=255)
    # required_student = models.IntergerField()
    # placed_student = models.IntergerField()
    college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "companies"




class Department(models.Model):
    dept_id = models.AutoField(primary_key=True,unique=True)
    college_name= models.CharField(max_length = 100, default="BVM")
    dept_name = models.CharField(max_length=100)
    dept_hod = models.CharField(max_length = 100)
    no_of_faculty = models.CharField(max_length=10)
    est_year = models.CharField(max_length=5)

    # class Meta:
    #     db_table = "departments"
class Faculties(models.Model):
    boolChoice = (
        ("Male","Male"),("Female","Female")
        )
    
    booldchoice  = (
        ("Mechanical","Mechanical"),
        ("EC","EC"),
        ("Civil","Civil"),
        ("IT","IT"),("EL","EL"),("EE","EE"),("Production","Production")
    )

    # boolschoice = (
    #     ("wd","Web Development"),("ad","App Development"),("cd","Cloud Computing"),
    #     ("excel","Excel"),("wp","Wordpress"),("react","React"),("dj","Django"),
    #     ("bc","Block Chain"),("dm","Data Mining"),("py","Python"),("c","C/C++"),
    #     ("j","Java")
    # )
    fname = models.CharField(max_length=100,null=True)
    lname = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=1,choices=boolChoice,null=True)
    dob = models.DateField(default=datetime.now())
    email = models.EmailField(max_length = 254,null=True)
    mobile = models.CharField(max_length=12,null=True)
    # role = models.CharField(max_length = 1,choices=boolrchoice,null=True)
    dept = models.CharField(max_length = 1,choices=booldchoice,null=True)
    
    id_no = models.CharField(max_length=10,null=True)
    desg = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=256,null=True)
    state = models.CharField(max_length=100,null=True)
    resident_address = models.CharField(max_length=100,null=True)
    pincode = models.CharField(max_length=6,null=True)
    city= models.CharField(max_length = 100,null=True)
    country = models.CharField(max_length = 100,null=True)
    B_E_college_name = models.CharField(max_length = 100,null=True)
    B_E_college_result = models.FileField(null=True)
    M_E_college_name = models.CharField(max_length = 100,null=True)
    M_E_college_result = models.FileField(null=True)








class Project(models.Model):
    project_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # subject_id = models.CharField(max_length=100)
    student_id = models.CharField(max_length = 100)
    project_name= models.CharField(max_length = 100,blank=True)
    description = models.CharField(max_length = 500,blank=True)
    url = models.URLField(max_length=100,blank=True)
    rating_star = models.CharField(max_length =3)
    college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "projects"






class Subject(models.Model):
    subject_id = models.CharField(max_length=100,  primary_key=True, unique=True)
    subject_name = models.CharField(max_length = 100)
    semester = models.CharField(max_length=3)
    teach_year = models.CharField(max_length = 5)
    faculty_id = models.CharField(max_length=100)
    dept_id = models.CharField(max_length=100)
    college_name = models.CharField(max_length =100, default="")

    # class Meta:
    #     db_table = "subjects"





class Timetable(models.Model):
    time_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    semester = models.CharField(max_length = 3)
    year = models.CharField(max_length=5)
    time = models.CharField(max_length = 100)
    faculty_name = models.CharField(max_length = 100)
    lab_lec = models.CharField(max_length=1)
    subject_name = models.CharField(max_length = 20)
    batch_id = models.CharField(max_length=5)
    college_name = models.CharField(max_length =100, default="BVM")

class Events(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    event_name = models.CharField(max_length=200)
    facultyy_name = models.CharField(max_length=200)
    depart_name = models.CharField(max_length=200)
    college_name = models.CharField(max_length =100, default="BVM")
    event_date = models.DateField()



class Exams(models.Model):
    exam_choice=(
        ("Mid","Mid"),
        ("External","External")
    )
    exam_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    subject_id = models.CharField(max_length=200)
    stud_name = models.CharField(max_length=200)
    exam_type = models.CharField(max_length=10,choices=exam_choice)
    obtain_marks = models.CharField(max_length=10)
    total_marks = models.CharField(max_length=10)










