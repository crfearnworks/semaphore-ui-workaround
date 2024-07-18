# ansible-admin

This is a Docker installation of Ansible Semaphore, allowing admins to use a web-based UI to manage Ansible scripts. 

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
6) Delete the `.env` file that's located in the container:
```
