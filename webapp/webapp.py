from flask import Flask
from flask import request

import mysql.connector
from socket import gethostbyname, gethostname

from datetime import datetime 

webapp = Flask(__name__)

# Create connection with DB
db_connection = mysql.connector.connect(
  host='mysql',
  port='3306',
  database='db',
  user='user',
  password='user'
)
print("Connected to DB")

cursor = db_connection.cursor(buffered=True)

@webapp.route("/")
def add_to_counter():
  # get information for access_log query
  now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  clientIP = request.remote_addr
  containerIP = gethostbyname(gethostname())
  
  # add +1 to global count
  cursor.execute("UPDATE global_count SET count = count + 1 WHERE ID = 'count'")
  
  # Add access_log entry 
  query = "INSERT INTO access_log (DateAndTime, UserIp, ContainerIP) VALUES (%s, INET_ATON(%s), INET_ATON(%s))"
  values = (now, clientIP, containerIP)
  
  cursor.execute(query, values)
  db_connection.commit()
    
  response = webapp.make_response("Internal IP: " + containerIP)
  response.set_cookie("internal_ip", containerIP, max_age=5*60)
  return response

@webapp.route("/showcount")
def show_counter():
  cursor.execute("SELECT count FROM db.global_count")
  count = cursor.fetchone()
  return webapp.make_response(f"Global counter: {count[0]}")
