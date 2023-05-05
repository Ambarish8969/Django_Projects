from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
    {
        'author':'Ambarish',
        'title':'My Louda Life',
        'content':'First post content',
        'date_posted':'August 8 1998'
    },
    {
        'author':'Rakesh',
        'title':'My Life',
        'content':'Second post content',
        'date_posted':'May 8 1998'
    },

]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html',{'title':'About'})