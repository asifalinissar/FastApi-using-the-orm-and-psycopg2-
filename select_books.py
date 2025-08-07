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
        
        for row in rows:
            print(f"Id : {row[0]} , Title : {row[1]} , Author : {row[2]} , Available :{row[3]}")
            
    except Exception as e:
        print("some error occured in the select_books" ,e)
    
        
        
fetch_all_books()