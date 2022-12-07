from django.urls import path
from .import views

urlpatterns = [ 
    path('',views.home,name='home'),
    path('exam',views.exam,name='exam'),
    path('add',views.add,name='add'),
    path('profile',views.profile,name='profile'),
    path('export_pdf',views.export_pdf,name='export_pdf'),
]