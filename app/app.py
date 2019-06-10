from cassandra.cluster import Cluster

KEYSPACE = "test"
TABLE = "test"

def main():
    print("Main method")

def write_to_cassandra(vals, session):
    session.execute(f"insert into test.test (thekey, col1, col2) values ('{vals[0]}', '{vals[1]}', '{vals[2]}')")

def write_to_redis():
    print("write")

def read_from_cassandra(key, session):
    query = f"SELECT thekey, col1, col2 FROM test.test where thekey = '{key}'"
    rows = session.execute(query)
    r = rows.one()
    return [ r[0], r[1], r[2] ]

def read_from_redis():
    return "2"

main()
