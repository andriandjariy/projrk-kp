

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from flask_ckeditor import CKEditorField
from wisata.models import Tadmin

class eadmin_F(FlaskForm):
    username= StringField('Username', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    usernamebaru= StringField('Username Baru', validators=[DataRequired()])
    passwordbaru= PasswordField('Password Baru', validators=[DataRequired(), Length(min=5)])
    submit=SubmitField('Ubah')

    def validate_username(self, username):
        cekadmin=Tadmin.query.filter_by(username=username.data).first()
        if not cekadmin:
            raise ValidationError('username yang anda masukan salah!')


class login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')  

class admin_F(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    konf_pass = PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Login') 

class wisata_F(FlaskForm):
    nama_wisata = StringField('Nama Wisata')
    keterangan = CKEditorField('Keterangan')
    lokasi = StringField('Lokasi')
    foto = FileField('Tambah Gambar', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('post') 

class editwisata_F(FlaskForm):
    nama_wisata = StringField('Nama Wisata')
    keterangan = CKEditorField('Keterangan')
    lokasi = StringField('Lokasi')
    foto = FileField('tambah gambar', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('post')


class sejarah_F(FlaskForm):
    nama = StringField('Naama Sejarah', validators=[DataRequired()])
    keterangan = CKEditorField('Keterangan', validators=[DataRequired()])
    gambar = FileField('Tambah Gambar', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('post') 

class editadatbudaya_F(FlaskForm):
    nama = StringField('Nama Adat & Budaya')
    keterangan = CKEditorField('Keterangan')
    gambar = FileField('Tambah Gambar', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('post')

class galery_F(FlaskForm):
    nama = StringField('Nama')
    keterangan = CKEditorField('Keterangan')
    gambar = FileField('Tambah Gambar', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('post') 

class editsejarah_F(FlaskForm):
    nama = StringField('Nama & Tempat Sejarah')
    keterangan = CKEditorField('Keterangan')
    gambar = FileField('Tambah Gambar', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('post') 

class adatbudaya_F(FlaskForm):
    nama = StringField('Nama Adat & Budaya', validators=[DataRequired()])
    keterangan = CKEditorField('Keterangan', validators=[DataRequired()])
    gambar = FileField('Tambah Gambar', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('post')

