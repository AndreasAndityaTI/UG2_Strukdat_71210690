kk={
    'nomor_kk':67123456,
    'kepala_keluarga':'Risky Siswono',
    'domisili' : {
        'alamat': 'Jl. Wr. Su',
        'rt':'02',
        'rw':'08',
        'kode_pos': 78817,
        'desa_kelurahan':'Berbas Tengah',
        'Kecamatan':'Bontang Selatan',
        'kabupaten_kota':'Kota Bontang',
        'provinsi':'Kalimantan Timur'
    },
    'anggota_keluarga':[
        {
            'nama_lengkap':'Risky Siswono',
            'nik':642222,
            'jenis_kelamin':'Laki-laki',
            'tempat_lahir':'Bontang',
            'tanggal_lahir':'01-01-2000',
            'agama':'Islam',
            'pendidikan':'SLTP/Sederajat',
            'jenis_pekerjaan':'Belum/Tidak Bekerja',
            'golongan_darah':'Tidak Tahu'

        },
        {
            'nama_lengkap':'Paijem',
            'nik':642223,
            'jenis_kelamin':'Permpuan',
            'tempat_lahir':'Jombang',
            'tanggal_lahir':'01-01-1990',
            'agama':'Hindu',
            'pendidikan':'SLTP/Sederajat',
            'jenis_pekerjaan':'Karyawan',
            'golongan_darah':'B'
        }
    ]
}
# print(kk)
print(kk['nomor_kk'])
print(kk['domisili']['kode_pos'])
print(len(kk['anggota_keluarga']))
# print((kk['anggota_keluarga']['tanggal_lahir']))
for anggota in (kk['anggota_keluarga']):
    print(anggota['tanggal_lahir'])
for anggota in (kk['anggota_keluarga']):
    if (anggota['jenis_pekerjaan']=='Karyawan'):
        print(anggota['nama_lengkap'])
    
input_user="Risky Siswono"
kk['anggota_keluarga'][0]['nama_lengkap']=kk['anggota_keluarga'][0]['nama_lengkap']+ ", SE"
kk['anggota_keluarga'][0]['pendidikan']='Sarjana S1'

if kk['kepala_keluarga']==input_user:
    kk['kepala_keluarga']=kk['kepala_keluarga']+" SE"

anggota_baru={'nama_lengkap':'Bambang Spektakuler',
            'nik':642229,
            'jenis_kelamin':'Laki-laki',
            'tempat_lahir':'Pekanbaru',
            'tanggal_lahir':'01-01-2022',
            'agama':'Islam',
            'pendidikan':'Belum/ Tidak Sekolah',
            'jenis_pekerjaan':'Belum/Tidak Bekerja',
            'golongan_darah':'B'}
kk['anggota_keluarga'].append(anggota_baru)
print(kk)