from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
try:
	auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
	cluster = Cluster(['127.0.0.1'], control_connection_timeout=10,  port=9042, auth_provider=auth_provider)
	session = cluster.connect()
	print("Connection Established !!")
except Exception as e:
    print(f"Connection Failed !! Error : {e}")