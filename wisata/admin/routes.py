import os 
import secrets
from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from wisata import app, db, bcrypt
from wisata.admin.forms import admin_F, wisata_F, login, sejarah_F, adatbudaya_F, eadmin_F, galery_F, editadatbudaya_F, editsejarah_F, editwisata_F
from wisata.models import Twisata, Tsejarah, Tprofil, Tadmin, Tadat_budaya
from PIL import Image

gadmin= Blueprint('gadmin',__name__)


# route simpam
def simpan_gambar(fotoo):
    random_hex= secrets.token_hex(8)
    _, f_ext= os.path.splitext(fotoo.filename)
    foto_fn= random_hex + f_ext
    foto_path= os.path.join(app.root_path, 'wisata/static/css layout/images', foto_fn)

    ubah_size=(300,300)
    j=Image.open(fotoo)
    j.thumbnail(ubah_size)
    j.save(foto_path)
    return foto_fn
# akhir rote simpan


# awal route wisata
@gadmin.route("/isi_data_wisata", methods=['GET','POST'])
@login_required
def isi_data_wisata():
    form=wisata_F()
    if form.validate_on_submit():
        nama_gambar= simpan_gambar(form.foto.data)
        add = Twisata(nama_wisata=form.nama_wisata.data, keterangan=form.keterangan.data, lokasi=form.lokasi.data, gambar=nama_gambar)
        db.session.add(add)
        db.session.commit()
        flash(f'Data Berhasil Di Input', 'primary')
        return redirect(url_for('gadmin.isi_data_wisata'))
    return render_template("t_admin/wisata.html", form=form)

@gadmin.route("/admin_wisata")
def admin_wisata():
    form=Twisata.query.all()
    return render_template("t_admin/data_wisata.html", form=form)

@gadmin.route("/editwisata/<int:ed_id>/update", methods=['GET', 'POST'])
def update_wisata(ed_id):
    datawisata=Twisata.query.get_or_404(ed_id)
    form=editwisata_F()
    if form.validate_on_submit():
        if form.foto.data:
            nama_gambar= simpan_gambar(form.foto.data)
            datawisata.gambar = nama_gambar
        datawisata.nama_wisata=form.nama_wisata.data
        datawisata.keterangan=form.keterangan.data
        datawisata.lokasi=form.lokasi.data
        db.session.commit()
        flash('Data Berhasil Di ubah','warning')
        return redirect(url_for('gadmin.admin_wisata'))
    elif request.method=="GET":
        form.nama_wisata.data=datawisata.nama_wisata
        form.keterangan.data=datawisata.keterangan
        form.lokasi.data=datawisata.lokasi
    return render_template('t_admin/editwisata.html', form=form)

@gadmin.route("/hapus_wisata/<id>", methods=['GET', 'POST'])
def hapus_wisata(id):
    my_data = Twisata.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash('Data berhasisl dihapus', 'warning')
    return redirect(url_for('gadmin.admin_wisata'))
# akhir route wisata


# awal route sejara
@gadmin.route("/isi_sejarah", methods=['GET','POST'])
@login_required
def isi_sejarah():
    form=galery_F()
    if form.validate_on_submit():
        jjk= simpan_gambar(form.gambar.data)
        add = Tsejarah(nama=form.nama.data, keterangan=form.keterangan.data, gambar=jjk)
        db.session.add(add)
        db.session.commit()
        flash(f'Data Berhasil Di Input', 'primary')
        return redirect(url_for('gadmin.isi_sejarah'))
    return render_template("t_admin/sejarah.html", form=form)

@gadmin.route("/admin_sejarah")
def admin_sejarah():
    form=Tsejarah.query.all()
    return render_template("t_admin/data_sejarah.html", form=form)

@gadmin.route("/editsejarah/<int:ed_id>/update", methods=['GET', 'POST'])
def update_sejarah(ed_id):
    datasejarah=Tsejarah.query.get_or_404(ed_id)
    form=editsejarah_F()
    if form.validate_on_submit():
        if form.foto.data:
            nama_gambar= simpan_gambar(form.foto.data)
            datawisata.gambar = nama_gambar
        datasejarah.nama=form.nama.data
        datasejarah.keterangan=form.keterangan.data
        db.session.commit()
        flash('Data Berhasil Di ubah','warning')
        return redirect(url_for('gadmin.admin_sejarah'))
    elif request.method=="GET":
        form.nama.data=datasejarah.nama
        form.keterangan.data=datasejarah.keterangan
    return render_template('t_admin/editsejarah.html', form=form)

@gadmin.route("/hapus_sejarah/<id>", methods=['GET', 'POST'])
def hapus_sejarah(id):
    my_data = Tsejarah.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash('Data berhasisl dihapus', 'warning')
    return redirect(url_for('gadmin.admin_sejarah'))
# akhir route sejarah


# awal route adat budaya
@gadmin.route("/admin_adatbudaya")
def admin_adatbudaya():
    form=Tadat_budaya.query.all()
    return render_template("t_admin/data_budaya.html", form=form)

