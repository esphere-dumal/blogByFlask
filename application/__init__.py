from flask import Flask
import os
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = 'not_A_h0rO_as_zebra_pu4'
app.config['UPLOAD_FOLDER'] = 'application/posts/'


def init_post_list():
    file_list = []
    for home, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for filename in files:
            file_list.append(filename)
    return file_list


from application import routes

