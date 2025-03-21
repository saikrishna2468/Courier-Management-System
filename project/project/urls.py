from django.contrib import admin
from django.urls import path
from app.views import index, login, registeration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('register', registeration, name="registeration"),
    path('login', login, name="login"),
]
