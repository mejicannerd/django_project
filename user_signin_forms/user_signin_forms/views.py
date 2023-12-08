from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def sign_new_user(request):
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                saveuser = User.objects.create_user(request.POST.get('username'),passoword=request.POST.get('password1'))
                saveuser = saveuser()
                return render(request, 'sign_up.html', {'form':UserCreationForm(),'info':'The User ' + request.POST.get('username') + 'is saved successfully'})
            except IntegrityError:
                 return render(request, 'sign_up.html', {'form':UserCreationForm(),'error':'The User ' + request.POST.get('username') + 'Already exists..!'})
        else:
            return render(request, 'sign_up.html', {'form':UserCreationForm(),'error':'The Passwords are Not Matching..!'})
             
    else:
            return render(request, 'sign_up.html',{'form':UserCreationForm})
