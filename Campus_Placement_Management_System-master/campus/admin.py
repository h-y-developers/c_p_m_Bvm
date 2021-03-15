from django.contrib import admin

# Register your models here.
# from .models import User,Achievements,Assignments,Assign_record,College,Comapnies,Department,Faculties,Projects,Students,Subjects,Timetable
from .models import User,Achievement,Exams,Events,College,Comapnies,Department,Faculties,Project,Student,Subject,Timetable

admin.site.register(User)
admin.site.register(Student)
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