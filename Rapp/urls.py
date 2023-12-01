from django.urls import path
from . import views
from django.contrib.auth import views as ad

urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('menu/',views.menu,name="mn"),
    path('shop/',views.shop,name="sh"),
    path('reg/',views.registration,name="rg"),
    path('login/',ad.LoginView.as_view(template_name="html/login.html"),name="ln"),
    path('logout/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lt"),
    path('upload/',views.upload,name="up"),
    path('cnt/',views.contact,name="ct"),
    path('slot/',views.booking,name="sb"),
    path('page/',views.page,name="pa"),
    path('table/',views.table,name="ta"),
]