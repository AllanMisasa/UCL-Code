import sqlite3

conn = sqlite3.connect('sensorData.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS dht
          ([temperature] FLOAT, [humidity] FLOAT)
          ''')
conn.commit()

c.execute("INSERT INTO dht VALUES (21.3, 50.5)")
conn.commit()
conn.close()

