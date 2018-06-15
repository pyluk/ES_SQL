import requests
import json

class ES_SQL:

    def __init__(self, uri):
        self.uri = uri
        self.result = []

    def execute(self, statement):
        query = json.dumps({
            "query": statement
        })
        response = requests.get(self.uri, data=query, headers={'Content-type': 'application/json'})
        result = response.text.split("\n")
        #Get the headers
        headers = result[0].split('|')
        #Remove the white spaces of the headers
        headers = [f.strip() for f in iter(headers)]
        #Delete the header and the -- seperation line
        del result[0:2]
        result_l = []
        result_l.append(tuple(headers))

        for row in iter(result):
            tmp_row = row.split('|')
            tmp_row = [f.strip() for f in iter(tmp_row)]
            result_l.append(tuple(tmp_row))

        del result_l[-1]
        self.result = result_l


    def fetchone(self):
        if self.result != []:
            return self.result[1]
        else:
            return []

    def fetchall(self):
        if self.result != []:
            ret = self.result
            del ret[0]
            return self.result
        else:
            return []