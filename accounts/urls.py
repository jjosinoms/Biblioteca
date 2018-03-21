from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^entrar/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}, name='login'), 
	url(r'^cadastro/$', 'accounts.views.register', name='register'), 
	url(r'^logout/$','django.contrib.auth.views.logout' ,{'next_page': 'home'}, name='logout'),

]