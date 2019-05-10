
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
# from  .upload import upload_image
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager/',include('manager.urls',namespace='manager')),
    path('goods/',include('goods.urls',namespace='goods')),
    path('user/',include('user.urls',namespace='user')),
    path('store/',include('store.urls',namespace='store')),
    path('',include('home.urls',namespace="home")),
    # url(r'^admin/uploads/(?P<dir_name>[^/]+)',upload_image,name='upload_image'),
# ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
]