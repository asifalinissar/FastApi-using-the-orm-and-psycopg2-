from db.db_connect import get_connect

def get_book_by_author(author_name : str):
    
    conn = get_connect()
    if not conn:
        print("error occred in connection with db")
        return
    try :
        cur = conn.cursor()
        
        select_query = """
        select * from get_book_by_author(%s);
        """
        cur.execute(select_query,(author_name,))
        rows = cur.fetchall()
            
        cur.close()
        conn.close()
        return rows
    
    except Exception as e :
        print("some error occured in fetching the data :" , e)
        