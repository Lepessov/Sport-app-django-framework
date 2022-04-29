
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='sportpage'),
    path('football', views.football, name='football'),
    path('wrestling', views.wrestling, name='wrestling'),
    path('create_comment/', views.createComment, name='comment'),
    path('comment', views.Comments, name='comments'),
    path('football_comments', views.Football_comments, name='f_comment'),
    path('wrestling_comments', views.Wrestling_comments, name='w_comment'),
    path('hockey_comments', views.Hockey_comments, name='h_comment'),
    path('weightlifting_comments', views.Weightlifting_comments, name='we_comment'),
    path('boxing_comments', views.Boxing_comments, name='f_comment'),
    path('update_order/<str:pk>', views.updateComment, name='comment_update'),
    path('delete_order/<str:pk>', views.deleteComment, name='comment_delete'),
    path('champions/', views.Champs, name='champions'),
    path('registration', views.AddRegistration, name='registration'),
    path('user_info', views.user_info, name='user'),
    path('mail', views.send_file, name='mail')
]


