import sqlite3

def create_sqlite_database(filename):
    """Create a database connection to an SQLite Database"""
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_sqlite_database("db/company.sqlite3")