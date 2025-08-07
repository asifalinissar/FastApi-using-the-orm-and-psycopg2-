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
        
        for row in rows:
            print(f"id : {row[0]} title : {row[1]} author : {row[2]} available : {row[3]}")
            
        cur.close()
        conn.close()
        return
    except Exception as e :
        print("some error occured in fetching the data :" , e)
        
get_book_by_author("james clear")