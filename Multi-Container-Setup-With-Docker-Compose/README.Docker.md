# Running Multi-Container Setup With Docker Compose for Mindfuel's Quote Delivery System application
This project delivers daily inspirational quotes to subscribed users via email. The system is containerized using Docker and orchestrated with Docker Compose, running as a multi-container application consisting of a Python-based quote delivery service and a PostgreSQL database.

## Prerequisites
- Docker
- Docker Hub account
- `.env` file with database and email credentials

## Steps followed
1. Created a compose.yml file defining two services:

    App: The Mindfuel Quote Delivery Python application

    Db: A PostgreSQL database with persistent storage via Docker volumes

2. Ran the Docker Compose command to build and start the full stack:

    docker compose up --build

![alt text](includes/Multi-Container.png)

![alt text](includes/compose%20run.png)

This Verifies:

- Both application and database containers start successfully

- The application connects automatically to the database container

- Quotes are fetched from the external API

- Emails are delivered successfully to subscribed users

- Database data persists across container restart

