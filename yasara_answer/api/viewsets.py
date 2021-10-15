from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
from basketball_ms.models import Team, Player, Game
from basketball_ms.permission import IsAdminCoach, IsAuth
from .serializers import TeamSerializer, PlayerSerializer, ScoreBoardSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
import numpy as np
from rest_framework.response import Response


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAdminCoach]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAdminCoach]

    @action(detail=False, methods=['get'])
    def filter_players(self, request, *args, **kwargs):
        average_scores = Player.objects.values_list('average_score', flat=True)
        scores_arr = [int(score) for score in average_scores]

        percentile_score = np.percentile(scores_arr, 90)
        response = {}
        data = {}
        for score in scores_arr:
            # check whether the player score is in between percentile+5 and
            # percentile-5
            if percentile_score - 5 <= score <= percentile_score + 5:
                player = Player.objects.filter(average_score=score).first()
                response[str(player.user)] = score
        data['percentile_score'] = percentile_score
        data['players'] = response
        return Response(data=data)


class ScoreBoardViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = ScoreBoardSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuth]
