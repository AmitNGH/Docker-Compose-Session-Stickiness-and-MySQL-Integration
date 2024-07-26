# Basic Docker Compose and Session stickiness project

This project creates a basic python webapp, which raises counter and saves records of it to MySQL

- The environment is created with docker-compose
- The webapp is created with 3 replicas
- SQL Server to save count and records
- NGINX for loadbalancing and session stickiness

