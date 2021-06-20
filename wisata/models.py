from datetime import datetime
from wisata import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(admin_id):
    return Tadmin.query.get(int(admin_id))

# awal table admin
class Tadmin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Tadmin('{self.nama}', '{self.username}', '{self.password}')"
# akhir table admin

# awal table demografi
class Twisata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_wisata = db.Column(db.String(100), nullable=False)
    keterangan = db.Column(db.Text, nullable=False)
    lokasi = db.Column(db.String(250), nullable=False)
    gambar = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"Twisata('{self.nama_wisata}','{self.keterangan}','{self.lokasi}','{self.gambar}')"

# akhir table demografi

# awal table adat_budaya
class Tadat_budaya(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    keterangan = db.Column(db.Text, nullable=False)
    gambar = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Tadat_budaya('{self.nama}','{self.keterangan}','{self.gambar}')"
# akhir table adat_budaya

# awal table sejara
class Tsejarah(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    keterangan = db.Column(db.Text, nullable=False)
    gambar = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Tsejarah('{self.nama}','{self.keterangan}','{self.gambar}')"
# akhir table sejara

# awal table profil
class Tprofil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    keterangan = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Tprofil('{self.nama}','{self.keterangan}')"
# akhir table profil


# awal table galery
class Tgalery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    gambar = db.Column(db.String(20), nullable=False)
    keterangan = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Tprofil('{self.nama}','{self.gambar}','{self.keterangan}')"
# akhir table galery