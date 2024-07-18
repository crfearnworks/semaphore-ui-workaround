# create_admin_service.py
import os
import subprocess
import time
import httpx
import core.constants as const

def wait_for_semaphore():
    url = "http://semaphore:3000/api/ping"
    max_retries = 30
    retry_interval = 10

    for _ in range(max_retries):
        try:
            with httpx.Client(timeout=10) as client:
                response = client.get(url)
                if response.status_code == 200:
                    print("Semaphore is ready.")
                    return True
        except httpx.RequestError:
            print("Semaphore not ready. Retrying...")
        time.sleep(retry_interval)

    print("Semaphore connection failed after maximum retries.")
    return False


def create_admin_user():

    cmd = [
        "semaphore",
        "user",
        "add",
        "--admin",
        "--login",
        const.SEMAPHORE_ADMIN,
        "--name",
        const.SEMAPHORE_ADMIN_NAME,
        "--email",
        const.SEMAPHORE_ADMIN_EMAIL,
        "--password",
        const.SEMAPHORE_ADMIN_PASSWORD,
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"Admin user '{const.SEMAPHORE_ADMIN}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating admin user: {e}")


if __name__ == "__main__":
    if wait_for_semaphore():
        create_admin_user()
    else:
        print("Failed to create admin user due to Semaphore connection issues.")
