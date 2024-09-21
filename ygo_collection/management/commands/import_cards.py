from django.core.management.base import BaseCommand
import pandas as pd
from ygo_collection.models import Card

class Command(BaseCommand):
    help = 'Import cards from a Pandas DataFrame'

    def add_arguments(self, parser):
        parser.add_argument('file_path',
                            type=str,
                            help='Path to the Excel file to import')
    
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        # Load your DataFrame (replace this with your actual file)
        df = pd.read_excel(file_path)

        # Update db with Card objects from Excel file
        for _, row in df.iterrows():
            Card.objects.update_or_create(
                name=row['Name'],
                quantity=row['Amount'],
                quantity_sd=row['SD'],
                in_decks=row['In decks'],
                in_decks_sd=row['SD in decks'],
            )
        
        self.stdout.write(self.style.SUCCESS(
            f"Successfully imported {df.shape[0]} cards.")
        )