from django.shortcuts import render
from user_app.models import User

# Create your views here.
def index(request):
    mydict = {'userlist':User.objects.order_by('first_name')}
    return render(request,'user_app/index.html',context=mydict)