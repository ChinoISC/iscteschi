from rest_framework.views import APIView
from django.shortcuts import render

class Home(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)

class Sign(APIView):
    template_name="forms-layouts.html"
    def get(self,request):
        return render(request,self.template_name)