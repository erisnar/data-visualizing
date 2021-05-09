# Data Visualizing

In this project we visualize data from an InfluxDB in a Grafana dashboard.

To build and deploy the stack run:

```bash
make all
```

Go to ```http://localhost:3000``` to view example Grafana dashboard.

## Docker Compose

Docker Compose is used to manage three containers. The stack consists of:

- Python app
- InfluxDB
- Grafana

The Python application generates data which is stored in the InfluxDB. Grafana is used to visualize the data from InfluxDB.

## Python Application

The Python application generates a random country code every 5 second and inserts a JSON object in the InfluxDB. The goal is to simulate incoming traffic to a website.

![country_codes](images/country_codes.png)

## Cleanup

To destroy the stack run:

```bash
make destroy
```
