from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistration
from .models import User
from django.contrib import messages
from django.contrib.messages import constants

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
# Create your views here.

# This function will add new item and show all items


def addshow(request):
    if request.method == 'POST':
        stud = None
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            fl = fm.cleaned_data['fnames']
            ln = fm.cleaned_data['lname']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = User(fnames=fl, lname=ln, email=em, password=pw)
            if len(pw) < 6:
                # fl = fm.cleaned_data['fnames']
                # ln = fm.cleaned_data['lname']
                # em = fm.cleaned_data['email']
                # pw = fm.cleaned_data['password']

                messages.add_message(request, constants.SUCCESS, 'Message')
                fm = UserRegistration()
            else:
                reg.save()
                fm = UserRegistration()

    else:
        fm = UserRegistration()
    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


# This function will update / Edit
def update_data(request, id):
    fm = None
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = UserRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi = User.objects.get(pk=id)
            fm = UserRegistration(instance=pi)
    return render(request, 'enroll/updateuser.html', {'form': fm})


# This function will delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
