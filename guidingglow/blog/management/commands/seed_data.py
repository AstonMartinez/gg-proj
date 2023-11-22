from django.core.management.base import BaseCommand
from blog.seed_scripts import seed_users, seed_blogs, seed_comments, seed_likes
from tracker.seed_scripts import seed_symptoms, seed_journals

class Command(BaseCommand):
    help = 'Seed data for users, symptoms, journals, blogs, comments, and likes'

    def handle(self, *args, **options):
        seed_users()
        seed_symptoms()
        seed_journals()
        seed_blogs()
        seed_comments()
        seed_likes()

        self.stdout.write(self.style.SUCCESS('Successfully seeded data'))
