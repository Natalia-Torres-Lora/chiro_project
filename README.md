# chiro_project
# chiro_project
# Chiropractor Patient Management System

## Description
This is a full-stack patient management system designed for a chiropractor's office. It enables chiropractors to manage patients, appointments, treatments, and notes, with user authentication and role-based access.

## API Reference

| Endpoint                     | Method | Description                          | Params                     |
|-----------------------------|--------|--------------------------------------|----------------------------|
| /patients                   | GET    | List all patients                    | None                       |
| /patients/<id>              | GET    | Get a specific patient               | `id` (int)                 |
| /appointments               | POST   | Create a new appointment             | JSON body                  |
| /appointments/<id>          | PUT    | Update an appointment                | `id` (int), JSON body      |
| /treatments                 | GET    | List all treatments                  | None                       |
| /appointments/<id>/notes    | POST   | Add a note to an appointment         | `id` (int), JSON body      |

> Replace these with your actual Flask or Django endpoints.

## Retrospective

### How did the project's design evolve over time?
Initially, I started with raw SQL and a lightweight Flask app to practice database interactions. As I progressed, I transitioned to Django for the final implementation to take advantage of its robust admin interface, built-in ORM, and authentication system. The schema was refined to support many-to-many relationships, bridge tables, and better normalization.

### Did you choose to use an ORM or raw SQL? Why?
I chose to use an ORM because it provides safer, more maintainable, and more readable code. During early development in Flask, I used SQLAlchemy; later in Django, I leveraged the built-in ORM. However, I still wrote raw SQL for specific performance queries or complex joins where needed.

### What future improvements are in store, if any?
- Add role-based permissions (admin, chiropractor, receptionist)
- Integrate billing/invoicing and insurance claim tracking
- Enable calendar syncing (Google Calendar API)
- Add automated email reminders for upcoming appointments
- Enhance performance with caching and optimized indexing
