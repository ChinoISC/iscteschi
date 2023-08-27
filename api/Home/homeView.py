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

class Home(APIView):
    template_name="index.html"
    @method_decorator(login_required(login_url='login')) 
    def get(self,request):
        return render(request,self.template_name)

class Sign(APIView):
    template_name="forms-layouts.html"
    @method_decorator(login_required(login_url='login')) 
    def get(self,request):
        return render(request,self.template_name)
    
class Login(APIView):
    template_name="pages-login.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Inicio de sesión exitoso'})
        else:
            return JsonResponse({'message': 'Credenciales inválidas'}, status=400)

class CreateUserView(APIView):
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



class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect(reverse('login')) 
