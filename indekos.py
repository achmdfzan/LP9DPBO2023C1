from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, tipe_indekos, foto, lokasi):
        super().__init__("Indekos", foto, lokasi)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.tipe_indekos = tipe_indekos

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_tipe_indekos(self):
        return self.tipe_indekos

    def get_summary(self):
        return "Hunian Indekos."
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nPenghuni : " + str(self.nama_penghuni) + "\nTipe Indekos : " + str(self.tipe_indekos) + "\n"