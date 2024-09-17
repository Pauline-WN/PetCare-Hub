PetCare Hub
===========

**PetCare Hub** is a simple command-line interface (CLI) application designed to help pet owners manage their pets' health and daily care. With this tool, users can track details about their pets, vet visits, and set daily care schedules.

Features
--------

-   **Manage Pet Information**: Keep track of important details like pet name, species, breed, age, and the pet's owner.
-   **Owner Management**: Store and update contact information for pet owners.
-   **Care Schedule Management**: Create and manage care schedules, including tasks like feeding, walking, and grooming.
-   **Vet Visit Tracking**: Schedule and log vet visits, along with the reason for each visit and the veterinarian's details.

Project Structure
-----------------

Here's an overview of the project structure:


Copy code

`PetCare-Hub/
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib/
    ├── models/
    │   ├── __init__.py
    │   ├── owner.py
    │   ├── pet.py
    │   ├── care_schedule.py
    │   └── vet_visit.py
    ├── cli.py
    ├── database.py
    └── helpers.py`

### Key Files

-   **lib/cli.py**: The main entry point for the PetCare Hub CLI. This file contains the menu and logic to manage the interaction with the user.
-   **lib/database.py**: Sets up the database connection and initializes the tables for storing information.
-   **lib/models/**: Contains the database models for pets, owners, care schedules, and vet visits.
-   **lib/helpers.py**: Helper functions to handle common tasks like displaying menus and validating user input.

How to Run the Project
----------------------

1.  **Install Dependencies**: Make sure you have [Pipenv](https://pipenv.pypa.io/en/latest/) installed on your machine.

   
    Copy code

    `pipenv install`

2.  **Activate the Virtual Environment**:

   
    Copy code

    `pipenv shell`

3.  **Run the CLI Application**:

  
    Copy code

    `python lib/cli.py`

Models Overview
---------------

1.  **Owner Model**:

    -   Represents a pet owner.
    -   Fields: `id`, `name`, `contact_info`.
2.  **Pet Model**:

    -   Represents a pet.
    -   Fields: `id`, `name`, `species`, `breed`, `age`, `owner_id` (links to `Owner`).
3.  **CareSchedule Model**:

    -   Represents a care task for a pet.
    -   Fields: `id`, `pet_id` (links to `Pet`), `task`, `frequency`, `due_date`.
4.  **VetVisit Model**:

    -   Represents a vet visit for a pet.
    -   Fields: `id`, `pet_id` (links to `Pet`), `visit_date`, `reason`, `vet_name`.

How to Use the CLI
------------------

After running the application, you will be presented with a menu that allows you to manage your pets, owners, care schedules, and vet visits.

### Example Menu:


Copy code

`PetCare Hub Menu:
1. Add Owner
2. Add Pet
3. Add Care Schedule
4. Add Vet Visit
0. Exit`

### Example Workflow:

-   To add a pet, first add an owner (option 1), then select "Add Pet" (option 2) and provide the details.
-   To log a vet visit, select "Add Vet Visit" (option 4), choose the pet, and enter the visit details.

Technologies Used
-----------------

-   **Python**: The language used for the CLI application.
-   **SQLAlchemy**: ORM (Object Relational Mapper) to interact with the SQLite database.
-   **Pipenv**: For managing dependencies and virtual environments.
-   **SQLite**: The database used for storing pet and care information.

Future Improvements
-------------------

-   Add reminders for upcoming care tasks.
-   Include more detailed reports on a pet's health history.
-   Add a user-friendly web interface.