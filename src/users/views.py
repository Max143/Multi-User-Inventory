from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 




def RegisterView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None, instance=request.user)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('stocks')
        else:
            form = UserRegistrationForm(request.POST)
            args = {'form':form}
        return render(reqeust, 'users/register.html', args)
    else:
        form = UserRegistrationForm(request.POST or None)
        args = {'form':form}
        return render(reqeust, 'users/register.html')



@login_required   
def ProfileView(request):    # it has default url route '/accout/profile/' which need to be changed in settings
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()             
            p_form.save()
            messages.success(request, f'Your Profile Has Been Updated !')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
        }
    return render(request, 'users/profile.html', context)