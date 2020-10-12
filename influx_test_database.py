import influxdb
import json
from datetime import datetime


def setup_server_json(message,addr,now, dbu, dbp):
    
    json_setup = json.loads(message) 
    name_db = now
    dbuser = dbu
    dbuser_password = dbp
    print("JSON")
    print(json_setup)
    client = influxdb.InfluxDBClient('localhost',8086,dbuser,dbuser_password,name_db)
    client.switch_user(dbuser, dbuser_password)
    
    json_body = [
        {
            "measurement": json_setup['table_name'],
        }        
    ] 

    client.create_database(now)
    client.switch_database(now)
    client.write_points(json_body)
    
def loop_server_json(buffer, addr,now):

    client = influxdb.InfluxDBClient('localhost',8086,"test_01","haslo",now,retries=0)
    client.switch_database(now)
    client.write_points(buffer,'ms',protocol=u'json')
    print("Wyslalem...")    