from rest_framework import serializers

from basketball_ms.models import Team, Player, Game


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class ScoreBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
