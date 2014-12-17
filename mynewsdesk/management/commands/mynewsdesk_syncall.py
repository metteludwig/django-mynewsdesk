from django.core.management.base import BaseCommand, CommandError
from mynewsdesk import sync

class Command(BaseCommand):
    args = '[limit]'

    def handle(self, *args, **options):
        if len(args):
            r = sync.sync_all(limit=int(args[0]))
        else:
            r = sync.sync_all()

        print r