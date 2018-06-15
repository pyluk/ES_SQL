# ES_SQL
Simple example to query Elasticsearch 6.3 with SQL SELECT statement

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Elasticsearch

Required version
```
Elasticsearch 6.3

```

### Python Prequisites

Required version and libraries
```
Python 3.6
Requests
json

```

## Example

Sample code

```
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
```


## Authors

* **pyluk** - *Initial work* - [pyluk](https://github.com/pyluk)
