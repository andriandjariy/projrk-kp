from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor

app=Flask('__name__', template_folder='wisata/templates', static_folder='wisata/static')
app.config['SECRET_KEY'] = "andrian"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pariwisata.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)

ckeditor = CKEditor(app)
app.config['CKEDITOR_HEIGHT']= 400

#registasi blueprints

from wisata.user.routes import guser
app.register_blueprint(guser)


from wisata.admin.routes import gadmin
app.register_blueprint(gadmin)