import sqlite3
from sqlite3 import Error

def create_connection(db):
    """Create a connection to knitrepoDB
        Args:
            param1: db = database file name
            Returns:
                Connection object or None
    """
    
    try:
        conn = sqlite3.connect(db)
        print("Connection to database successful")
        return conn
    except Error as e:
        print(e)
    
    return None

