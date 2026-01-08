import sqlite3, sqlLib
from sqlite3 import Error

def select_Projects(conn):
    """Query: proj_id, title, author, date_created, file_types,
            tags, downloads, description, settings, type, speed, car_config
        Args:
            param1: conn = the Connection object
    """
    cur = conn.cursor()
    cur.execute('''SELECT proj_id, title, author, date_created, file_types, 
                tags, downloads, description, settings, type, speed, car_config 
                FROM Projects''')
    
    rows = cur.fetchall() #fetches all (or remaining) rows of query result, returns a list of tuples
    
    cur.close()
    return (rows)

def projResults(rows):
    print

def main():
    database = "knitrepoDB.db"
    
    conn = sqlLib.create_connection(database)
    
if __name__ == '__main__':
    main()