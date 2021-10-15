from basketball_ms.models import Game, UserGroup, Player, Team, Coach


def scoreboard(request):
    games = Game.objects.all()
    # user_group = UserGroup.objects.get(user_id=request.user.id)
    response = {
        'games': games
        # 'user_role': user_group,
    }
    print('UUUUUUUUUUUUUU')
    print(response)
    print('UUUUUUUUUUUUUU')
    return response


def team(request):
    pass


def coach(request, id=None):
    teams = Coach.objects.filter(id=id).first()
    response = {
        'team': teams.team
    }
    return response


def player(request, id=None):
    player = Player.objects.filter(id=id).first()
    response = {
        'player': player,
        'player_id': player.id,
        'team': player.team.name,
        'no_of_games': player.no_of_games,
        'average_score': player.average_score
    }
    return response