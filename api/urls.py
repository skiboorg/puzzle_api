from django.urls import path,include
from . import views

urlpatterns = [
    path('game_levels', views.GetGameLevels.as_view()),
    path('start_game', views.StartGame.as_view()),
    path('end_game', views.EndGame.as_view()),
    path('slider_win', views.SliderWin.as_view()),
    path('game_history', views.GameHistory.as_view()),
    path('ratings', views.Ratings.as_view()),
    path('add_money_ratings', views.AddMoneyRatings.as_view()),
    path('ad', views.GetAd.as_view()),
    path('add_fb', views.AddFb.as_view()),
    path('all_fb', views.AllFb.as_view()),


]
