from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from myapp.models import SpecialNews, Comment
from myapp.forms import SpecialnewsForm


class SpecialView(View):
    def get(slef, request):
        allnews = SpecialNews.objects.all()
        return render(request, 'special.html', {'news': allnews})


def shownews(request, id):
    mainid = SpecialNews.objects.get(pk=id)
    mycomment = Comment.objects.all().order_by('-id')
    if request.method == "POST":

        comment = request.POST.get('comment')
        comments = Comment(user=request.user, comment=comment)

        comments.save()
    else:
        return render(request, 'specialnewshow.html', {'mynews': mainid, 'mycomment': mycomment})

    return render(request, 'specialnewshow.html', {'mynews': mainid, 'mycomment': mycomment})


def updatenews1(request, id):
    if request.user.is_authenticated:
        try:
            pi = SpecialNews.objects.get(id=id)
            if request.method == "POST":
                fm = SpecialnewsForm(request.POST, request.FILES, instance=pi)

                if fm.is_valid():
                    fm.save()

            else:
                fm = SpecialnewsForm(instance=pi)

            return render(request, 'updatenews1.html', {'form': fm})

        except:
            return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/')
