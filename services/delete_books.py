from db.db_connect import get_connect

def delete_book_by_id(book_id : int):
    
    conn = get_connect()
    if not conn :
        print("connection falied with db")
        return
    
    try :
        
        cur = conn.cursor()
        
        delete_query = """
        delete from books where id = %s;
        """
        cur.execute(delete_query , (book_id,))
        conn.commit()
        cur.close()
        conn.close()
        
        print("book deleted sucessfully")
        
        return
    except Exception as e:
        print("there is some error occred is deleting the books" , e)
        return
delete_book_by_id(3)
