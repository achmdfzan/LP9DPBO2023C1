from rumah import Rumah

class Ruko(Rumah):
    def __init__(self, nama_pemilik, jumlah_lantai, foto, lokasi, jml_penghuni, jml_kamar, nama_toko):
        super().__init__(nama_pemilik, jumlah_lantai, foto, lokasi, jml_penghuni, jml_kamar)
        self.nama_toko = nama_toko
        self.jenis = "Rumah Toko"
    
    def get_nama_toko(self):
        return self.nama_toko
    
    def get_detail(self):
        return super().get_detail() + "Nama Toko : " + str(self.nama_toko) + "\n"