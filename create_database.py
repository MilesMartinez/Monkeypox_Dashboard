import psycopg2

def drop_table(conn, table):
    query = f'DROP TABLE IF EXISTS {table}'
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    print(f'dropped table {table}.')

def create_monkeypox_staging_table(conn):
    query = """
        create table if not EXISTS monkeypox.public.staging (
        row_id serial primary key,
        id varchar,
        status varchar,
        location varchar,
        city varchar,
        country varchar,
        age varchar,
        gender varchar,
        date_onset varchar,
        date_confirmation varchar,
        symptoms varchar,
        hospitalized varchar(1),
        date_hospitalization varchar,
        isolated varchar(3),
        date_isolation varchar,
        outcome varchar,
        contact_comment varchar,
        contact_id varchar,
        contact_location varchar,
        travel_history varchar(1),
        travel_history_entry varchar,
        travel_history_start varchar,
        travel_history_location varchar,
        travel_history_country varchar,
        genomics_metadata varchar,
        confirmation_method varchar,
        source1 varchar,
        source2 varchar,
        date_entry varchar,
        date_death varchar,
        date_last_modified varchar,
        source3 varchar,
        source4 varchar,
        country_iso3 varchar
        );
    """
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    print('created monkeypox staging table.')

def main():
    # connect to AWS RDS instance
    conn = psycopg2.connect(user="",
                            password="",
                            host="",
                            port="5432",
                            database="monkeypox")
    # build database                            
    drop_table(conn, 'staging')
    create_monkeypox_staging_table(conn)

if __name__ == '__main__':
    main()