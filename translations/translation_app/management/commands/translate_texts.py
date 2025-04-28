from django.core.management.base import BaseCommand
from deep_translator import GoogleTranslator
from translation_app.models import TextEntry
from django.db import transaction

class Command(BaseCommand):
    help = 'Translate all English texts to French.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting translation process...")

        translator = GoogleTranslator(source='en', target='fr')

        # Only translate if french_text is empty
        entries = TextEntry.objects.filter(french_text__isnull=True)

        with transaction.atomic():
            for entry in entries:
                try:
                    french = translator.translate(entry.english_text)
                    entry.french_text = french
                    entry.save()
                    self.stdout.write(self.style.SUCCESS(f"Translated ID {entry.id}: {entry.english_text} -> {french}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error translating ID {entry.id}: {str(e)}"))

        self.stdout.write(self.style.SUCCESS("Translation completed."))