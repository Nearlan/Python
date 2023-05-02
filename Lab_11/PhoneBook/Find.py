import psycopg2
from config import host, user, password, db_name

# Connect to database
conn = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name
    )
conn.autocommit = True

# Cursor
cursor = conn.cursor()


def show():
    
    sql = f'''
    
   CREATE procedure show(n VARCHAR(20))
    LANGUAGE plpgsql
AS
$$
BEGIN
    SELECT * FROM phone WHERE name LIKE n;
END;
$$;


    '''
    cursor.execute(sql)


show()