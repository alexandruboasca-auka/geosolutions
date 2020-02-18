from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from geosolutions_app.models import Point

class Command(BaseCommand):
    help = 'Fill database with points'

    def add_arguments(self, parser):
        parser.add_argument('number_of_points', nargs='+', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        for i in range(0, options['number_of_points'][0]):
            fake_point = fake.latlng()
            point = Point(
                x=fake_point[0],
                y=fake_point[1],
            )

            try:
                point.save()
            except IntegrityError:
                raise 'Point already exists, continuing...'

        self.stdout.write(self.style.SUCCESS('Successfully added "%s" points' % options['number_of_points'][0]))