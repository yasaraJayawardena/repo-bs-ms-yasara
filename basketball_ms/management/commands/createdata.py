from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from faker import Faker
from django.contrib.auth.models import User
from basketball_ms.models import Team, UserGroup, Player, \
    Coach, Group, Game


class Command(BaseCommand):
    help = "Command information"

    def create_groups(self, fake):
        """
        generate group types
        :param fake:
        """
        group_types = ['ad', 'c', 'p']
        for g_type in range(len(group_types)):
            try:
                group = Group(group_category=group_types[g_type])
            except Exception as e:
                raise Exception(e)
            group.save()

    def create_teams(self, fake, team_id):
        """
        generate team names
        :param
        """
        if team_id > 16:
            team_id = 16
        team = Team.objects.filter(id=team_id).first()
        if not team:
            team = Team(id=team_id, name=fake.slug())
            team.save()
        return team

    def create_user_groups(self, fake):
        """
        generate user groups(roles) as players and coach
        :param fake:
        """

        users = User.objects.filter(is_superuser=False)
        player = get_object_or_404(Group, group_category='p')
        coach = get_object_or_404(Group, group_category='c')
        league_admin = get_object_or_404(Group, group_category='ad')

        # adding players
        for user in users[:83]:
            try:
                pl = UserGroup(user_id=user.id, group_id=player.id,
                               is_logged_in=fake.pybool())
            except Exception as e:
                raise Exception(e)
            pl.save()

        # adding coaches
        for user in users[83:99]:
            try:
                co = UserGroup(user_id=user.id, group_id=coach.id,
                               is_logged_in=fake.pybool())
            except Exception as e:
                raise Exception(e)
            co.save()

        # add super admin
        for user in users[83:]:
            try:
                ad = UserGroup(user_id=user.id, group_id=league_admin.id,
                               is_logged_in=fake.pybool())
            except Exception as e:
                raise Exception(e)
            ad.save()

    def play_a_round(self, teams, round_name, fake):
        """
        to get the winners of first round
        :param round_name:
        :param teams:
        :param fake:
        """

        limit = 2
        offset = 0

        while offset < len(teams):
            playing_teams = teams[offset:offset + limit]
            Game.objects.create(
                team1=playing_teams[0],
                team1_score=fake.random_int(min=2, max=186),
                team2=playing_teams[1],
                team2_score=fake.random_int(min=2, max=186),
                game_round_number=round_name
            )

            offset += limit

    def get_winners(self, round_name):
        """
        to get the winners
        :param round_name:
        """

        games = Game.objects.filter(game_round_number=round_name)
        winning_teams = []
        for game in games:
            if game.team1_score < game.team2_score:
                winning_teams.append(game.team2.id)
            else:
                winning_teams.append(game.team1.id)

        return Team.objects.filter(id__in=winning_teams)

    def add_users(self, fake):
        """
        to add Admin, Coaches and Players
        :param fake:
        """
        # add total 177 users
        # players 160
        # coach 16
        # admin 1

        for i in range(1, 177):
            print("----Adding Users with user type---------------")
            username = fake.name()
            print(f"username -------{username}")

            user = User.objects.create_user(username=username,
                                            password="123",
                                            email=fake.ascii_company_email(),
                                            first_name=fake.first_name(),
                                            last_name=fake.last_name())
            if i < 177:
                team = self.create_teams(fake, int(i / 11) + 1)
                if len(Player.objects.filter(team=team)) < 10:
                    print(f"user type -player")
                    group = Group.objects.get(group_category="p")
                    Player.objects.create(
                        user=user,
                        team=team,
                        height=fake.random_int(min=150, max=255),
                        average_score=fake.random_int(max=186),
                        no_of_games=fake.random_int(max=400)
                    )
                else:
                    print(f"user type -coach")
                    group = Group.objects.get(group_category="c")
                    Coach.objects.create(
                        user=user,
                        team=team
                    )

            UserGroup.objects.create(
                user=user,
                group=group
            )
        # admin user
        user = User.objects.create_user(username="admin",
                                        password="Admin123",
                                        email=fake.ascii_company_email(),
                                        first_name=fake.first_name(),
                                        last_name=fake.last_name())
        group = Group.objects.get(group_category="ad")
        UserGroup.objects.create(
            user=user,
            group=group
        )

    def clear_data(self):
        """
        to clear the models before initiating new data
        """

        User.objects.all().delete()
        UserGroup.objects.all().delete()
        Player.objects.all().delete()
        Team.objects.all().delete()
        Coach.objects.all().delete()
        Group.objects.all().delete()
        Game.objects.all().delete()

    def handle(self, *args, **options):

        # To clear all data in the models before initiating new data
        self.clear_data()

        # Creating the fake object
        fake = Faker()

        # Adding data to models
        self.create_groups(fake)

        # The user name and user type should be identified from here in order
        # to access APIs with permissions
        self.add_users(fake)

        self.create_user_groups(fake)

        # play first round
        self.play_a_round(Team.objects.all(), "FR", fake)

        # play 2 round
        self.play_a_round(self.get_winners("FR"), "SR", fake)

        # play 3 round
        self.play_a_round(self.get_winners("SR"), "TR", fake)

        # play 4 round
        self.play_a_round(self.get_winners("TR"), "W", fake)
