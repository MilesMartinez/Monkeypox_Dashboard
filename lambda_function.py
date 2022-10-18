import requests
import pandas as pd
import psycopg2
import psycopg2.extras as extras

def execute_values(conn, df, table):
  
    tuples = [tuple(x) for x in df.to_numpy()]
  
    cols = ','.join(list(df.columns))

    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()

def lambda_handler(event, context):

    # pull data
    r = requests.get('https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.json')
    data = r.json()
    df = pd.DataFrame.from_dict(data)

    orig_cols = ['ID','Status','Location','City','Country','Age','Gender','Date_onset','Date_confirmation','Symptoms','Hospitalised (Y/N/NA)','Date_hospitalisation','Isolated (Y/N/NA)','Date_isolation','Outcome','Contact_comment','Contact_ID','Contact_location','Travel_history (Y/N/NA)','Travel_history_entry','Travel_history_start','Travel_history_location','Travel_history_country','Genomics_Metadata','Confirmation_method','Source','Source_II','Date_entry', 'Date_death', 'Date_last_modified','Source_III','Source_IV','Country_ISO3']
    new_cols = ['id','status','location','city','country','age','gender','date_onset','date_confirmation','symptoms','hospitalized','date_hospitalization','isolated','date_isolation','outcome','contact_comment','contact_id','contact_location','travel_history','travel_history_entry','travel_history_start','travel_history_location','travel_history_country','genomics_metadata','confirmation_method','source1','source2','date_entry', 'date_death', 'date_last_modified','source3','source4','country_iso3']
    name_mapper = {orig_cols[i]: new_cols[i] for i in range(len(orig_cols))}
    df = df.rename(columns=name_mapper)

    # connect to AWS RDS instance
    conn = psycopg2.connect(user="",
                            password="",
                            host="",
                            port="5432",
                            database="monkeypox")    
    # insert
    execute_values(conn, df, 'staging')

    conn.close()