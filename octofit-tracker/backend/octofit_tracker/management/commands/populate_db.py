from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        tony = User.objects.create(email='tony@stark.com', username='IronMan', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', username='Batman', team=dc)
        clark = User.objects.create(email='clark@kent.com', username='Superman', team=dc)

        # Activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=date(2023, 1, 1))
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=date(2023, 1, 2))
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date=date(2023, 1, 3))
        Activity.objects.create(user=clark, type='Yoga', duration=20, date=date(2023, 1, 4))

        # Workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        w2 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio')
        w1.suggested_for.set([tony, steve])
        w2.suggested_for.set([bruce, clark])

        # Leaderboard
        Leaderboard.objects.create(user=tony, score=120)
        Leaderboard.objects.create(user=steve, score=110)
        Leaderboard.objects.create(user=bruce, score=130)
        Leaderboard.objects.create(user=clark, score=140)

        self.stdout.write(self.style.SUCCESS('octofit_db has been populated with test data.'))
