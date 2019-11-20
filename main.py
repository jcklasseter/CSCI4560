# Author: John Lasseter
# CSCI 4560 Assignment 5
# Due: Nov. 25 2019

# Description: Manipulate the SUPPLIER-PART-SHIPMENT database programmatically

import mysql.connector

def setupTables():
    # Supplier table
    supplierStr = "CREATE TABLE SUPPLIER ( Sno varchar(32) NOT NULL PRIMARY KEY," \
                  "Sname varchar(32) NOT NULL," \
                  "Status int," \
                  "City varchar(32)," \
                  "CHECK (Status > 0));"



if __name__ == "__main__":
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="CSCI4560"
    )

    cursor = mydb.cursor(buffered=True)

    # First, setup the tables
    setupTables()
