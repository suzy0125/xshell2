from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('post/<int:post_id>',views.main, name = 'main'),
    path('post/new/', views.post_new, name = 'new'),
    path('post/<int:post_id>/edit/',views.post_edit,name='edit'),
    path('post/<int:post_id>/delete/',views.post_delete,name='delete'),
    path('post/<int:post_id>/comment', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete', views.comment_delete, name="delete_comment"),
    ]