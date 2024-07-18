"""
file : core.constants
description: This module loads environment variables from a `.env` file and logs any missing variables. 
"""
import os
from loguru import logger
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(find_dotenv())

def get_env_variable(name, default=None):
    value = os.environ.get(name, default)
    if value is None:
        logger.warning(f"Environment variable {name} is not set!")
    return value


# POSTGRES CONFIG
POSTGRES_HOST = get_env_variable("POSTGRES_HOST")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_NAME = os.environ.get("POSTGRES_NAME")
POSTGRES_DB = os.environ.get("POSTGRES_DB")


# SEMAPHORE CONFIG
SEMAPHORE_BOLT_HOST = os.environ.get("SEMAPHORE_BOLT_HOST")
SEMAPHORE_DB_USER = os.environ.get("SEMAPHORE_DB_USER")
SEMAPHORE_DB_PASS = os.environ.get("SEMAPHORE_DB_PASS")
SEMAPHORE_DB_HOST = os.environ.get("SEMAPHORE_DB_HOST")
SEMAPHORE_DB_PORT = os.environ.get("SEMAPHORE_DB_PORT")
SEMAPHORE_DB_DIALECT = os.environ.get("SEMAPHORE_DB_DIALECT")
SEMAPHORE_DB = os.environ.get("SEMAPHORE_DB")
SEMAPHORE_PLAYBOOK_PATH = os.environ.get("SEMAPHORE_PLAYBOOK_PATH")
SEMAPHORE_WEB_PORT = os.environ.get("SEMAPHORE_WEB_PORT")
SEMAPHORE_ADMIN_PASSWORD = os.environ.get("SEMAPHORE_ADMIN_PASSWORD")
SEMAPHORE_ADMIN_NAME = os.environ.get("SEMAPHORE_ADMIN_NAME")
SEMAPHORE_ADMIN_EMAIL = os.environ.get("SEMAPHORE_ADMIN_EMAIL")
SEMAPHORE_ADMIN = os.environ.get("SEMAPHORE_ADMIN")
SEMAPHORE_ACCESS_KEY_ENCRYPTION = os.environ.get("SEMAPHORE_ACCESS_KEY_ENCRYPTION")
SEMAPHORE_LDAP_ACTIVATED = os.environ.get("SEMAPHORE_LDAP_ACTIVATED")
SEMAPHORE_LDAP_HOST = os.environ.get("SEMAPHORE_LDAP_HOST")
SEMAPHORE_LDAP_PORT = os.environ.get("SEMAPHORE_LDAP_PORT")
SEMAPHORE_LDAP_NEEDTLS = os.environ.get("SEMAPHORE_LDAP_NEEDTLS")
SEMAPHORE_LDAP_DN_BIND = os.environ.get("SEMAPHORE_LDAP_DN_BIND")
SEMAPHORE_LDAP_PASSWORD = os.environ.get("SEMAPHORE_LDAP_PASSWORD")
SEMAPHORE_LDAP_DN_SEARCH = os.environ.get("SEMAPHORE_LDAP_DN_SEARCH")
SEMAPHORE_LDAP_SEARCH_FILTER = os.environ.get("SEMAPHORE_LDAP_SEARCH_FILTER")
TZ = os.environ.get("TZ")
SEMAPHORE_CONFIG_FILE = os.environ.get("SEMAPHORE_CONFIG_FILE")
