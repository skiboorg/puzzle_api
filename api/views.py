# coding utf-8
from decimal import Decimal

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from .models import *
from datetime import datetime
import datetime as dt
from datetime import datetime
from django.utils import timezone

class GetGameLevels(generics.ListAPIView):
    serializer_class = GameLevelSerializer
    queryset = Level.objects.all()


class StartGame(APIView):
    def post(self,request):
        data = request.data
        print(data)
        user = request.user
        if user.is_authenticated:

            game = Game(
                player=user,
                level_id=data.get('level_id'),
                game_type=data.get('type')
            )
            # user.games_count -= 1
            # user.save()

        else:
            game = Game(
                level_id=data.get('level_id'),
                game_type=data.get('type')
            )
        game.save()


        return Response ({'id':game.id,'img':game.image.url}, status=200)





class SliderWin(APIView):
    def post(self, request):
        data = request.data
        game = Game.objects.get(id=data.get('game_id'))
        if game.player:
            game.player.rating += 20
            game.result = True
            game.save()
            game.player.save()
        return Response(status=200)

class EndGame(APIView):
    def post(self, request):
        data = request.data
        request_type = data.get('request_type')
        game_status = data.get('game_status')
        print(data)
        game = Game.objects.get(id=data.get('game_id'))
        if game.player:
            if request_type == 'remove_rating':
                game.player.rating -= game.level.rating
            elif request_type == 'add_rating':
                if game_status:
                    game.player.rating += game.level.rating
                    game.player.balance += Decimal(0.02)
                    game.result = game_status
                else:
                    game.player.rating += game.level.rating
                    game.result = game_status
            game.save()
            game.player.save()
        return Response(status=200)


class AddFb(APIView):
    def post(self,request):
        print(request.data)
        data = request.data
        new_fb = FeedBack.objects.create(user=request.user,text=data.get('message'))
        if request.FILES:
            files = request.FILES.getlist('image')
            for file in files:
                new_fb.image = file
                new_fb.save()
        return Response (status=200)

class AllFb(generics.ListAPIView):
    serializer_class = FeedBackSerializer
    queryset = FeedBack.objects.filter(is_active=True)

class AddMoneyRatings(generics.ListAPIView):
    serializer_class = RatingUserSerializer
    queryset = User.objects.all().order_by('-total_remove')

class Ratings(generics.ListAPIView):
    serializer_class = RatingUserSerializer
    queryset = User.objects.all().order_by('-rating')
class GameHistory(generics.ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        return Game.objects.filter(player=self.request.user).order_by('-date')

class GetAd(generics.RetrieveAPIView):
    serializer_class = AdSerializer

    def get_object(self):
        return Ad.objects.random(1).first()
