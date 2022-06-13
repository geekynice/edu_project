from operator import is_
from django.shortcuts import redirect, render
from edu_app.models import Assignment, Contact, Courses, Events, Student, Staff, Message
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def contact(request):
    if request.method == 'GET':
        return render(request, 'frontend/contact.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']

        Contact.objects.create(name=name, email=email, number=number, message=message)
        messages.success(request, 'Form submitted Succesfully')
        return redirect('contact')


def events(request):
    return render(request, 'frontend/events.html')

def courses(request):
    return render(request, 'frontend/courses.html')

def courses_inner(request):
    if request.method == 'GET':
        return render(request, 'frontend/course-inner.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        number = request.POST['number']
        message = request.POST['message']

        Courses.objects.create(name=name, email=email, course=course, number=number, message=message)
        messages.success(request, 'Form submitted Succesfully')
        return redirect('courses-inner')

def events_inner(request):
    if request.method == 'GET':
        return render(request, 'frontend/events-inner.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        event = request.POST['event']
        number = request.POST['number']
        message = request.POST['message']

        Events.objects.create(name=name, email=email, event=event, number=number, message=message)
        messages.success(request, 'Form submitted Succesfully')
        return redirect('events-inner')

@login_required
def dashboard(request):
    notice = Message.objects.all()
    return render(request, 'backend/admin/dashboard.html', {'notice':notice})
@login_required
def events_info(request):
    events = Events.objects.all()
    return render(request, 'backend/admin/events-info.html', {'events':events})
@login_required
def forms_info(request):
    form = Contact.objects.all()
    return render(request, 'backend/admin/forms-info.html', {'form':form})
@login_required
def addmission_info(request):
    addmission = Courses.objects.all()
    return render(request, 'backend/admin/addmission-info.html', {'addmission':addmission})

#student function
@login_required
def add_student(request):
    if request.method == 'GET':
        return render(request, 'backend/admin/add-student.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        parents_name = request.POST['parents_name']
        prof = request.POST['prof']
        number = request.POST['number']
        blood_group = request.POST['blood_group']
        address = request.POST['address']

        user = User.objects.create_user(first_name=first_name, last_name=last_name, 
                            email=email, username=username, password=password)

        student = Student.objects.create(parents_name=parents_name, prof=prof, number=number,user=user,blood_group=blood_group,address=address)
        messages.success(request, 'Added student Succesfully')
        return redirect('students-info')
@login_required
def students_info(request):
    students_info = Student.objects.all()
    return render(request, 'backend/admin/students-info.html', {'students_info':students_info})

@login_required
def delete_student(request,id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success(request, 'Student Deleted Succesfully')
    return redirect('students-info')

@login_required
def delete_notice(request,id):
    notice = Message.objects.get(id=id)
    notice.delete()
    messages.success(request, 'Notice deleted successfully')
    return redirect('dashboard')
@login_required
def student_profile(request,id):
    student = Student.objects.get(id=id)
    return render(request, 'backend/admin/student-profile.html', {'student':student})
@login_required
def edit_student(request, id):
    user = User.objects.all()
    student = Student.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'backend/admin/edit-student.html', {'student':student})
    else:
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.username = request.POST['username']
        student.parents_name = request.POST['parents_name']
        student.prof = request.POST['prof']
        student.number = request.POST['number']
        student.save()
        messages.success(request, 'Edited student Succesfully')
        return redirect('students-info')
@login_required
def my_profile(request, id):
    student = Student.objects.get(user_id=id)
    return render(request, 'backend/student/profile.html', {'student':student})
@login_required
def notice(request):
    notice = Message.objects.all()
    return render(request, 'backend/admin/notice.html', {'notice':notice})

#staff function
@login_required
def add_staff(request):
    if request.method == 'GET':
        return render(request, 'backend/admin/add-staff.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        designation = request.POST['designation']
        prof = request.POST['prof']
        number = request.POST['number']
        address = request.POST['address']

        user = User.objects.create_user(first_name=first_name, last_name=last_name, 
                            email=email, username=username, password=password,is_staff=True)

        Staff.objects.create(designation=designation, prof=prof, number=number,user=user,address=address)
        messages.success(request, 'Added Staff Succesfully')
        return redirect('staffs-info')
@login_required
def staff_info(request):
    staffs_info = Staff.objects.all()
    return render(request, 'backend/admin/staffs-info.html', {'staffs_info':staffs_info})
@login_required
def delete_staff(request,id):
    staff = Staff.objects.get(user_id=id)
    staff.delete()
    messages.success(request, 'Staff deleted Succesfully')
    return redirect('staffs-info')
@login_required
def edit_staff(request, id):
    staff = Staff.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'backend/admin/edit-staff.html', {'staff':staff})
    else:
        staff.first_name = request.POST['first_name']
        staff.last_name = request.POST['last_name']
        staff.email = request.POST['email']
        staff.username = request.POST['username']
        staff.parents_name = request.POST['parents_name']
        staff.prof = request.POST['prof']
        staff.number = request.POST['number']
        staff.save()
        messages.success(request, 'Edited staff Succesfully')
        return redirect('staffs-info')
@login_required
def user_staff_profile(request,id):
    staff = Staff.objects.get(id=id)
    return render(request, 'backend/admin/staff-profile.html', {'staff':staff})
@login_required
def message(request):
    if request.method == 'GET':
        return render(request, 'backend/admin/issue-notice.html')
    else:
        title = request.POST['title']
        description = request.POST['title']

        Message.objects.create(title=title,description=description)
        messages.success(request, 'Notice Sent')
        return redirect('dashboard')


@login_required
def student_dashboard(request):
    student = Student.objects.all()
    notice = Message.objects.all()
    return render(request, 'backend/student/student-dashboard.html', {'student':student, 'notice':notice})

def staff_dashboard(request):
    assignment = Assignment.objects.all()
    staff = Staff.objects.all()
    return render(request, 'backend/staff/staff-dashboard.html', {'staff':staff, 'assignment':assignment})

#authentication

def signin(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url is None:
                if user.is_superuser:
                    return redirect('dashboard')
                elif user.is_staff:
                    return redirect('staff-dashboard')
                else :
                    return redirect('student-dashboard')
            else:
                return redirect(next_url)
        else:
            return redirect('login')


@login_required()
def signout(request): 
    logout(request)
    return redirect('login')
@login_required
def assignment(request):
    if request.method == 'GET':
        assignment = Assignment.objects.all()
        return render(request, 'backend/student/assignment.html', {'assignment':assignment})
    else:
        description = request.POST['description']
        file = request.POST['file']

        Assignment.objects.create(description=description,file=file)

        return redirect('student-dashboard')
@login_required
def provide_assignment(request):
    if request.method == 'GET':
        return render(request, 'backend/staff/assignment.html')
    else:
        title = request.POST['title']
        description = request.POST['description']
        file = request.POST['file']
        deadline = request.POST['deadline']

        Assignment.objects.create(title=title,description=description,file=file,deadline=deadline)
        messages.success(request, 'Task Assigned Successfully!')
        return redirect('staff-dashboard')
@login_required
def staff_profile(request, id):
    staff = Staff.objects.get(user_id=id)
    return render(request, 'backend/staff/profile.html', {'staff':staff})

@login_required
def delete_assignment(request,id):
   assignment =Assignment.objects.get(id=id)
   assignment.delete()
   messages.success(request, 'assignment Deleted Succesfully')
   return redirect('staff-dashboard')