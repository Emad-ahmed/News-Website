from django.urls import path
from myapp.views import HomeView, fullnews, breaknews, LoginView, SignupView, user_logout, editmain, cpass, search, addnews, updatenews, SpecialView, shownews, updatenews1

urlpatterns = [
    path('',  HomeView.as_view(), name='home'),
    path('special',  SpecialView.as_view(), name='special'),
    path('fullnews/<int:id>/',  fullnews, name='fullnews'),
    path('breaknews/<int:id>/',  breaknews, name='breaknews'),
    path('shownews/<int:id>/',  shownews, name='shownews'),
    path('login',  LoginView.as_view(), name='login'),
    path('signup',  SignupView.as_view(), name='signup'),
    path('logout',  user_logout, name='logout'),
    path('editmain',  editmain, name='editmain'),
    path('cpass',  cpass, name='cpass'),
    path('cpass',  cpass, name='cpass'),
    path('search',  search, name='search'),
    path('addnews',  addnews, name='addnews'),
    path('updatenews/<int:id>/',  updatenews, name='updatenews'),
    path('updatenews1/<int:id>/',  updatenews1, name='updatenews1'),

]
