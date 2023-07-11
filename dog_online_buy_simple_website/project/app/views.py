from django.shortcuts import render
from app.models import Website


# Create your views here.
def index(request):
    website = Website.objects.all()
    return render(request,'app/index.html',{'website':website})
