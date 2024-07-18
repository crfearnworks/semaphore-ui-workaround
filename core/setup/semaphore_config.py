import os
import json
import secrets
from core import constants as const
from loguru import logger

logger.debug("Environment variables at the start of semaphore_config.py:")
for key, value in os.environ.items():
    logger.debug(f"{key}: {value}")

logger.info(f"POSTGRES_HOST from constants: {const.POSTGRES_HOST}")
logger.info(f"SEMAPHORE_DB_USER from constants: {const.SEMAPHORE_DB_USER}")

def main():
    logger.info("Creating Semaphore config file")
    logger.info("Reading environment variables")
    logger.info(f"POSTGRES_HOST: {const.POSTGRES_HOST}")
    config = {
        "bolt": {"host": const.SEMAPHORE_BOLT_HOST},
        "postgres": {
            "host": const.POSTGRES_HOST,
            "user": const.POSTGRES_USER,
            "pass": const.POSTGRES_PASSWORD,
            "name": const.POSTGRES_NAME,
            "options": {"sslmode": "disable"},
        },
        "dialect": const.SEMAPHORE_DB_DIALECT,
        "port": const.SEMAPHORE_WEB_PORT,
        "interface": "",
        "tmp_path": const.SEMAPHORE_PLAYBOOK_PATH,
        "cookie_hash": secrets.token_hex(16),
        "cookie_encryption": secrets.token_hex(16),
        "access_key_encryption": const.SEMAPHORE_ACCESS_KEY_ENCRYPTION,
        "email_sender": "",
        "email_host": "",
        "email_port": "",
        "web_host": "",
        "ldap_binddn": const.SEMAPHORE_LDAP_DN_BIND,
        "ldap_bindpassword": const.SEMAPHORE_LDAP_PASSWORD,
        "ldap_server": const.SEMAPHORE_LDAP_HOST,
        "ldap_searchdn": const.SEMAPHORE_LDAP_DN_SEARCH,
        "ldap_searchfilter": const.SEMAPHORE_LDAP_SEARCH_FILTER,
        "ldap_mappings": {"dn": "", "mail": "", "uid": "", "cn": ""},
        "telegram_chat": "",
        "telegram_token": "",
        "concurrency_mode": "",
        "max_parallel_tasks": 0,
        "email_alert": False,
        "telegram_alert": False,
        "slack_alert": False,
        "slack_url": "",
        "rocketchat_alert": False,
        "rocketchat_url": "",
        "ldap_enable": False,
        "ldap_needtls": False,
    }

    logger.info("Writing Semaphore config file")
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)

    logger.info("Semaphore config file created")
    logger.info("Copying config file to the Semaphore config file path")
    with open("config.json", "r") as f:
        data = f.read()
        f.close()
    with open(const.SEMAPHORE_CONFIG_FILE, "w") as f:
        f.write(data)
        f.close()

if __name__ == "__main__":
    main()
