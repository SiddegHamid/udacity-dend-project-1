import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """Connect to Postgresql, drop any existing sparkifydb and create a new one.

    Keyword arguments:
    * None

    Output:
    * conn --   (psycopg2) connection to Postgres database (sparkifydb).
    * cur --    cursory to connected DB. Allows to execute SQL commands.
    """
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """Drop any existing tables from sparkifydb.

    Keyword arguments:
    * cur --    cursory to connected DB. Allows to execute SQL commands.
    * conn --   (psycopg2) connection to Postgres database (sparkifydb).

    Output:
    * Old sparkifydb database tables are dropped from Postgresql.
    """
    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print("Error: Issue dropping table.")
            print(e)

    print("Tables dropped successfully.")

def create_tables(cur, conn):
    """Create new tables (songplays, users, artists, songs, time)
        to sparkifydb.

    Keyword arguments:
    * cur --    cursory to connected DB. Allows to execute SQL commands.
    * conn --   (psycopg2) connection to Postgres database (sparkifydb).

    Output:
    * New sparkifydb database tables are created into Postgresql.
    """
    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print("Error: Issue creating table.")
            print(e)
    print("Tables created successfully.")

def main():
    """Connect to Postgresql, create new DB (sparkifydb),
        drop any existing tables, create new tables. Close DB connection.

    Keyword arguments:
    * cur --    cursory to connected DB. Allows to execute SQL commands.
    * conn --   (psycopg2) connection to Postgres database (sparkifydb).

    Output:
    * New sparkifydb is created, old tables are droppped,
        and new tables (songplays, users, artists, songs, time)
        are created..
    """
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
