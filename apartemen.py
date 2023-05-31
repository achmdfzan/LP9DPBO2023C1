from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, nama_apartemen, foto, lokasi, jml_penghuni, jml_kamar):
        super().__init__("Apartemen", foto, lokasi, jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.nama_apartemen = nama_apartemen

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_nama_apartemen(self):
        return self.nama_apartemen
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nNama Apartemen : " + str(self.nama_apartemen) + "\nJumlah Kamar : " + str(self.jml_kamar) + "\n"