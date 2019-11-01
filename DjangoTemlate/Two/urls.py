from django.conf.urls import url

from Two import views

urlpatterns = [
    # url(r'^students/(\d+)/', views.student),

    url(r'^grades/', views.grades),
    url(r'^students/(\d+)/', views.students),
    url(r'^gettime/(\d+)/(\d+)/(\d+)/', views.get_time, name='get_time'),
    url(r'^getdate/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.get_date, name='get_date'),

    url(r'^learn/', views.learn, name='learn'),

    url(r'^haverequest/', views.have_request),

    url(r'^createstudent/', views.create_student),

    url(r'^docreatestudent/', views.do_create_student, name='do_create_student'),
]