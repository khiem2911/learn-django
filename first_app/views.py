from django.shortcuts import render
from first_app.models import AccessRecord,Topic,Webpage,User,FormUser
from django.shortcuts import redirect
from . import form

def index(request):
    listUsers = FormUser.objects.all()
    user_dict = {'access_users': listUsers}
    return render(request,'list.html',context=user_dict)

def form_view(request):
    forms = form.FormName()
    if request.method == 'POST':
        forms = form.FormName(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    return render(request,'form.html',context={'form':forms})

    