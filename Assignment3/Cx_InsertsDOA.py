"""Zoe Berling Cx_InsertsDAO Denver University DU ID 872608482
This py file has all the SQL calls on the tables created to save the customer free bottle requests."""

import mysql.connector
from my_SQL_root_data import passwd, database, host
import csv
import pandas as pd

class CxInsertsDAO():
    """create database connection. Enter info or import to variables"""
    def __init__(self):
        self.mydb = mysql.connector.connect(
            user='root',
            passwd=passwd,
            database=database,
            host=host)
        self.mycur = self.mydb.cursor()

    def close(self):
        self.mydb.commit()
        self.mydb.close()

    def insertfreeprod(self, a, b, c):
        """Insert csv data into free_prod_req table"""
        # perform query
        sql = "INSERT IGNORE INTO free_prod_request (request_id, prod_request, email) " \
              f"values ('{a}', '{b}', '{c}');"
        self.mycur.execute(sql)
        self.mydb.commit()

    def insertcustomer(self, a, b ,c, d, e):
        """Insert csv data into free_prod_req table"""
        # perform query
        request_id = a
        customer_email = b
        phone_number = c
        first_name = d
        last_name = e
        sql = "INSERT INTO customer_table (request_id, customer_email, phone_number, first_name, last_name) " \
              f"values ('{request_id}', '{customer_email}', '{phone_number}', '{first_name}', '{last_name}') " \
              f"ON DUPLICATE KEY UPDATE " \
              f"phone_number = '{phone_number}', " \
              f"first_name = '{first_name}', " \
              f"last_name = '{last_name}'"
        self.mycur.execute(sql)
        self.mydb.commit()

    def insertaddress(self, a, b, c, d, e):
        customer_email = a
        address = b
        city = c
        state = d
        zipcode = e
        sql = "INSERT INTO addresses (customer_email, address, city, state, zipcode) " \
              f"values ('{customer_email}','{address}', '{city}', '{state}', '{zipcode}') " \
              f"ON DUPLICATE KEY UPDATE " \
              f"address = '{address}', " \
              f"city = '{city}', " \
              f"state = '{state}', " \
              f"zipcode = '{zipcode}'"
        self.mycur.execute(sql)
        self.mydb.commit()


    def insertorder(self, a, b, c, d, e, f):
        request_id = a
        order_id = b
        prod_purch = c
        age_of_order = d
        experience = e
        review = f
        sql = "INSERT INTO order_table (request_id, order_id, prod_purch, age_of_order, duplicatebool, experience, review) " \
              f"values ('{request_id}', '{order_id}', '{prod_purch}', '{age_of_order}', '0' ,'{experience}', '{review}') " \
              f"ON DUPLICATE KEY UPDATE " \
              f"duplicatebool = 1"
        self.mycur.execute(sql)
        self.mydb.commit()


    def freeprod(self):
        sql = "SELECT * from free_prod_request"
        self.mycur.execute(sql)
        free_prod_request = []
        for row in self.mycur:
            id = row[0]
            prod_request = row[1]
            email= row[2]
            free_prod_request.append((id,prod_request,email))
        return free_prod_request

    def customer(self):
        sql= "SELECT * from customer_table"
        self.mycur.execute(sql)
        customer = []
        for row in self.mycur:
            id = row[0]
            email = row[1]
            phone= row[2]
            customer.append((id,email, phone))
        return customer

    def address(self):
        sql= "SELECT * from addresses"
        self.mycur.execute(sql)
        list1 = []
        for row in self.mycur:
            email = row[0]
            city = row[1]
            state= row[2]
            list1.append((email, city, state))
        return list1

    def order(self):
        sql = "SELECT * from order_table"
        self.mycur.execute(sql)
        list1 = []
        for row in self.mycur:
            id = row[0]
            order_id = row[1]
            prod_purch = row[2]
            list1.append((id, order_id, prod_purch))
        return list1


    def no_duplicates(self):
        sql = "SELECT o.request_id, order_id, prod_purch, a.customer_email, phone_number, first_name, last_name, address, city, state, zipcode " \
              "from order_table o " \
              "JOIN free_prod_request f " \
              "ON o.request_id = f.request_id " \
              "JOIN addresses a " \
              "ON a.customer_email = f.email " \
              "JOIN customer_table c " \
              "ON a.customer_email = c.customer_email " \
              "WHERE o.duplicatebool = 0 AND experience = 'LOVE IT';"
        self.mycur.execute(sql)
        list1 = []
        for row in self.mycur:
            list2 = []
            for i in row:
                list2.append((i))
            list1.append(list2)
        return list1
