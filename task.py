class Task:
    def __init__(self, titlu, descriere, termen_limita, responsabil, status):
        self.titlu = titlu
        self.descriere = descriere
        self.termen_limita = termen_limita
        self.responsabil = responsabil
        self.status = status
        self.resursa = None

    def adauga_angajat(self, angajat):
        self.responsabil = angajat

    def adauga_resursa(self, resursa):
        self.resource = resursa

    def __str__(self):
        return (f"Titlu: {self.titlu}\n"
                f"Descriere: {self.descriere}\n"
                f"Termen limita: {self.termen_limita}\n"
                f"Responsabil: {self.responsabil}\n"
                f"Status: {self.status}\n"
                f"Responsabil: {self.responsabil}\n"
                )