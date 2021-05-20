from django.urls import path,include
from . import views

urlpatterns = [


    path('me', views.GetUser.as_view()),
    path('game_count', views.GetUserGameCount.as_view()),
    path('add_money', views.AddMoney.as_view()),
    path('remove_money', views.RemoveMoney.as_view()),
    path('update', views.UserUpdate.as_view()),
    path('recover_password', views.UserRecoverPassword.as_view()),

]
