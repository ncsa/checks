import urllib.request

import pika
import psycopg2
import pymongo


# ----------------------------------------------------------------------
# RABBITMQ
# ----------------------------------------------------------------------
def check_rabbitmq(rabbitmq_uri):
    params = pika.URLParameters(rabbitmq_uri)
    connection = pika.BlockingConnection(params)
    if connection.is_open:
        print('Connected to RabbitMQ.')
        connection.close()
        return True
    return False


# ----------------------------------------------------------------------
# MONGO
# ----------------------------------------------------------------------
def check_mongo(mongo_uri):
    client = pymongo.MongoClient(mongo_uri,
                                 connectTimeoutMS=1000,
                                 socketTimeoutMS=1000,
                                 serverSelectionTimeoutMS=1000)
    result = client.admin.command('ismaster')
    print("Connected to Mongo, master = ", result)
    return True


# ----------------------------------------------------------------------
# URL
# ----------------------------------------------------------------------
def check_url(url: str, text: str = None) -> bool:
    print(f"Verifying connectivity to URL: {url}")
    with urllib.request.urlopen(url) as res:
        print(f"  Response code: {res.code}")
        if not (200 <= res.code < 300):
            return False
        print("  Connected successfully.")
        if not text:
            return True
        print(f"  Searching in response for sentinel text: {text}")
        for line_no, line in enumerate(res.readlines(), start=1):
            if text in line.decode():
                print(f"    Sentinel text found on response line {line_no}:\n  {line}")
                return True
    return False


# ----------------------------------------------------------------------
# POSTGRESQL
# ----------------------------------------------------------------------
def check_postgresql(pg_uri=None, pg_table=None):
    connection = None
    if pg_uri:
        connection = psycopg2.connect(pg_uri)
    else:
        exit(4)
    if not connection:
        return False
    cursor = connection.cursor()
    print("Connected to database")
    if pg_table:
        cursor.execute('SELECT count(*) FROM "%s";' % pg_table)
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row:
            print("Found %d rows in table %s." % (row[0], pg_table))
            return True
        else:
            print("Did not find table %s." % pg_table)
    else:
        cursor.close()
        connection.close()
        return True
