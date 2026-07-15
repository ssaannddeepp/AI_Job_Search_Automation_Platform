"""
AI Job Search Automation Platform

Application Entry Point

Author: Sandeep Kumar Singh
Project: AI Job Search Automation Platform
"""

from config.app_settings import (
    APPLICATION_NAME,
    APPLICATION_VERSION,
    ENVIRONMENT
)


from app.core.logger import get_logger

logger = get_logger("app.main")


def main():
    """
    Start the AI Job Search Automation Platform.
    """

    print("==========================================")
    print(f" {APPLICATION_NAME}")
    print(f"Version: {APPLICATION_VERSION}")
    print(f"Environment: {ENVIRONMENT}")

    logger.info("Application started successfully.")
    
    print("==========================================")



if __name__ == "__main__":
    main()