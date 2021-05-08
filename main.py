#! /usr/bin/env python3

# Import list of all countries
import pycountry

# Import random
import random

# Import InfluxDBClient to operate the Influx database
from influxdb import InfluxDBClient

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
    # Initialize DB connection
    client = InfluxDBClient('localhost', 8086, "user", "password", "globalmap2")

    client.write_points(generateJSON)

# Control execution of code
if __name__ == "__main__":
    main()