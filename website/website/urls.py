"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.static import serve
from django.conf import settings
import authentification.views
import board_games.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', serve, {'path': 'static/favicon.ico', 'document_root': settings.BASE_DIR}),
    path('', board_games.views.home, name='home'),
    path('login/', authentification.views.login_custom, name='login'),
    path('logout/', authentification.views.logout_custom, name='logout'),
    path('signup/', authentification.views.signup, name='signup'),
    path('reset_password/', authentification.views.reset_password, name='reset_password'),
    path('delete_account/<int:id>', authentification.views.delete_account, name='delete_account'),
    path('advanced_search/', board_games.views.advanced_search, name='advanced_search'),
    path('add_game/', board_games.views.add_game, name='add_game'),
    path('game/<int:id>', board_games.views.game, name='game'),
    path('user/<int:id>', board_games.views.profil, name='profil'),
    path('stats/', board_games.views.stats, name='stats'),
    path('game/<int:id>/rate', board_games.views.rate_game, name='rate_game')
]
