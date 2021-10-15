from yasara_answer.api.viewsets import TeamViewSet, PlayerViewSet, \
    ScoreBoardViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teams', TeamViewSet),
router.register('players', PlayerViewSet),
router.register('scoreboard', ScoreBoardViewSet)
