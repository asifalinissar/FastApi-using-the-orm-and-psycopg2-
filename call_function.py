from db.db_connect import get_connect

def show_available_books():
    
    conn = get_connect()
    
    if not conn:
        print("failed in connecting the db")
        return
    try :
        cur = conn.cursor()
        
        show_query = """
        select * from get_available_book();
        """
        
        cur.execute(show_query)
        rows = cur.fetchall()       
        for row in rows:
            print(f"id : {row[0]} title : {row[1]} , author : {row[2]} available : {row[3]} ")
        cur.close()
        conn.close()
        return
    except Exception as e:
        print ("some error occured" , e)
        
show_available_books()