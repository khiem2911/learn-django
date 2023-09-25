from django.shortcuts import render
from first_app.models import AccessRecord,Topic,Webpage,User

# Create your views here.
def index(request):
    listUsers = User.objects.all()
    user_dict = {'access_users': listUsers}
    return render(request,  'list.html',context=user_dict)