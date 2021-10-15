from django.contrib.auth.models import User
from django.test import TestCase

from basketball_ms.models import Group, UserGroup
from rest_framework.test import APIClient


class TestBasketBallManagementSystem(TestCase):

    @staticmethod
    def check_status(response):
        if response.status_code not in [200, 201]:
            raise Exception(f'{response.status_code} {response.data}')

    def setUp(self):
        """
        add users to test
        """
        self.create_groups()
        self.client = APIClient()

        # add admin user
        user = User.objects.create_user(
            username='admin', password='admin123')
        group = Group.objects.filter(group_category="ad").first()
        UserGroup.objects.create(
            user=user,
            group=group
        )

        # add coach
        user = User.objects.create_user(
            username='coach', password='coach123')
        group = Group.objects.filter(group_category="c").first()
        UserGroup.objects.create(
            user=user,
            group=group
        )

        # add player
        user = User.objects.create_user(
            username='player', password='player123')
        group = Group.objects.filter(group_category="p").first()
        UserGroup.objects.create(
            user=user,
            group=group
        )

    def create_groups(self):
        """
        generate group types
        """
        group_types = ['ad', 'c', 'p']
        for g_type in range(len(group_types)):
            try:
                group = Group(group_category=group_types[g_type])
            except Exception as e:
                raise Exception(e)
            group.save()

    # test functions begin here
    # scoreboard
    def test_admin_scoreboard(self):

        self.client.login(username='admin', password='admin123')
        self.check_status(self.client.get('/api/scoreboard/'))
        self.client.logout()

    def test_coach_scoreboard(self):

        self.client.login(username='coach', password='coach123')
        self.check_status(self.client.get('/api/scoreboard/'))
        self.client.logout()

    def test_player_scoreboard(self):

        self.client.login(username='player', password='player123')
        self.check_status(self.client.get('/api/scoreboard/'))
        self.client.logout()

    # teams
    def test_admin_teams(self):

        self.client.login(username='admin', password='admin123')
        self.check_status(self.client.get('/api/teams/'))
        self.client.logout()

    def test_coach_teams(self):

        self.client.login(username='coach', password='coach123')
        self.check_status(self.client.get('/api/teams/'))
        self.client.logout()

    # players
    def test_admin_players(self):

        self.client.login(username='admin', password='admin123')
        self.check_status(self.client.get('/api/players/'))
        self.client.logout()

    def test_coach_players(self):

        self.client.login(username='coach', password='coach123')
        self.check_status(self.client.get('/api/players/'))
        self.client.logout()

