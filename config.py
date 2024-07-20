# config.py
import os

class Config:
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///example.db'  # Conexión SQLite para desarrollo local
    SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://root:root@127.0.0.1/sgb_database'
    #SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://root:root@127.0.0.1:3307/sgb_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'mysecretkey'  # Clave secreta para formularios
