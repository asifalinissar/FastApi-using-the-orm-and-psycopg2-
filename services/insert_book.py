from db.db_connect import get_connect

def insert_book(title : str , author : str , available : bool):
    
    conn = get_connect()
    if not conn:
        print("there is come error occured in connecting the db")
        return
    try :
        cur = conn.cursor()
        insert_qurey = """
        select insert_books(%s,%s,%s)
        """
        cur.execute(insert_qurey ,(title,author,available))
        conn.commit()
        cur.close()
        conn.close()
        print("insert value sucessfully")
        return
    except Exception as e:
        print("some error occured ;" ,e)
    
insert_book('Deep Work', 'Cal Newport',True)
