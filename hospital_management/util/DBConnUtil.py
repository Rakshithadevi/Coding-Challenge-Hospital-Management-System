# util/DBConnUtil.py

import mysql.connector
from util.DBPropertyUtil import getPropertyString

class DBConnUtil:
    @staticmethod
    def getConnection():
        props = getPropertyString('db.properties')
        if props is None:
            return None
        try:
            conn = mysql.connector.connect(
                host=props['host'],
                port=props['port'],
                database=props['database'],
                user=props['user'],
                password=props['password']
            )
            return conn
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            return None
