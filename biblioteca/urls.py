from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('livros.urls')),
    url(r'conta/', include('accounts.urls' , namespace='accounts')),

    
] 