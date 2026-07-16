"""
Database Manager

Responsible for managing
the PostgreSQL database connection.
"""


from app.core.logger import get_logger


logger = get_logger("database.manager")



class DatabaseManager:
    def connect(self):
        logger.info("Connection to PostgreSQL...")


    def disconnect(self):
        logger.info("Disconnecting from PostgreSQL...")