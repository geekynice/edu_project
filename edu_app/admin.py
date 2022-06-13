from django.contrib import admin

from edu_app.models import Assignment, Contact, Courses, Events, Staff, Student, Message

# Register your models here.

admin.site.register(Contact)
admin.site.register(Courses)
admin.site.register(Events)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Message)
admin.site.register(Assignment)