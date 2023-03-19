from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request,'first_app/index.html',context=date_dict)

def help(request):
    my_dict = {'help_doc' : 'Help Page'}
    return render(request,'first_app/help.html',context=my_dict)