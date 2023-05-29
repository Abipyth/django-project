from django.contrib import admin
from django.urls import path
from uploadfiles import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('staffuploadfiles',views.staffuploadfiles,name='staffuploadfiles'),
    path('uploadfile',views.uploadfile,name='uploadfile'),
    path('deletefile/<int:id>',views.deletefile),
    path('studentReg',views.sturegister,name='stureg'),path('studentlogin',views.stulogin,name='stu_login'),
    path('staffreg',views.staffregister,name='staffreg'),
    path('stafflogin',views.stafflogin,name='stafflogin'),
    path('downloadfiles',views.downloadfiles,name='downloadfiles'),
    path('getuploadfiles',views.getuploadfile,name='getuploadfile')
]
urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)