@gadmin.route("/hapus_adatbudaya/<id>", methods=['GET', 'POST'])
def hapus_adatbudaya(id):
    H_data = Tadat_budaya.query.get(id)
    db.session.delete(H_data)
    db.session.commit()
    flash('Data berhasisl dihapus', 'warning')
    return redirect(url_for('gadmin.admin_adatbudaya'))


@gadmin.route("/editadatbudaya/<int:ed_id>/update", methods=['GET', 'POST'])
def update_adatbudaya(ed_id):
    dataadatbudaya=Tadat_budaya.query.get_or_404(ed_id)
    form=editadatbudaya_F()
    if form.validate_on_submit():
        if form.foto.data:
            nama_gambar= simpan_gambar(form.foto.data)
            datawisata.gambar = nama_gambar
        dataadatbudaya.nama=form.nama.data
        dataadatbudaya.keterangan=form.keterangan.data
        db.session.commit()
        flash('Data Berhasil Di ubah','warning')
        return redirect(url_for('gadmin.admin_adatbudaya'))
    elif request.method=="GET":
        form.nama.data=dataadatbudaya.nama
        form.keterangan.data=dataadatbudaya.keterangan
    return render_template('t_admin/editadatbudaya.html', form=form)

@gadmin.route("/isi_adatbudaya", methods=['GET','POST'])
@login_required
def isi_adatbudaya():
    form=adatbudaya_F()
    if form.validate_on_submit():
        jjk= simpan_gambar(form.gambar.data)
        add = Tadat_budaya(nama=form.nama.data, keterangan=form.keterangan.data, gambar=jjk)
        db.session.add(add)
        db.session.commit()
        flash(f'Data Berhasil Di Input', 'primary')
        return redirect(url_for('gadmin.isi_adatbudaya'))
    return render_template("t_admin/adatbudaya.html", form=form)
# akhir route adat budaya


# awal rote galery
@gadmin.route("/isi_galery", methods=['GET','POST'])
@login_required
def isi_galery():
    form=sejarah_F()
    if form.validate_on_submit():
        jjk= simpan_gambar(form.gambar.data)
        add = Tsejarah(nama=form.nama.data, keterangan=form.keterangan.data, gambar=jjk)
        db.session.add(add)
        db.session.commit()
        flash(f'Data Berhasil Di Input', 'primary')
        return redirect(url_for('gadmin.isi_galery'))
    return render_template("t_admin/galery.html", form=form)
# akhir route galery


# awal route admin
@gadmin.route("/daftar_admin",  methods=['GET', 'POST'])
@login_required
def daftar_admin():
    form=admin_F()
    if form.validate_on_submit():
        pass_hash = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        add= Tadmin(nama=form.nama.data, username=form.username.data, password=pass_hash)
        db.session.add(add)
        db.session.commit()
        flash(f'Akun berhasil daftar', 'primary')
        return redirect(url_for('gadmin.daftar_admin'))
    return render_template("t_admin/admin.html",form=form)

@gadmin.route("/login_admin",  methods=['GET', 'POST'])
def login_admin():
    form=login()
    if request.method == 'POST':
        ceknik=Tadmin.query.filter_by(username=form.username.data).first()
        if ceknik and bcrypt.check_password_hash(ceknik.password, form.password.data):
            login_user(ceknik)
            flash('selamat Datang Kembali', 'warning')
            return redirect(url_for('gadmin.daftar_admin'))
        else:
            flash('login gagal, periksa username dan Password!', 'danger')
    return render_template("t_admin/login_admin.html", form=form)

@gadmin.route("/logout_admin")
def logout_admin():
    logout_user()
    return redirect(url_for('gadmin.login_admin'))


@gadmin.route("/admin", methods=['GET', 'POST'])
def admin():
    dataadmin=Tadmin.query.all()
    return render_template("t_admin/tampilan.html", data=dataadmin)

@gadmin.route("/edithakakses/<int:ed_id>/update", methods=['GET', 'POST'])
def update_admin(ed_id):
    dataadmin=Tadmin.query.get_or_404(ed_id)
    form=eadmin_F()
    if form.validate_on_submit():
        cekpass= Tadmin.query.filter_by(username=form.username.data).first()
        if cekpass and bcrypt.check_password_hash(cekpass.password, form.password.data):
            pass_hash= bcrypt.generate_password_hash(form.passwordbaru.data). decode('utf-8')
            dataadmin.username=form.usernamebaru.data
            dataadmin.password=pass_hash
            db.session.commit()
            flash('Hak Akses Berhasil di ubah','warning')
            return redirect(url_for('gadmin.admin'))
        else:
            flash('password yang dimasukan salah, silahkan coba kembali !!','danger')
            return redirect(url_for('gadmin.admin'))
       
    return render_template("t_admin/eadmin.html", data=dataadmin, form=form)
# akhir rote admin




    