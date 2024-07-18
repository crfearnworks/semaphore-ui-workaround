# ansible-admin

This is a Docker installation of Ansible Semaphore, allowing admins to use a web-based UI to manage Ansible scripts. 

## Background
The official Semaphore docker image, https://hub.docker.com/r/semaphoreui/semaphore, as of 7/18/24, has a number of issues:
1) The `cookie_hash` and `cookie_encryption` settings cannot be set
2) The environment variables for the admin account do not get passed into the container, causing the account to not be created.

## Workaround
I wrote this very slap-dash workaround to bring up a development system to test out Semaphore.
The .env file gets copied to the image when it's built so that environment variables can be read when the container is brought online.
**NOTE:** Due to the implementation, this should NOT be used in a production environment at this time.

## Installation
1) Clone this repo to your Docker server
2) Create your `.env` file from the `template.env` file.
3) Run the following in the root directory:
```
docker compose up
```
4) Once the semaphore container is running, attach a shell to the Docker container:
```
docker exec -it ansible-admin-semaphore-1 /bin/bash
```
5) Once in the container run the following to setup the admin account you defined in the `.env` file:
```
python create_admin_service.py
```
6) Exit the container.

## TO-DO
1) Change implementation to not store .env file