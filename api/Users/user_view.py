from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class CreateUserView(APIView):
    def is_superuser(user):
        return user.is_superuser

    def post(self, request):
        data = request.data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        username = data.get('username')
        password1 = data.get('password1')
        password2 = data.get('password2')

        # Realiza validaciones aquí si es necesario
        
        if password1 != password2:
            return Response({'message': 'Las contraseñas no coinciden'}, status=status.HTTP_400_BAD_REQUEST)

        hashed_password = make_password(password1)
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=hashed_password
        )

        if user:
            return Response({'message': 'Datos insertados exitosamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Error al insertar datos en la base de datos'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    template_name="create_user.html"
    @method_decorator(user_passes_test(is_superuser), name='get')
    @method_decorator(login_required(login_url='login')) 
    def get(self,request):
        username = request.user.username
        is_super = request.user.is_super
        context = {
            'username': username,
            'is_super': is_super
        }
        return render(request,self.template_name, context)