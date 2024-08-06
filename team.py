class Team:
    def __init__(self, nume, lista_angajati, proiecte_alocate):
        self.nume = nume
        self.lista_angajati = lista_angajati
        self.proiecte_alocate = proiecte_alocate

    def __str__(self):
        return (f"Nume: {self.nume}\n"
                f"Lista Angajati: {self.lista_angajati}\n"
                f"Proiecte Alocate: {self.proiecte_alocate}")