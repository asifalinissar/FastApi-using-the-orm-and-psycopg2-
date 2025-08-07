# used for testing

from db.db_connect import get_connect

conn = get_connect()

if conn:
    conn.close()