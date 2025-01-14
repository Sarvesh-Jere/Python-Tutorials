# Here we will learn how to connect to a MySQl databsse with python 

# Firstly lets understand what is ORM

# ORM is Object Relational Mapping in which you create an object and use it to manipulate or change your whole data. In this data is used as a python code. sql injection chances low. sql injection = hack your code

# Another option is raw sql query in which we use sql quereies to manipulate data. There are some chances of sql injection

from loguru import logger 
import mysql.connector

connection = mysql.connector.connect(host = "localhost",
                                     username = "user",
                                     password= "12345"
)

logger.info(f"{connection}")

cursor = connection.cursor()
# cursor is used to execute mysql queries as shown below

cursor.execute()
# put your sql queries in execute 
result = cursor.fetchall()
# used to fetch all the data 

connection.commit
# Commit is used last to commit the changes

logger.info(f"{result}")