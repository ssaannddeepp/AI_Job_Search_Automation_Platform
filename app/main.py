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
from app.exceptions.database_exceptions import DatabaseConnectionError
from app.database.database_manager import DatabaseManager

logger = get_logger("app.main")


def main():
    """
    Start the AI Job Search Automation Platform.
    """
    try:

        print("==========================================")
        print(f" {APPLICATION_NAME}")
        print(f"Version: {APPLICATION_VERSION}")
        print(f"Environment: {ENVIRONMENT}")

        logger.info("Application started successfully.")

        database_manager = DatabaseManager()
        database_manager.connect()
        database_manager.disconnect()
        
    
      
    except DatabaseConnectionError as error:

        logger.error(f"Database error: {error}")

    print("==========================================")



if __name__ == "__main__":
    main()