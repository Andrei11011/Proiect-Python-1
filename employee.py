class Employee:
    def __init__(self, nume, id, rol, echipa, salariu):
        self.nume = nume
        self.id = id
        self.rol = rol
        self.echipa = echipa
        self.salariu = salariu

    def adauga_sarcina(self, sarcina):
        self.sarcini.append(sarcina)

    def adauga_proiect(self, proiect):
        self.proiect = proiect

    def __str__(self):
        return (f"Nume: {self.nume}\n"
                f"ID: {self.id}\n"
                f"Rol: {self.rol}\n"
                f"Echipa: {self.echipa}\n"
                f"Salariu: {self.salariu}")

