import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = lambda *parts: os.path.join(BASE_DIR, *parts)

os.environ['SECRET_KEY'] = 'testing'
os.environ['DATABASE_URL'] = f"sqlite:///{path('db.sqlite3')}"

from .settings import *
