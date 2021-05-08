#! /usr/bin/env python3

# Import influx to operate the database
from influxdb import InfluxDBClient

 # Initialization
client = InfluxDBClient('localhost', 8086, "user", "password", "globalmap")

json_body = [
    {
        "measurement": "countries",
        "tags": {
            "country_code": "GB"
        },
        "fields": {
            "value": 1
        }
    }
]

client.write_points(json_body)