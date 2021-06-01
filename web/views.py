from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse

from .forms import ProfileForm


def index(request):
    return render(request, "index.html")


def profile_reg(request):
    register = False
    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST)
        if profile_form.is_valid():
            user = profile_form.save()
            user.set_password(user.password)
            profile_form.user = user
            profile_form.save()
            user.save()
            register = True
            to = user.email
            # send an email

        else:
            HttpResponse("<h2>Something Went Wrong with Form</h2>")

    else:
        profile_form = ProfileForm(data=request.POST)

    return render(request, 'registration.html', {'profile_form': profile_form, 'register': register, })

def contact(request):
    return render(request, "contact.html")