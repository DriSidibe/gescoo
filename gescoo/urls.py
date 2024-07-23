from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gescoo_app.urls')),
    path('account/', include('account.urls'))
]
