#! /usr/bin/env python3

# Import list of all countries
import pycountry

# Import random
import random

# Import InfluxDBClient to operate the Influx database
from influxdb import InfluxDBClient

# Sleep
import time

# Get random country
def getRandomCountryCode():
    n = random.randint(0,len(pycountry.countries))
    country_code = list(pycountry.countries)[n].alpha_2
    print("Random country: " + country_code)
    return country_code

def generateJSON():
    json_body = [
        {
            "measurement": "countries",
            "tags": {
                "country_code": getRandomCountryCode()
            },
            "fields": {
                "value": 1
            }
        }
    ]
    return json_body

def main():

    # Wait for DB
    time.sleep(10)

    # Initialize DB connection
    client = InfluxDBClient('influxdb', 8086, "user", "password", "db1")

    while True:
        client.write_points(generateJSON())
        time.sleep(5)

# Control execution of code
if __name__ == "__main__":
    main()