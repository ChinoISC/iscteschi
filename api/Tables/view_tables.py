from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from api.models import Activities
from datetime import date


class ViewTable(APIView):
    template_name="tables_activity.html"
    @method_decorator(login_required(login_url='login')) 
    def get(self,request):
        id = request.user.id
        username= request.user.username
        is_super = request.user.is_superuser
        activities = Activities.objects.all()
        context = {
            'id': id,
            'username':username,
            'is_super': is_super,
            'activities':activities
        }

        return render(request,self.template_name,context)
