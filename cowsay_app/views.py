from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from cowsay_app.forms import AddCowForm
from cowsay_app import models
import subprocess
# Create your views here.
def index_view(request): 
    if request.method == "POST":
        form = AddCowForm(request.POST)
        if form.is_valid():
            
            data = form.cleaned_data
            args_data = data.get('cowsay')
            sub_process_1 = subprocess.run(['cowsay',args_data],capture_output=True, text=True)
            print(sub_process_1.stdout)
            models.Cow.objects.create(
                cowsay = data.get('cowsay')
            )
            context = {'form':AddCowForm(),'sub_process_data':sub_process_1.stdout}
            
            return render(request,'index_view.htm',context)
            
    context = {'form':AddCowForm()}
    return render(request,'index_view.htm',context)

def detail_view(request): 
    all_voices = models.Cow.objects.filter().order_by('-id')[:10]
    context = {'all_voices':all_voices,}
    return render(request,'detail_view.htm',context)


