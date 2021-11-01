from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

def home(request):
    return render(request, 'chat/index.html')


def about(request):
    return render(request, 'chat/about.html')


@login_required
def room_select(request):
    return render(request, 'chat/room_select.html')


@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})

@login_required
def general_chat(request):
    return render(request, 'chat/general_room.html')


@login_required
def programming_chat(request):
    return render(request, 'chat/programming_room.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm()
        if u_form.is_valid():
            u_form.save()
            return redirect('chat-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
    
    return render(request, 'chat/profile.html', context={'u_form': u_form})


class UserLogin(LoginView):
    template_name = 'chat/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('chat-select')


class UserRegister(FormView):
    template_name = 'chat/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('chat-select')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegister, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('chat-select')
        return super(UserRegister, self).get(request, *args, **kwargs)
