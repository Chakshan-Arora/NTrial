from django.shortcuts import render, redirect
from django.http import HttpResponse

# def redirect_home():
    # return redirect("https://www.google.com")

def home(request):
    data = {
        "title" : "Navrang",
        # "programs" : ["1","2","3"]
        # "contact" : [
        #     {"name":"test1", "email":"test1@example"},
        #     {"name":"test2", "email":"test2@example"},
        # ]
        # "nums" : [10,20,30,40,50]
    }
    return render(request, 'index.html', data)

def program_detail(request, pid):
    # return HttpResponse(pid)
    programs = {
        "1" : "Navrang Exhibition",
        "2" : "Navrang Dance Off",
        "3" : "Upcoming"
    }
    t = f"{programs[str(pid)]}"
    data = {
        "title" : t
    }
    return render(request, 'program_detail.html', data)

def about(request):
    data = {"title":"About Us"}
    return render(request, 'about.html',data)
