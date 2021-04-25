from django.contrib import admin
from .models import Map, Service, Token, Profile


admin.site.register(Map)
admin.site.register(Service)
admin.site.register(Token)
admin.site.register(Profile)
