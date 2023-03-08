from django.shortcuts import render
from blogs.models import Post
from django.views import View
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
class viewIndex(View):
   
   def get(self,request ):
      Data = {'Posts': Post.objects.all().order_by('-date')[:2]}
      return render(request, 'pages/index.html',Data)
   

class viewAboutIndex(View):
   def get(self,request ):
      return render(request, 'pages/profile.html')

def loadMore(request):
      if request.method == 'POST' and request.POST['total_item']:
         offset = int(request.POST['total_item'])
         limit = 2
         totalData = Post.objects.count()
         post_object = Post.objects.all().order_by('-date')[offset:limit+offset]
         post_json = serializers.serialize('json', post_object)
         return JsonResponse(data={
             'posts': post_json,
             'totalResults': totalData
         })