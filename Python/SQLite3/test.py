import sqlite3

conn = sqlite3.connect('sensorData.db')
c = conn.cursor()

temperature = 26.3
humidity = 50.5

c.execute('CREATE TABLE IF NOT EXISTS Dht (temp FLOAT, hum FLOAT)')
c.execute('INSERT INTO Dht VALUES(24.3, 45.5)')


c.execute('INSERT INTO Dht VALUES(?, ?)', (temperature, humidity))

conn.commit()

print(c.execute('SELECT * FROM Dht').fetchall())