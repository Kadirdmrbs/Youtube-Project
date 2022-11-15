import psycopg2
import pandas as pd
from decouple import config

# Connection parameters, yours will be different
param_dic = {
    "host"      : config('HOST_NAME'),
    "database"  : config('DATABASE_NAME'),
    "user"      : config('USER_NAME'),
    "password"  : config('PASSWORD_DB'),
    "port"      : config('PORT_NUMBER')
}
def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn


def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df

def return_df():
    conn = connect(param_dic)
    column_names = ['Id','Title', 'Published_date', 'Views',
    'Likes','Comments','Duration']
    # Execute the "SELECT *" query
    df = postgresql_to_dataframe(conn, "select * from videos", column_names)

    return df
