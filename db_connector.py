import mysql.connector

def connect():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd=''
        # auth_plugin='mysql_native_password'
    )

    cursor = mydb.cursor()
    cursor.execute('create database if not exists inventory')
    cursor.execute("use inventory")
    cursor.execute(
        "create table if not exists stocks(id int auto_increment, name text, sale_price int,purchase_price int,stock_in_qty int, stock_out_qty int, category_id int, primary key(id))")
    cursor.execute(
        "create table if not exists categories(id int auto_increment, name text, primary key(id))")
    return cursor, mydb
