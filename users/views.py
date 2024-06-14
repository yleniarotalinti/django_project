from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def regist_new_user(request):
    # if the request is a POST request it means that the user has submitted the form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            # redirect to the name_of_the_app:name_of_the_url
            return redirect('/')
        else:
            print('Form is not valid')
    else:
        form = UserCreationForm()
    # the third argument is a parameter that we can pass to the html    
    return render(request, 'registration.html', {'form': form})