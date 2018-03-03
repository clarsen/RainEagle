import RainEagle
import pprint
import time
from influxdb import InfluxDBClient

raineagle = RainEagle.Eagle(debug=0, 
                            addr="<your ip address>192.168.7.56", 
                            username="<your cloud id>", 
                            password="<your install code>")

client = InfluxDBClient(host="localhost", port=8086, database="ruuvi")

r = raineagle.get_usage_data()

json_body = [
    {
        "measurement": "energy_demand",
        "fields": {
            "value": float(r['demand']),
        }
    },
    {
        "measurement": "energy_price",
        "fields": {
            "value": float(r['price']),
        }
    },
    {
        "measurement": "energy_tiering",
        "fields": {
            "value": r['price_label'],
        }
    },
    {
        "measurement": "energy_spend_per_hour",
        "fields": {
            "value": float(r['demand']) * float(r['price']),
        }
    },
]

client.write_points(json_body)
