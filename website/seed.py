from .models import *
from django.db.models import *
import random
from faker import Faker
fake = Faker()

def seed_records(n):
    for _ in range(n):
        Record.objects.create(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            phone = fake.phone_number(),
            address = fake.street_address(),
            city = fake.city(),
            state = fake.state(),
            zipcode = fake.zipcode()
        )
    print(f"✅ Successfully seeded {n} fake records.")

if __name__ == "__main__":
    seed_records()