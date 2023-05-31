class Hunian():
    def __init__(self, jenis, foto, lokasi, jml_penghuni = 1, jml_kamar = 1):
        self.jenis = jenis
        self.foto = foto
        self.lokasi = lokasi
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar

    def get_jenis(self):
        return self.jenis
    
    def get_foto(self):
        return self.foto
    
    def get_lokasi(self):
        return self.lokasi

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Lokasi : " + str(self.lokasi) + "\nHunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang."