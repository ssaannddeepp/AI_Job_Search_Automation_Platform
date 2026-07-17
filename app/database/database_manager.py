"""
Database Manager

Responsible for managing
the PostgreSQL database connection.
"""

import psycopg2

from app.core.logger import get_logger
from config.database_settings import(
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD,
)

from app.exceptions.database_exceptions import DatabaseConnectionError



logger = get_logger("database.manager")



class DatabaseManager:

    def __init__(self):
        self.connection = None

    
    def connect(self):
        try:
            logger.info("Connecting to PostgreSQL...")

            self.connection = psycopg2.connect(
                host=DATABASE_HOST,
                port=DATABASE_PORT,
                database=DATABASE_NAME,
                user=DATABASE_USER,
                password=DATABASE_PASSWORD
            )
            logger.info("Successfully connected to PostgreSQL.")
        
        except Exception as error:
            raise DatabaseConnectionError(
                f"Unable to connect to PostgreSQL: {error}"
            )


    def disconnect(self):
        if self.connection:
            self.connection.close()
            logger.info("Disconnected from PostgreSQL.")
        