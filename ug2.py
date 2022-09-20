toko={
    
    #KETERANGAN TOKO
    'toko_NPWP':9999999999999999,
    'toko_nama':"Cahaya Abadi",
    'toko_alamat':
    {
        'alamat_jalan':"Insaja",
        'alamat_nomor':"01",
        'alamat_rt':"99",
        'alamat_rw':"99",
        'alamat_kampung':"Durian Runtuh",
        'alamat_kelurahan':"Los Santos",
        'alamat_kecamatan':"Konoha",
        'alamat_kabupaten':"Wakanda"
    
    },
    #KETERANGAN DAFTAR BUKU YANG TERSEDIA
    'daftar_buku':[
        {
            'buku_isbn':"978-979-107-882-5",
            "buku_judul":"Akuntansi Pengantar 1",
            "buku_stok":20,
            "buku_harga($)":10.5
            
        },
            {
            'buku_isbn':"978-602-8759-44-1",
            "buku_judul":"Struktur Data",
            "buku_stok":10,
            "buku_harga($)":20.8
            
        },
            {
            'buku_isbn':"978-602-8759-42-7",
            "buku_judul":"Algoritma dan Pemrograman",
            "buku_stok":18,
            "buku_harga($)":18.5
            
        },
            {
            'buku_isbn':"978-602-6232-33-5",
            "buku_judul":"Mudah Belajar Ruby",
            "buku_stok":28,
            "buku_harga($)":60.5
            
        }
    ]
    }

#KETERANGAN TOKO
def keterangan_toko():
    print("Toko",toko['toko_nama'])
    print("Jl.",toko["toko_alamat"]["alamat_jalan"],end=", ")
    print("No.",toko["toko_alamat"]["alamat_nomor"],end=", ")
    print("RT.",toko["toko_alamat"]["alamat_rt"],end=", ")
    print("RW.",toko["toko_alamat"]["alamat_rw"],end=", ")
    print("Kampung",toko["toko_alamat"]["alamat_kampung"],end=", ")
    print("Kel.",toko["toko_alamat"]["alamat_kelurahan"],end=", ")
    print("Kec.",toko["toko_alamat"]["alamat_kecamatan"],end=", ")
    print("Kab.",toko["toko_alamat"]["alamat_kabupaten"])
    print("NPWP :",toko["toko_NPWP"])
    print()
    print()
keterangan_toko()

#KETERANGAN DAFTAR BUKU YANG TERSEDIA
n=len(toko["daftar_buku"])
def daftar_buku(n):
    print("##########")
    print()
    print("DAFTAR BUKU")
    print()

    for i in range(n):
        print(f"{i+1}.")
        print("ISBN :",toko['daftar_buku'][i]['buku_isbn'])
        print("Judul :",toko["daftar_buku"][i]['buku_judul'])
        print("Stok :",toko["daftar_buku"][i]['buku_stok'])
        print("Harga ($) :",toko["daftar_buku"][i]['buku_harga($)'])
        
    print()
    print("##########")
    print()
daftar_buku(n)
    #PENGHAPUSAN DATA
input1=input(("Apakah anda ingin menghapus data buku ? (Ya/Tidak) : "))
input1.lower()
while not(input1=="ya" or input1=="tidak"):
    print()
    print("Mohon masukkan input dengan benar !")
    input1=input(("Apakah anda ingin menghapus data buku ? (Ya/Tidak) : "))
else:
    if input1=="ya":
        data_yang_mau_dihapus=int(input(f"Data ke berapa yang mau anda hapus ? (1-{len(toko['daftar_buku'])}) : "))
        toko["daftar_buku"].pop(data_yang_mau_dihapus-1)
        print()
    elif input1=="tidak":
        print()
n=len(toko["daftar_buku"])
daftar_buku(n)
    #PENGUBAHAN DATA
input2=input(("Apakah anda ingin mengubah data buku ? (Ya/Tidak) : "))
input2.lower()
while not(input2=="ya" or input2=="tidak"):
    print()
    print("Mohon masukkan input dengan benar !")
    input2=input("Apakah anda ingin mengubah data buku ? (Ya/Tidak) : ")
else:
    if input2=="ya":
        data_yang_mau_diubah=int(input(f"Data ke berapa yang mau anda ubah ? (1-{len(toko['daftar_buku'])}) : "))
        ubah_isbn=(input("Masukkan ISBN baru : ") )
        ubah_judul=(input("Masukkan Judul baru : ") )
        ubah_stok=int(input(("Masukkan Jumlah stok baru (Masukkan dengan bilangan bulat !) : "))) 
   
  
        ubah_harga=float((input("Masukkan harga baru (Masukkan dengan angka !): ")))
      
        toko["daftar_buku"][data_yang_mau_diubah-1].update({
            'buku_isbn':ubah_isbn,
            "buku_judul":ubah_judul,
            "buku_stok":(ubah_stok),
            "buku_harga($)":ubah_harga}
            )
        print()
        n=len(toko["daftar_buku"])
        daftar_buku(n)
    elif(input2=="tidak"):
        print()






