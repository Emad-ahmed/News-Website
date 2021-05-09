from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.cache import cache
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render


@receiver(post_save, sender=User)
def shownotification(sender, instance, created, **kwargs):
    if created:
        subject = "hello"
        message = f"Successfully Signed Up {User}"
        from_mail = 'amadahmed1234678@gmail.com'
        my_mail = [instance.email]
        send_mail(subject, message, from_mail, my_mail, fail_silently=True)

    else:
        print("Info Updated")


@receiver(user_logged_in, sender=User)
def login_man(sender, request, user, **kwargs):

    ct = cache.get('comm',  version=user.pk)

    cache.set('comm', user.username, version=user.pk)

    return render(request, 'newsshow.html', {'ct': ct})
