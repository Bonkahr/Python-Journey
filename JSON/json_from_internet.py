import time
import json
from urllib import request


json_data_source = 'https://www.ncdc.noaa.gov/cag/global/time-series/globe' \
                   '/land_ocean/1/12/1880-2021/data.json '

connection_trials = 1

while True:
    try:
        with request.urlopen(json_data_source) as json_stream:
            data = json_stream.read().decode('utf-8')
    except:
        if connection_trials <= 3:
            print('Trying to reconnect to internet.....')
            time.sleep(4)
            connection_trials += 1
            continue
        else:
            print('Unable to connect to the internet!')
            break

    # print(data)
    anomalies = json.loads(data)

    structure_type = str(type(anomalies)).split(' ')[-1].lstrip(
        '\'').rstrip('\'>')
    no_of_items = len(anomalies)
    data_type = 'list'
    data_name = 'item'
    if structure_type == 'dict':
        data_type = 'dictionary'
        data_name = 'keys'
    elif no_of_items > 1:
        data_name = 'items'

    print(f'The data type is "{data_type}" with {no_of_items} {data_name}'
          f' available.')

    counter = 1
    for key, _ in anomalies.items():
        print(f'\t{counter}. {key}')
        counter += 1
    # print(anomalies['description'])

    for year, value in anomalies['data'].items():
        print(f'{int(year)} ---> {float(value):5.2f}')
    break


