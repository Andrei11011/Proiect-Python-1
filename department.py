class Departament:
    def __init__(self, nume):
        self.nume = nume
        self.echipe = []
        self.proiect = []

    def adauga_echipe(self, echipa):
        self.echipe.append(echipa)

    def adauga_proiect(self, proiect):
        self.proiect.append(proiect)

    def __repr__(self):
        return (f"Nume: {self.nume}\n"
                f"Echipe: {self.echipe}\n"
                f"Proiect: {self.proiect}")