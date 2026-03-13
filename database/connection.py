import sqlite3
from config.config import DB_PATH

def conectar():
    return sqlite3.connect(DB_PATH)