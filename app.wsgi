import os, sys

PROJECT_DIR = "/var/www/mcme"

activate_this = os.path.join(PROJECT_DIR, 'venv', 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from mcmeAPI import app as application