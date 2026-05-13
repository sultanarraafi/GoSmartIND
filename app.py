from flask import Flask, render_template, request, redirect, url_for 
import urllib.parse

app = Flask(__name__)

data_pendaftar = []

@app.route('/')
def halaman_utama():
    return render_template('index.html')

@app.route('/proses_daftar', methods=['POST'])
def proses_daftar():
    nama_siswa = request.form.get('siswa')
    jenis_kelamin = request.form.get('jk')
    kelas = request.form.get('kls')
    nama_sekolah = request.form.get('sekolah')
    alamat_lengkap = request.form.get('alamat')
    mata_pelajaran = request.form.get('mapel')
    nama_orang_tua = request.form.get('ortu')
    nomor_hp_ortu = request.form.get('hp')

    data_baru ={
    'siswa' : nama_siswa,
    'jk' : jenis_kelamin,
    'kls' : kelas,
    'sekolah' : nama_sekolah,
    'alamat' : alamat_lengkap,
    'mapel' : mata_pelajaran,
    'ortu' : nama_orang_tua,
    'hp' : nomor_hp_ortu
    }

    data_pendaftar.append(data_baru)

    # ==========================================
    # LOGIKA BARU: MEMBUAT PESAN WHATSAPP
    # ==========================================
    
    # 2. GANTI DENGAN NOMOR WA ADMIN ANDA (Gunakan 62, bukan 0)
    nomor_admin = "62895353924188" 
    
    # 3. Merangkai teks pesan (menggunakan f-string dengan tanda kutip tiga agar bisa multi-baris)
    pesan_wa = f"""Halo Admin GoSmart IND! 
Saya ingin mendaftar les privat. Berikut adalah data diri saya:

*Data Siswa*
Nama: {nama_siswa}
Jenis Kelamin: {jenis_kelamin}
Kelas: {kelas}
Sekolah: {nama_sekolah}
Alamat: {alamat_lengkap}

*Program Akademik*
Mata Pelajaran: {mata_pelajaran}

*Data Orang Tua/Wali*
Nama Ortu/Wali: {nama_orang_tua}
No HP: {nomor_hp_ortu}

Mohon informasi selanjutnya mengenai pendaftaran ini. Terima kasih!"""

    # 4. Mengubah teks yang dirangkai tadi menjadi format URL yang sah
    teks_terenkode = urllib.parse.quote(pesan_wa)
    
    # 5. Membuat link tujuan akhir ke API WhatsApp
    link_whatsapp = f"https://wa.me/{nomor_admin}?text={teks_terenkode}"
    
    # 6. Alihkan user langsung ke WhatsApp, BUKAN ke halaman hasil.html lagi
    return redirect(link_whatsapp)

@app.route('/daftar_siswa')
def halaman_hasil():
    return render_template('hasil.html', data_siswa=data_pendaftar)

# if __name__ == '__main__':
#     app.run(debug=True)