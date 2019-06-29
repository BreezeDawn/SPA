import os
import sys

from flask_script import Manager
from flask_migrate import MigrateCommand

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), "..")))

from SPA_back.src.py import create_app

app = create_app("dev")

mgr = Manager(app)

mgr.add_command("mc", MigrateCommand)

if __name__ == '__main__':
    mgr.run()
