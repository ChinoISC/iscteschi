from rest_framework.views import APIView
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from api.models import Activities

class Home(APIView):
    template_name="index.html"
    @method_decorator(login_required(login_url='login')) 
    def get(self,request):
        id = request.user.id
        username = request.user.username
        is_super = request.user.is_superuser
        activities = Activities.objects.all().order_by('-date_activities')[:3]

        context = {
            'id': id,
            'username': username,
            'is_super': is_super,
            'activities':activities
        }
        return render(request,self.template_name,context)

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





class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect(reverse('login')) 

