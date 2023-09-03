from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from api.models import Activities
from datetime import date


class ActivityView(APIView):
    template_name="view_activities.html"
    @method_decorator(login_required(login_url='login')) 
    def get(self,request):
        id = request.user.id
        username = request.user.username
        is_super = request.user.is_superuser
        activities = Activities.objects.all()
        context = {
            'id':id,
            'username': username,
            'is_super': is_super,
            'activities': activities
        }
        return render(request,self.template_name,context)



class CreateActivity(APIView):

    template_name = "create_activity.html"

    @method_decorator(login_required(login_url='login')) 
    def get(self, request):
        username = request.user.username
        is_super = request.user.is_superuser
        
        context = {
            'username': username,
            'is_super': is_super
        }
        return render(request, self.template_name, context)
    def post(self, request):
        data = request.data
        title = data.get('title')
        description = data.get('description')
        color = data.get('color')
        
        user = request.user
        activity = Activities(
            title=title,
            descriptions=description,
            date_activities=date.today(), 
            completed=0,  
            color = color,
            fk_user=user  
        )


        activity.save()
        return Response({'message': 'Actividad creada exitosamente'})



class CompletedActivity(APIView):
    def get(self,request):
        activity_id = request.GET.get('id')
        try:
            # Busca la actividad en la base de datos por su ID
            activity = Activities.objects.get(id=activity_id)
            
            # Cambia el estado 'completed' de la actividad
            activity.completed = True  # Invierte el estado actual
            
            # Guarda los cambios en la base de datos
            activity.save()

            return Response({'message': "El estatus de la actividad cambió"})
        except Activities.DoesNotExist:
            return Response({'message': "La actividad no existe"}, status=404)



class EditActivity(APIView):

    template_name="update_activity.html"
    @method_decorator(login_required(login_url='login')) 
    def get(self,request):
        is_super = request.user.is_superuser
        activity_id = request.GET.get('id')
        try:
            # Busca la actividad en la base de datos por su ID
            activity = Activities.objects.get(id=activity_id)
            
            context ={
                'is_super':is_super,
                'activity':activity
            }

            return render(request, self.template_name, context)
        except Activities.DoesNotExist:

            return Response({'message': "La actividad no se puede editar"}, status=404)
    def post(self,request):
        data = request.data
        activity_id = data.get('id')
        new_title = data.get('title')
        new_description = data.get('description')
        new_color = data.get('color')
        try:
            Activities.objects.filter(id=activity_id).update(
            title=new_title,
            descriptions=new_description,
            color=new_color
            )    
            return Response({'message': "La actividad se actualizo"})
        except Activities.DoesNotExist:
            return Response({'message': "La actividad no existe"}, status=404)



class DeleteActivity(APIView):
    def get(self, request):
        activity_id = request.GET.get('id')
        try:
            # Busca la actividad en la base de datos por su ID
            activity = Activities.objects.get(id=activity_id)
            
            # Elimina la actividad de la base de datos
            activity.delete()

            return Response({'message': "La actividad se eliminó correctamente"})
        except Activities.DoesNotExist:
            return Response({'message': "La actividad no existe"}, status=404)
