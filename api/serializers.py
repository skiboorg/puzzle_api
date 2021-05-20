from rest_framework import serializers
from .models import *
from user.models import User

class RatingUserSerializer(serializers.ModelSerializer):
    games = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'nickname',
            'rating',
            'games',
            'avatar',
            'total_add'
        ]

    def get_games(self,obj):
        return Game.objects.filter(player=obj).count()


class FeedBackSerializer(serializers.ModelSerializer):
    user = RatingUserSerializer(many=False)
    class Meta:
        model = FeedBack
        fields = '__all__'

class GameLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    level = GameLevelSerializer(many=False)
    class Meta:
        model = Game
        fields = '__all__'




class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'