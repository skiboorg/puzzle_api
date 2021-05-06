import json
import uuid

from django.http import HttpResponseRedirect


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import create_random_string
from .serializers import *
from .models import *
from rest_framework import generics
from datetime import datetime
import datetime as dt
from datetime import datetime
from django.utils import timezone
from api.models import Game


class UserUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        userData = json.loads(request.data['userData'])
        serializer = UserSerializer(user, data=userData)
        if userData.get('pass') != '':
            user.set_password(userData.get('pass'))
            user.save()
        if serializer.is_valid():
            serializer.save()
            for f in request.FILES.getlist('avatar'):
                user.avatar = f
                user.save(force_update=True)
            return Response(status=200)
        else:
            return Response(status=400)


class GetUser(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
    # def get(self, request):
    #     user = request.user
    #     serializer = UserSerializer(user, many=False)
    #     return Response(serializer.data)


class GetUserGameCount(APIView):
    def get(self, request):
        user = request.user
        today = timezone.now()

        game = Game.objects.filter(player=user).last()
        last_game = game.date
        print(today - last_game)
        if today - last_game > dt.timedelta(days=1):
            user.games_count = 3
            user.save()
        return Response({'games':user.games_count}, status=200)

class UserRecoverPassword(APIView):
    def post(self,request):
        user = None
        try:
            user = User.objects.get(phone=request.data['phone'])
        except:
            user = None
        if user:
            messageSend = True
            return Response({'result': True, 'email': user.email}, status=200)
        else:
            return Response({'result': False}, status=200)
