from flask import Flask

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = 'not_A_h0rO_as_zebra_pu4'
app.config['UPLOAD_FOLDER'] = 'application/posts/'

from application import routes
