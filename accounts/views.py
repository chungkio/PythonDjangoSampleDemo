from django.shortcuts import render
from django.views import View

# Create your views here.
class viewAccountIndex(View):
   def get(self,request ):
      return render(request, 'accounts/index.html')


def my__acount(request ):
   return render(request, 'accounts/my-account.html')