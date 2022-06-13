from django.urls import path,include
from edu_app import views

urlpatterns = [
    path('', views.index, name=''),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('events/', views.events, name='events'),
    path('events-inner/', views.events_inner, name='events-inner'),
    path('courses-inner/', views.courses_inner, name='courses-inner'),
    path('events-info/', views.events_info, name='events-info'),
    path('addmission-info/', views.addmission_info, name='addmission-info'),
    path('forms-info/', views.forms_info, name='forms-info'),
    path('events-info/', views.events_info, name='events-info'),
    path('add-student/', views.add_student, name='add-student'),
    path('students-info/', views.students_info, name='students-info'),
    path('delete-student/<int:id>/', views.delete_student, name='delete-student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit-student'),
    path('add-staff/', views.add_staff, name='add-staff'),
    path('staffs-info/', views.staff_info, name='staffs-info'),
    path('delete-staff/<int:id>/', views.delete_staff, name='delete-staff'),
    path('edit-staff/<int:id>/', views.edit_staff, name='edit-staff'),
    path('user-staff-profile/<int:id>', views.user_staff_profile, name='user-staff-profile'),
    path('student-profile/<int:id>', views.student_profile, name='student-profile'),
    path('send-message/', views.message, name='send-messaage'),
    path('issue-notice/', views.message, name='issue-notice'),
    path('student-dashboard/', views.student_dashboard, name='student-dashboard'),
    path('staff-dashboard/', views.staff_dashboard, name='staff-dashboard'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('my-profile/<int:id>', views.my_profile, name='my-profile'),
    path('staff-profile/<int:id>', views.staff_profile, name='staff-profile'),
    path('notice/', views.notice, name='notice'),
    path('delete-notice/<int:id>/', views.delete_notice, name='delete-notice'),
    path('delete-assignment/<int:id>/', views.delete_assignment, name='delete-assignment'),
    path('assignment/', views.assignment, name='assignment'),
    path('provide-assignment/', views.provide_assignment, name='provide-assignment'),
]
