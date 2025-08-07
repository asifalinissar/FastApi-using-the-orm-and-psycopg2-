from db.db_connect import get_connect


def create_books_table():
    
    conn = get_connect()
    
    if not conn:
        print("connection falied")
        return
    try :
        cur = conn.cursor()
        
        create_query = """
        create table if not exists books(
            id serial primary key,
            title varchar(100),
            author varchar(100),
            available boolean default true
        )
        """
        cur.execute(create_query)
        conn.commit()
        
        cur.close()
        conn.close()
        print("table created sucessfully")
        return
    except Exception as e:
        print("table is not created" , e)
    

create_books_table()