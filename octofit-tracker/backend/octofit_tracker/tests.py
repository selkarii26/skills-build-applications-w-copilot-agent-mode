from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel", description="Marvel Team")
        self.user = User.objects.create(email="tony@stark.com", username="IronMan", team=self.team)
    def test_user_creation(self):
        self.assertEqual(self.user.email, "tony@stark.com")
        self.assertEqual(self.user.team.name, "Marvel")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="DC", description="DC Team")
        self.assertEqual(team.name, "DC")

class ActivityModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel", description="Marvel Team")
        self.user = User.objects.create(email="bruce@banner.com", username="Hulk", team=self.team)
        self.activity = Activity.objects.create(user=self.user, type="Running", duration=30, date="2023-01-01")
    def test_activity_creation(self):
        self.assertEqual(self.activity.type, "Running")

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Pushups", description="Upper body strength")
        self.assertEqual(workout.name, "Pushups")

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel", description="Marvel Team")
        self.user = User.objects.create(email="natasha@romanoff.com", username="BlackWidow", team=self.team)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)
    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 100)
