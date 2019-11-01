from django.http import HttpResponse
from django.shortcuts import render

from Two.models import Grade, Student


def students(request, g_id):

    student_list = Student.objects.filter(s_grade_id=g_id)

    return render(request, 'grade_student_list.html', context=locals())


def student(request):

    # print(s_id)
    #
    # print(type(s_id))

    return HttpResponse("Get Student Success")


def grades(request):

    grade_list = Grade.objects.all()

    # locals

    return render(request, 'grade_list.html', context=locals())


def get_time(request,hour, minute, second):
    return HttpResponse("Time %s: %s: %s" %(hour, minute, second))


def get_date(request,  month, day, year):
    return HttpResponse("Date %s- %s- %s" %(year, month, day))


def learn(request):
    return HttpResponse("Love Learn")


def have_request(request):

    print(request.path)

    print(request.method)

    print(request.GET)

    hobby = request.GET.get('hobby')

    print(hobby)

    hobbies = request.GET.getlist('hobby')

    print(hobbies)

    print(request.POST)

    # print(request.META)

    # for key in request.META:
    #     print(key, request.META.get(key))

    print("Remote IP", request.META.get("REMOTE_ADDR"))

    return HttpResponse("Request Success")


def create_student(request):
    return render(request, 'student.html')


def do_create_student(request):

    print(request.method)

    username = request.POST.get('username')

    return HttpResponse(username)