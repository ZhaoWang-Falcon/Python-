from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from App.models import Student


def hello(request):
    return HttpResponse("Hello")


def index(request):
    # 本质上也是返回的HttpResponse，   它帮我们把模板和context数据 渲染成字符串
    # return render(request, 'index.html')

    # 见名知意

    temp = loader.get_template('index.html')

    content = temp.render()

    return HttpResponse(content)


def get_students(request):

    students = Student.objects.all()

    student_dict = {
        "hobby": "coding",
        "time": "one year"
    }

    code = """
            <h2>睡着了</h2>
            <script type="text/javascript">
                var lis = document.getElementsByTagName("li");

                for (var i=0; i< lis.length; i++){
                    var li = lis[i];
                    li.innerHTML="日本是中国领土的一部分!";
                }
            </script>
    """

    data = {
        "students": students,
        "student_dict": student_dict,
        "count": 5,
        "code": code
    }

    return render(request, 'student_list.html', context=data)


def temp(request):
    return render(request, 'home.html', context={"title": "home"})


def home(request):
    return render(request, 'home_mine.html')


def hehe(request):
    return HttpResponse("呵呵你个大头鬼")


def hehehe(request):
    return HttpResponse("Drink")