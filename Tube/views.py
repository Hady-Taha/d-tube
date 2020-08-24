from django.shortcuts import render,HttpResponse
from pytube import YouTube
from .forms import url

# Create your views here.
def home(request):
    if request.method=='POST':
        form=url(request.POST)
        if form.is_valid():
            u=form.cleaned_data['url']
            try:
                yt=YouTube(u)
                yt.streams.first().download()
            except:
                ex="خف وحط لينك يوتيوب"
              
    else:
        form=url()

    
    context={
        'title':'home',
        'form':form,
        }
    return render(request,'Tube/index.html',context)
