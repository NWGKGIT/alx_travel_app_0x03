# listings/management/commands/seed.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seeds the database with sample listings data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # Get the User model
        User = get_user_model()

        # 1. Get or create a host user
        # (Assumes your CustomUser model uses 'email' as USERNAME_FIELD)
        # Adjust 'username' and 'email' as needed for your user model
        try:
            # Try to find a user by email
            host_user = User.objects.get(email='host@example.com')
        except User.DoesNotExist:
            # Create a new user if one doesn't exist
            self.stdout.write('Creating new host user...')
            # Check if 'username' is required
            if 'username' in [f.name for f in User._meta.fields]:
                host_user = User.objects.create_user(
                    username='host_user',
                    email='host@example.com',
                    password='seedpassword123',
                    first_name='Host',
                    last_name='User'
                )
            else:
                 # Assumes email is the username field
                host_user = User.objects.create_user(
                    email='host@example.com',
                    password='seedpassword123',
                    first_name='Host',
                    last_name='User'
                )

        # 2. Clear existing listings to avoid duplicates
        self.stdout.write('Deleting old listings...')
        Listing.objects.all().delete()

        # 3. Create new sample listings
        listings_data = [
            {
                'host': host_user,
                'title': 'Cozy Beachfront Cottage',
                'description': 'A beautiful cottage right on the beach. Perfect for a romantic getaway.',
                'address': '123 Ocean Drive, Beach City',
                'price_per_night': Decimal('175.00'),
                'bedrooms': 2,
                'bathrooms': 1
            },
            {
                'host': host_user,
                'title': 'Modern Downtown Loft',
                'description': 'A stylish loft in the heart of the city. Close to all attractions.',
                'address': '456 Main Street, Metroville',
                'price_per_night': Decimal('220.00'),
                'bedrooms': 1,
                'bathrooms': 1
            },
            {
                'host': host_user,
                'title': 'Secluded Mountain Cabin',
                'description': 'Escape to the mountains. This cabin offers peace, quiet, and stunning views.',
                'address': '789 Pine Road, Summit Peak',
                'price_per_night': Decimal('130.00'),
                'bedrooms': 3,
                'bathrooms': 2
            }
        ]

        for data in listings_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(listings_data)} listings!'))