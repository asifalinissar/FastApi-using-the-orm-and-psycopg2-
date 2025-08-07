from db.db_connect import get_connect

def fetch_all_books():
    
    conn = get_connect()
    
    if not conn:
        print("some error occured with the connection in the db")
        return
    try :
        cur = conn.cursor()
        
        select_query = """
        select * from books
        """
        cur.execute(select_query)
        rows = cur.fetchall()
        
        return rows
            
    except Exception as e:
        print("some error occured in the select_books" ,e)
    
