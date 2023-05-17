"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7t1bhp8u7g2efqb10-a.oregon-postgres.render.com",
        database="todo_x0nq",
        user="root",
        password="DTSmmWOkfjk03yXHPgZZndZ51A8HmqQK")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
