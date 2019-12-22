from django.urls import path
from .import views
urlpatterns=[
    path('profile/',views.profile,name="profile"),
    path('content/',views.content,name="content"),
    path('delete/<int:id>',views.destroy),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>',views.update),
    
]