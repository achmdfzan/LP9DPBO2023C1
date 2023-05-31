from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jumlah_lantai, foto, lokasi, jml_penghuni, jml_kamar):
        super().__init__("Rumah", foto, lokasi, jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.jumlah_lantai = jumlah_lantai

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_jumlah_lantai(self):
        return self.jumlah_lantai

    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Lantai" + str(self.jumlah_lantai) + "\nJumlah Kamar : " + str(self.jml_kamar) + "\n"