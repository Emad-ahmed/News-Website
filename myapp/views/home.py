from django.shortcuts import render, HttpResponseRedirect

from django.views import View
from myapp.models import BreakNews, Comment, SpecialNews
from datetime import datetime
from myapp.forms import ChangeForm, PassChangeForm, Myallnews
from django.core.cache import cache
import bangla


class HomeView(View):
    def get(self, request):
        now = bangla.get_date()

        mynews = BreakNews.objects.all()
        id_list = []
        for news in mynews:
            id_list.append(news.id)

        n = id_list[-1]

        news1 = BreakNews.objects.get(id=n)

        date_list = []
        for i, j in now.items():
            date_list.append(j)

        for i in date_list:
            print(i, end="")

        return render(request, 'home.html', {'news': news1, 'mynews': mynews, 'date': date_list})


def fullnews(request, id):

    myallnewsshow = BreakNews.objects.all()
    mainid = BreakNews.objects.get(pk=id)
    mycomment = Comment.objects.all().order_by('-id')

    if request.method == "POST":

        comment = request.POST.get('comment')
        comments = Comment(user=request.user, comment=comment)

        comments.save()
    else:
        return render(request, 'newsshow.html', {'mynews': mainid, 'mycomment': mycomment, 'myallnewsshow': myallnewsshow})

    return render(request, 'newsshow.html', {'mynews': mainid, 'mycomment': mycomment, 'myallnewsshow': myallnewsshow})


def breaknews(request, id):
    mainid = BreakNews.objects.get(pk=id)
    return render(request, 'breaknews.html', {'mynews': mainid})


def editmain(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = ChangeForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()

        else:
            fm = ChangeForm(instance=request.user)

        return render(request, 'editprofile.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login')


def cpass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PassChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/editmain')
        else:
            fm = PassChangeForm(user=request.user)

        return render(request, 'changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login')


def search(request):
    if request.method == "POST":
        title = request.POST.get('search')
        user = BreakNews.objects.filter(title=title)
        special = SpecialNews.objects.filter(title=title)
        return render(request, 'search.html', {'user': user, 'special': special})
    else:
        return HttpResponseRedirect('/')


def addnews(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = Myallnews(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()

        else:
            fm = Myallnews()
        return render(request, 'addnews.html', {'form': fm})
    else:
        return HttpResponseRedirect('/')


def updatenews(request, id):
    if request.user.is_authenticated:
        try:
            pi = BreakNews.objects.get(id=id)
            if request.method == "POST":
                fm = Myallnews(request.POST, request.FILES, instance=pi)

                if fm.is_valid():
                    fm.save()

            else:
                fm = Myallnews(instance=pi)

            return render(request, 'updatenews.html', {'form': fm})

        except:
            return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/')
