#Import library
from ES_SQL import ES_SQL

if __name__ == "__main__":

	#Url of the elasticsearch node
    uri_sql = 'http://172.30.1.19:9200/_xpack/sql?format=txt'
    crsr = ES_SQL(uri=uri_sql)
    #Send the SQL query
    try:
        crsr.execute("SELECT * FROM library WHERE release_date < '2000-01-01'")
        #Get all the data
        data = crsr.fetchall()
        #Iterate over the data
        for row in iter(data):
            print(row)
    except Exception as e:
        print("Error: %s" %str(e))
