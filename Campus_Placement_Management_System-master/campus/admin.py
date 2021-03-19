from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# from .models import User,Achievements,Assignments,Assign_record,College,Comapnies,Department,Faculties,Projects,Students,Subjects,Timetable
<<<<<<< HEAD
from .models import User,Skills,Achievement,Exams,Events,College,Comapnies,Department,Faculties,Project,Student,Subject,Timetable,student_data
=======
from .models import User,Achievement,Exams,Events,College,Comapnies,Department,Faculties,Project,Student,Subject,Timetable,student_data,Marks
>>>>>>> 13d331b31cf26d89d095901e1e746c63ae160bde

@admin.register(student_data)
class student_csv(ImportExportModelAdmin):
    list_display = ('clg_id_no','name','email')

admin.site.register(Marks)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Skills)
admin.site.register(Achievement)
admin.site.register(Exams)
admin.site.register(Events)
admin.site.register(College)
admin.site.register(Comapnies)
admin.site.register(Department)
admin.site.register(Faculties)
admin.site.register(Project)
admin.site.register(Subject)
admin.site.register(Timetable)