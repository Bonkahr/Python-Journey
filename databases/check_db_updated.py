import pickle
import sqlite3

import pytz

db = sqlite3.connect("accounts_updated.sqlite",
                     detect_types=sqlite3.PARSE_DECLTYPES)
for row in db.execute("SELECT * FROM history"):
    print(row)
    utc_time = row[0]
    picked_zone = row[3]
    zone = pickle.loads(picked_zone)
    # zone = pytz.timezone("CET")
    local_time = pytz.utc.localize(utc_time).astimezone(zone)
    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo()))

db.close()
