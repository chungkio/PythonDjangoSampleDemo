from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.
class IndexView(View):
    template_name = 'accounts/index.html'
    form_class = RegisterForm

    def get(self, request):
        if not request.user.is_authenticated:
            if 'action' in request.GET and request.GET['action'] == 'register':
                tab = {"tab" : " right-panel-active"}
            else:
                tab = {"tab" : "" }
            return render(request, self.template_name,tab)
        else:
            return render(request, 'accounts/my-account.html')


    def post(self, request):
        # check which form was submitted
        if 'register' in request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                # save user object and log him/her in automatically
                form.save()
                # authenticate user since form doesn't do it automatically
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                next_page = request.GET.get('next', '/')
                return redirect(next_page)
        elif 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # log the user in and redirect to the appropriate page
                login(request, user)
                next_page = request.GET.get('next', '/')
                return redirect(next_page)
        return render(request, self.template_name)

class AccountView(View):
    @login_required
    def my__acount(request):
        return render(request, 'accounts/my-account.html')
