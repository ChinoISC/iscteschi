from rest_framework.views import APIView
from django.shortcuts import render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from api.models import Activities
from datetime import date

class ActivityView(APIView):
    template_name="view_activities.html"
    @method_decorator(login_required(login_url='login')) 
    def get(self,request):
        id = request.user.id
        username = request.user.username
        activities = Activities.objects.all()
        context = {
            'id':id,
            'username': username,
            'activities':activities
        }
        return render(request,self.template_name,context)
    
class CreateActivity(APIView):
    template_name = "create_activity.html"
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        username = request.user.username
        
        context = {
            'username': username,
        }
        return render(request, self.template_name, context)
    def post(self, request):
        data = request.data
        title = data.get('title')
        description = data.get('description')
        color = data.get('color')
        
        # Obtiene el usuario actualmente autenticado
        user = request.user

        # Crea una nueva instancia de Activities con los valores proporcionados
        activity = Activities(
            title=title,
            descriptions=description,
            date_activities=date.today(),  # Obtiene la fecha actual
            completed=0,  # Establece el campo completed en 0
            color = color,
            fk_user=user  # Asigna el usuario actual
        )

        # Guarda la actividad en la base de datos
        activity.save()

        # Puedes redirigir al usuario a donde desees después de guardar la actividad
        # Por ejemplo, puedes redirigirlo a la página de detalles de la actividad
        # return redirect('detalle_actividad', id=activity.id)

        # O devolver una respuesta JSON si estás trabajando con una API
        return Response({'message': 'Actividad creada exitosamente'})

        