import json

with open('temperature_anomaly.json', encoding='utf-8') as data:
    anomalies = json.load(data)

for key, _ in anomalies.items():
    print(key)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    print(f'{int(year)} ---> {float(value):5.2f}')

print(anomalies['citation'])
