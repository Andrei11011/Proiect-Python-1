class Company:
    def __init__(self, nume, departamente, angajati, resurse):
        self.nume = nume
        self.departamente = departamente
        self.angajati = angajati
        self.resurse = resurse

    def __str__(self):
        return f"Companie: {self.nume}, departamente: {self.departamente}, Numar angajati: {self.angajati}, Resurse: {self.resurse}"