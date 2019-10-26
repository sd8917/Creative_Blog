
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('', views.BlogView, name='post' ),
    path('blog/<slug:slug>/',views.BlogDetail,name='detail')

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)