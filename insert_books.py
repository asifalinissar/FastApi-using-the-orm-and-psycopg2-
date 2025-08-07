from db.db_connect import get_connect

def add_books():
    
    conn = get_connect()
    if not conn:
        print("the connection with db failed")
        
    try :
        
        cur = conn.cursor()
        
        create_query = """
          INSERT INTO books (title, author, available)
        VALUES 
            ('The Alchemist', 'Paulo Coelho', TRUE),
            ('Atomic Habits', 'James Clear', TRUE),
            ('The Hobbit', 'J.R.R. Tolkien', FALSE);
        """
        cur.execute(create_query)
        conn.commit()
        cur.close()
        conn.close()
        print("values added sucessfully")
        return
    except Exception as e:
        print("some error occured" , e)
        
add_books()
