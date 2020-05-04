import pymysql
from datetime import datetime

host = 'localhost'
username = 'root'
password = ''
db_name = 'gigagroup_bot'

db = pymysql.connect(host, username, password, db_name)

def add_user(message):
    cursor = db.cursor()

    sql = "INSERT INTO users (user_id, name,surname, created_at) \
                    VALUES ('%s', '%s', '%s', '%s')" % \
          (message.from_user.id, message.from_user.first_name, message.from_user.last_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        db.rollback()

def add_message(message):
    cursor = db.cursor()

    sql = "INSERT INTO messages (message, created_at, user_id) \
                        VALUES ('%s', '%s', '%s')" % \
          (message.text, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message.from_user.id)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        db.rollback()

def add_message_from_contact(message):
    cursor = db.cursor()

    contact_msg = message.contact.phone_number + ' ' + message.contact.first_name

    sql = "INSERT INTO messages (message, created_at, user_id) \
                        VALUES ('%s', '%s', '%s')" % \
          (contact_msg, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message.from_user.id)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        db.rollback()

