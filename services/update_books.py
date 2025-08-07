from db.db_connect import get_connect


def update_books_by_id(book_id : int , available : bool):
    
    conn = get_connect()
    if not conn:
        print("falied to connect with the db")
        return
    
    try :
        cur = conn.cursor()
        
        update_query = """
        update books set available = %s where id = %s ;
        """
        cur.execute(update_query , (available, book_id))
        conn.commit()
        cur.close()
        conn.close
        print("value updated sucessfully")
        return
    except Exception as e:
        print("there is some error occred in updating the book" ,e)
        return
    
update_books_by_id(3,True)
        
