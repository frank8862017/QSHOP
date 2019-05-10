from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^store_list/',views.store_list,name='store_list'),
    url(r'^store_details/',views.store_details,name='store_details'),
]
app_name="store"