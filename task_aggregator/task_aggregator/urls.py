from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from swagger_render.views import SwaggerUIView

from aggregator.views.register import RegisterView

urlpatterns = [
    path('', include('aggregator.urls')),

    path('admin/', admin.site.urls),
    path('swagger/', SwaggerUIView.as_view()),

    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]

urlpatterns += static('/../docs/', document_root='docs')
