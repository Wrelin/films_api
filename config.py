import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + str(BASE_DIR / "data" / "db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'you-will-newer-know'
    HEROKU_DATABASE_URI = 'postgres://qcekicenzssxfh:26049d6f235252714fa838acc8dcf92dbc3748be8fd6efec845611dec34f4165@ec2-54-155-226-153.eu-west-1.compute.amazonaws.com:5432/ddpf7pc0vnr0tb'
