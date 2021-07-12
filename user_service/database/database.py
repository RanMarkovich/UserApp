import os
import sqlite3


class Database:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    location = current_dir + '/user.db'

    def create_user(self, first_name, last_name, user_name, email, password):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()
        q = f"INSERT INTO `user`(`f_name`,`l_name`,`u_name`,`Email`, `password`) VALUES(?,?,?,?,?)", (
            first_name, last_name, user_name, email, password)
        cursor.execute(*q)
        connection.commit()

    def validate_user(self, email, password):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()
        cursor.execute(f"SELECT Email, password FROM `user` WHERE `Email` = '{email}' AND `password` = '{password}'")
        results = cursor.fetchall()
        return True if len(results) > 0 else False

    def is_email_exit(self, email):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()
        cursor.execute(f"SELECT Email FROM `user` WHERE `Email` = '{email}'")
        results = cursor.fetchall()
        return True if len(results) > 0 else False
