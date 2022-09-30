from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.create, name='create'),
    path('new/',views.new, name='new'),
    path('edit/<int:pkk>', views.edit, name='edit'),
    path('update/<int:pkk>', views.update, name='update'),
    path('detail/<int:pkk>', views.detail, name='detail'),
    path('delete/<int:pk>', views.delete, name='delete'),

    # path('update/<int:pk>', views.update, name="update"),
]