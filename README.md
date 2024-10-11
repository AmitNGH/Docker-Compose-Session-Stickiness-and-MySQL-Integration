# Session-Sticky WebApp with Docker Compose, NGINX, and MySQL

This project demonstrates a scalable Python web application that uses Docker Compose to manage multiple services, including NGINX for load balancing and MySQL for data storage. The web application maintains session stickiness across multiple replicas to ensure user requests are consistently directed to the same instance.

Features
  - Python Web Application: A basic web app that increments a counter and saves records to a MySQL database.
  - Docker Compose: Orchestrates the entire application environment.
  - Session Stickiness: NGINX is configured to maintain session stickiness, routing requests from the same user to the same backend instance.
  - MySQL Database: Stores counters and records reliably.
