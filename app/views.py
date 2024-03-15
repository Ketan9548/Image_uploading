from django.shortcuts import render
from .form import ImageForm
from .models import Imges

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Imges.objects.all()
    return render(request, 'home.html', {'img':img,'form':form})