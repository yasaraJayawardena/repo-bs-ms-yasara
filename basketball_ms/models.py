from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Group(models.Model):
    ADMIN = 'ad'
    COACH = 'c'
    PLAYER = 'p'

    GROUP_TYPES = [
        (ADMIN, 'League Admin'), (COACH, 'coach'),
        (PLAYER, 'Player')
    ]

    group_category = models.CharField(max_length=10, choices=GROUP_TYPES,
                                      default=ADMIN)

    def __str__(self):
        return str(self.group_category)

    def get_id(self):
        return str(self.id)


class UserGroup(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_logged_in = models.BooleanField(default=False)


class UserStatus(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    log_in_time = models.DateTimeField(default=timezone.now)
    log_out_time = models.DateTimeField()


class Team(models.Model):
    name = models.CharField(max_length=100)


class Player(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    height = models.IntegerField()
    average_score = models.CharField(max_length=100)
    no_of_games = models.IntegerField()


class Coach(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Game(models.Model):
    FIRST_ROUND = 'FR'
    SECOND_ROUND = 'SR'
    THIRD_ROUND = 'TR'
    WINNER = 'W'

    GAME_ROUNDS = [
        (FIRST_ROUND, 'First round'), (SECOND_ROUND, 'Second round'),
        (THIRD_ROUND, 'Third round'), (WINNER, 'Winner')
    ]

    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1', null=True)
    team1_score = models.IntegerField(null=True)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2', null=True)
    team2_score = models.IntegerField(null=True)
    game_round_number = models.CharField(
        max_length=2,
        choices=GAME_ROUNDS,
        default=FIRST_ROUND
    )


class TeamStatus(models.Model):
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_score = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)


class PlayerStatus(models.Model):
    player_name = models.ForeignKey(Player, on_delete=models.CASCADE)
    player_score = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)