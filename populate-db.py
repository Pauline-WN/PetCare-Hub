from lib.database import SessionLocal
from lib.models.owner import Owner
from lib.models.pet import Pet
from lib.models.care_schedule import CareSchedule
from lib.models.vet_visit import VetVisit
from datetime import date

# Create a new session
session = SessionLocal()

# Clear existing data (optional, uncomment to use)
# session.query(VetVisit).delete()
# session.query(CareSchedule).delete()
# session.query(Pet).delete()
# session.query(Owner).delete()
# session.commit()

# Function to get or create an owner
def get_or_create_owner(name, contact_info):
    owner = session.query(Owner).filter(Owner.name == name).first()
    if not owner:
        owner = Owner(name=name, contact_info=contact_info)
        session.add(owner)
        session.commit()  # Commit to get the ID assigned
    return owner

# Create sample owners
owner1 = get_or_create_owner("Pauline Nguru", "pauline.nguru@example.com")
owner2 = get_or_create_owner("Mercy Nzau", "mercy.nzau@example.com")

# Function to get or create a pet
def get_or_create_pet(name, species, breed, age, owner_id):
    pet = session.query(Pet).filter(Pet.name == name, Pet.owner_id == owner_id).first()
    if not pet:
        pet = Pet(name=name, species=species, breed=breed, age=age, owner_id=owner_id)
        session.add(pet)
        session.commit()  # Commit to get the ID assigned
    return pet

# Create sample pets
pet1 = get_or_create_pet("Buddy", "Dog", "Golden Retriever", 3, owner1.id)
pet2 = get_or_create_pet("Whiskers", "Cat", "Siamese", 2, owner2.id)

# Function to get or create a care schedule
def get_or_create_care_schedule(pet_id, task, frequency, due_date):
    schedule = session.query(CareSchedule).filter(
        CareSchedule.pet_id == pet_id,
        CareSchedule.task == task
    ).first()
    if not schedule:
        schedule = CareSchedule(pet_id=pet_id, task=task, frequency=frequency, due_date=due_date)
        session.add(schedule)
    return schedule

# Create care schedules for pets
get_or_create_care_schedule(pet1.id, "Feed", "Twice a day", date(2024, 9, 23))
get_or_create_care_schedule(pet2.id, "Groom", "Once a week", date(2024, 9, 25))

# Function to get or create a vet visit
def get_or_create_vet_visit(pet_id, visit_date, reason, vet_name):
    vet_visit = session.query(VetVisit).filter(
        VetVisit.pet_id == pet_id,
        VetVisit.visit_date == visit_date,
        VetVisit.reason == reason
    ).first()
    if not vet_visit:
        vet_visit = VetVisit(pet_id=pet_id, visit_date=visit_date, reason=reason, vet_name=vet_name)
        session.add(vet_visit)
    return vet_visit

# Create vet visits for pets
get_or_create_vet_visit(pet1.id, date(2024, 9, 20), "Annual check-up", "Dr. Smith")
get_or_create_vet_visit(pet2.id, date(2024, 9, 21), "Dental cleaning", "Dr. Lee")

# Commit changes
session.commit()

# Close the session
session.close()

print("Database populated with initial data!")
