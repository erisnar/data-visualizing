# Data Visualizing

In this project we visualize data from an InfluxDB in a Grafana dashboard.

To build and deploy the stack run:

```bash
make all
```

Go to ```http://localhost:3000``` to view example Grafana dashboard.

## InfluxDB

```SQL
> create database globalmap
> use globalmap
> INSERT countries,country_code=US value=1
> SELECT * FROM "countries"
name: countries
time                country_code value
----                ------------ -----
1620484211870645277 US           1
> SELECT * FROM "countries"^C
> INSERT countries,country_code=NO value=1
> SELECT * FROM "countries"
name: countries
time                country_code value
----                ------------ -----
1620484211870645277 US           1
1620484410599741637 NO           1
```

![country_codes](images/country_codes.png)

## Python Application

The Python application generates random country codes and inserts JSON objects as Data Tables in the InfluxDB. The goal is to simulate incoming traffic to a website.
