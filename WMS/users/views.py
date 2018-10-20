from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #instantiate the form and pass in the post data

        if form.is_valid(): #data that is passed in is okay
            form.save() #creates a new user. Form is based off the user model.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username = username, password = password)

            login(request, user)
            return redirect('index')
    else:

        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/registration.html', context)