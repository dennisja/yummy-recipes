# ugrade database to the latest version
#!venv/scripts/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
with open("yummy.log","w+") as logfile:
    print('Database Upgrade: Current database version: {} at {}'.format(str(v),datetime.utcnow()), file=logfile)