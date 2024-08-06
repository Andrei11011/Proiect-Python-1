class Project:
    def __init__(self, nume, descriere, data_inceput, data_sfarsit, buget, sarcini):
        self.nume = nume
        self.descriere = descriere
        self.data_inceput = data_inceput
        self.data_sfarsit = data_sfarsit
        self.buget = buget
        self.sarcini = sarcini
        self.responsabil = None
        self.resource = None


    def __str__(self):
        return (f"Nume: {self.nume}\n"
                f"Descriere: {self.descriere}\n"
                f"Data de inceput: {self.data_inceput}\n"
                f"Data de sfarsit: {self.data_sfarsit}\n"
                f"Buget: {self.buget}\n"
                f"Sarcini: {self.sarcini}\n"
                )
