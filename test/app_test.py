from app.app import *

from cassandra.cluster import Cluster

import logging
log = logging.getLogger()
log.setLevel('INFO')

KEYSPACE = "test"
TABLE = "test"


def create_keyspace(session):
    session.execute(f"""
        CREATE KEYSPACE IF NOT EXISTS {KEYSPACE} 
        WITH replication = {{ 'class': 'SimpleStrategy', 'replication_factor': '2' }}
    """)

def drop_table(session):
    session.execute(f"DROP TABLE IF EXISTS {KEYSPACE}.{TABLE}")

def create_table(session):
    session.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE} (
            thekey text,
            col1 text,
            col2 text,
            PRIMARY KEY (thekey)
        )
    """)

def insert_into(vals, session):
    session.execute(f"insert into test.test (thekey, col1, col2) values ('{vals[0]}', '{vals[1]}', '{vals[2]}')")

def select_from(key, session):
    query = f"SELECT thekey, col1, col2 FROM test.test where thekey = '{key}'"
    rows = session.execute(query)
    r = rows.one()
    return [ r[0], r[1], r[2] ]

class TestApp(object):

    def setup(self):
        log.info("setup")
        self.res = "1"
        self.cluster = Cluster(['cassandra'])
        self.session = self.cluster.connect()
        create_keyspace(self.session)
        self.session.set_keyspace(KEYSPACE)
        drop_table(self.session)
        create_table(self.session)
        #insert_into(self.session)

    def teardown(self):
        log.info("teardown")
        self.cluster.shutdown()


    def test_read_from_cassandra(self):
        insert_into(["r1", "r11", "r12"], self.session)
        row = read_from_cassandra("r1", self.session)
        assert row == ["r1", "r11", "r12"]

    def test_write_to_cassandra(self):
        write_to_cassandra(["w1", "w11", "w12"], self.session)
        r = select_from("w1", self.session)
        assert r == ["w1", "w11", "w12"]

    def test_read_from_redis(self):
        assert read_from_redis() == "2"

