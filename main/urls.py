from django.urls import path
from .import views


app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('graphic-design', views.graphic_design, name='graphic_design'),
    path('tshirt-printing', views.tshirt_printing, name='tshirt_printing'),
    path('2D&3D-Signages', views.signages, name='signages'),
    path('promotional-materials', views.promotional_materials, name='promotional_materials'),
    path('banners-and-stickers', views.banners_stickers, name='banners_stickers'),
    path('contact-us', views.contact, name='contact'),
    path('ajax-contact/', views.process_contact, name='contact_post'),    
]