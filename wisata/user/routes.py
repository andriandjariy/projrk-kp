from flask import Flask, render_template, redirect, url_for, Blueprint, flash, request
from wisata import app
from wisata.models import Twisata, Tsejarah, Tprofil, Tadmin, Tadat_budaya

guser= Blueprint('guser',__name__)

@guser.route("/")
def home():
    return render_template("t_user/branda.html")

@guser.route("/wisata_alam")
def wisata_alam():
    form=Twisata.query.all()
    return render_template("t_user/wisata_alam.html", form=form)

@guser.route("/galery")
def galery():
    return render_template("t_user/galery.html")

@guser.route("/galery_wisata")
def galery_wisata():
    data=Twisata.query.all()
    return render_template("t_user/galery_wisata.html", data=data)

@guser.route("/galery_sejarah")
def galery_sejarah():
    data=Tsejarah.query.all()
    return render_template("t_user/galery_sejarah.html", data=data)

@guser.route("/galery_adatbudaya")
def galery_adatbudaya():
    data=Tadat_budaya.query.all()
    return render_template("t_user/galery_sejarah.html", data=data)

@guser.route("/sejarah")
def sejarah():
    form=Tsejarah.query.all()
    return render_template("t_user/sejarah.html", form=form)

@guser.route("/dataadat_budaya", methods=['GET', 'POST'], defaults={"page": 1})
@guser.route("/dataadat_budaya/<int:page>", methods=['GET', 'POST'])
def adat_budaya(page):
    page = page
    pages = 3
    DataAdatBudaya = Tadat_budaya.query.order_by(Tadat_budaya.id.desc()).paginate(page, pages, error_out=False)
    if request.method == 'POST' and 'tag' in request.form:
        tag = request.form["tag"]
        search ="%{}%".format(tag)
        DataAdatBudaya = Tadat_budaya.query.filter(Tadat_budaya.nama.like(search)).paginate(page, pages, error_out=False)
        return render_template("t_user/adatbudaya.html", DataAdatBudaya=DataAdatBudaya, tag=tag)
    return render_template("t_user/adatbudaya.html", DataAdatBudaya=DataAdatBudaya )

@guser.route("/contact")
def contac():
    return render_template("t_user/contact.html")


#route untuk ketegangan
@guser.route("/keterangan_wisata/<int:ed_id>/wisata", methods=['GET', 'POST'])
def keterangan_wisata(ed_id):
    dt=Twisata.query.get_or_404(ed_id)
    return render_template('t_user/keterangan.html',dt=dt)

@guser.route("/keterangansejarah/<int:ed_id>/sejarah", methods=['GET', 'POST'])
def keterangansejarah(ed_id):
    dt=Tsejarah.query.get_or_404(ed_id)
    return render_template('t_user/keterangan_sejarah.html',dt=dt)

@guser.route("/keteranganadatbudaya/<int:ed_id>/kebudayaan", methods=['GET', 'POST'])
def keteranganadatbudaya(ed_id):
    dt=Tadat_budaya.query.get_or_404(ed_id)
    return render_template('t_user/keteranga_adat_budaya.html',dt=dt)
#akhir route keterangan
