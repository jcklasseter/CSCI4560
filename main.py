# Author: John Lasseter
# CSCI 4560 Assignment 5
# Due: Nov. 25 2019

# Description: Manipulate the SUPPLIER-PART-SHIPMENT database programmatically

import mysql.connector


# Create the tables
def createTables(cursor):
    supplierStr = "CREATE TABLE SUPPLIER ( Sno varchar(32) NOT NULL PRIMARY KEY," \
                  "Sname varchar(32) NOT NULL," \
                  "Status int," \
                  "City varchar(32)," \
                  "CHECK (Status > 0));"

    partStr = "CREATE TABLE PART ( Pno varchar(32) NOT NULL PRIMARY KEY," \
              "Pname varchar(32) NOT NULL," \
              "Color varchar(32)," \
              "Weight int," \
              "City varchar(20)," \
              "UNIQUE (Pname, Color)," \
              "CHECK (Weight >= 1)," \
              "CHECK (Weight <= 100));"

    shipmentStr = "CREATE TABLE SHIPMENT ( Sno varchar(32) NOT NULL," \
                  "Pno varchar(32) NOT NULL," \
                  "Qty int DEFAULT 100," \
                  "Price  float," \
                  "PRIMARY KEY (Sno, Pno)," \
                  "FOREIGN KEY (Sno) REFERENCES SUPPLIER(Sno)," \
                  "FOREIGN KEY (Pno) REFERENCES PART(Pno)," \
                  "CHECK (Price > 0));"

    cursor.execute(supplierStr)
    cursor.execute(partStr)
    cursor.execute(shipmentStr)

# Populate the tables with the data
def populateTables(cursor):
    cursor.execute("INSERT INTO SUPPLIER VALUES('s1', 'Smith', 20, 'London')")
    cursor.execute("INSERT INTO SUPPLIER VALUES('s2', 'Jones', 10, 'Paris')")
    cursor.execute("INSERT INTO SUPPLIER VALUES('s3', 'Blake', 30, 'Paris')")
    cursor.execute("INSERT INTO SUPPLIER VALUES('s4', 'Clark', 20, 'London')")
    cursor.execute("INSERT INTO SUPPLIER VALUES('s5', 'Adams', 30, NULL)")

    # "INSERT INTO PART VALUES('p1', 'Nut', 'Red', 12, 'London')"
    # "INSERT INTO PART VALUES('p2', 'Bolt', 'Green', 17, 'Paris')"
    # "INSERT INTO PART VALUES('p3', 'Screw', NULL, 17, 'Rome')"
    # "INSERT INTO PART VALUES('p4', 'Screw', 'Red', 14, 'London')"
    # "INSERT INTO PART VALUES('p5', 'Cam', 'Blue', 12, 'Paris')"
    # "INSERT INTO PART VALUES('p6', 'Cog', 'Red', 19, 'London')"
    #
    # "INSERT INTO SHIPMENT VALUES('s1', 'p1', 300, 0.005)"
    # "INSERT INTO SHIPMENT VALUES('s1', 'p2', 200, 0.009)"
    # "INSERT INTO SHIPMENT VALUES('s1', 'p3', 400, 0.004)"
    # "INSERT INTO SHIPMENT VALUES('s1', 'p4', 200, 0.009)"
    # "INSERT INTO SHIPMENT VALUES('s1', 'p5', 100, 0.01)"
    # "INSERT INTO SHIPMENT VALUES('s1', 'p6', 100, 0.01)"
    # "INSERT INTO SHIPMENT VALUES('s2', 'p1', 300, 0.006)"
    # "INSERT INTO SHIPMENT VALUES('s2', 'p2', 400, 0.004)"
    # "INSERT INTO SHIPMENT VALUES('s3', 'p2', 200, 0.009)"
    # "INSERT INTO SHIPMENT VALUES('s3', 'p3', 200, NULL)"
    # "INSERT INTO SHIPMENT VALUES('s4', 'p2', 200, 0.006)"
    # "INSERT INTO SHIPMENT VALUES('s4', 'p3', NULL, NULL)"
    # "INSERT INTO SHIPMENT VALUES('s4', 'p4', 300, 0.006)"
    # "INSERT INTO SHIPMENT VALUES('s4', 'p5', 400, 0.003)"

# Run the main program
if __name__ == "__main__":
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="CSCI4560"
    )

    cursor = mydb.cursor(buffered=True)

    # First, setup the tables
    createTables(cursor)
    populateTables(cursor)




