
## Flask Application with Nginx and PostgreSQL

This repository contains a Flask application, a PostgreSQL database, and Nginx configured to serve the application. The setup uses Docker Compose for container orchestration.

# Directory Structure  
~~~javascript  
project-root/
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Flask application Dockerfile
├── app/
│   ├── app.py               # Flask application code
│   └── requirements.txt     # Python dependencies
├── init-db/
│   └── init.sql             # Database initialization script
├── nginx.conf               # Nginx configuration
└── README.md                # This file

~~~  

# Prerequisites
- Install Docker: Docker Installation Guide
- Install Docker Compose: Docker Compose Installation Guide

# How to Use

 **Start the Application**

 To start the application with all services (Flask, PostgreSQL, and Nginx):

 ``` bash
 docker compose up --build -d
 ```
 This will:

- Build the Flask application image.
- Start the PostgreSQL database and initialize it with init.sql.
- Start Nginx as a reverse proxy for the Flask app.

 **Access the Application**
 - Flask Application: http://localhost:5000
 - Nginx (reverse proxy): http://localhost

 **Stop the Application**
 To stop all running containers without deleting them:

 ```
  docker compose stop
 ```

 **Restart the Application**

 ```
 docker-compose restart
 ```

 **Remove Containers**

 ```
 docker-compose down
 ```

 **Clean Up Resources**

 *Remove Volumes*:

 To remove volumes created by Docker Compose (e.g., postgres_data):

 ```
 docker-compose down -v
 ```

**Remove Images**

To remove all Docker images associated with the project:

```
docker rmi $(docker images -q <project_name>_flask)
```
Replace <project_name> with the name of your project (check with docker ps if unsure).

**Remove All Unused Resources**

To remove unused containers, networks, images, and volumes:

```
docker system prune -a --volumes
```

# Notes

**Database Initialization:**

- The init.sql script is executed only the first time the database container is started. If you make changes to init.sql, you need to remove the postgres_data volume to reinitialize the database:

```
docker-compose down -v
```

- Custom Nginx Configuration:

  The nginx.conf file is mapped to the Nginx container. Edit it to customize the reverse proxy behavior.

# Troubleshooting

**Check Logs**

- container:

```
docker logs <container_name>
```

**Rebuild Containers**

If you encounter issues with stale configurations or dependencies, rebuild the containers:

```
docker-compose up --build -d
```

# Useful Commands

**View Running Containers**

```
docker ps
```

**View Logs of a Container**

```
docker logs <container_name>
```

**Access a Container's Shell**

```
docker exec -it <container_name> /bin/sh
```

**List All Docker Images**
```
docker images
```

**List All Docker Volumes**

```
docker volume ls
```