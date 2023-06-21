import sqlite3

conn = sqlite3.connect('sensorData.db')
c = conn.cursor()

c.execute('SELECT * FROM dht')