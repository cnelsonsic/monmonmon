from flask import Flask

app = Flask(__name__)
app.secret_key = '\x96\xa8\xca\x90;C\xfe\xdc\xf7\xf2\x1a\x9b%w\xb6\x1b\xca\n\x0cK2\xbc\xf4\x9c'

from model import *
setup_all()
create_all()

import monmonmon.views
