class Sistem:
    def __init__(self):
        self.lista_proiecte = []
        self.lista_sarcini = []
        self.lista_angajati = []
        self.lista_echipe = []
        self.lista_departamente = []
        self.finante = None
        self.utilizator = None

    def verificare_permisiune(self, utilizator):
        if utilizator == "Angajat":
            return False
        return True

    def adauga_proiect(self, proiect):
        self.lista_proiecte.append(proiect)

    def stergere_proiect(self, nume):
        self.lista_proiecte = [proiect for proiect in self.lista_proiecte if proiect.nume != nume]

    def adauga_sarcina(self, sarcina):
        self.lista_sarcini.append(sarcina)

    def stergere_sarcina(self, titlu):
        self.lista_sarcini = [proiect for proiect in self.lista_sarcini if proiect.titlu != titlu]

    def adaugare_angajat(self, angajat):
        self.lista_angajati.append(angajat)

    def stergere_angajat(self, nume):
        self.lista_angajati = [angajat for angajat in self.lista_angajati if angajat.nume != nume]

    def adauga_echipa(self, angajati):
        self.lista_echipe.append(angajati)

    def stergere_echipa(self, nume):
        self.lista_echipe = [echipa for echipa in self.lista_echipe if echipa.nume != nume]

    def adauga_departament(self, departament):
        self.lista_departamente.append(departament)

    def cauta_anagajat_dupa_nume(self, nume):
        for i in self.lista_angajati:
            if i.nume == nume:
                return i
        return None

    def cauta_proiect_dupa_nume(self, nume):
        for i in self.lista_proiecte:
            if i.nume == nume:
                return i
        return None

    def cauta_sarcina_dupa_titlu(self, nume):
        for i in self.lista_sarcini:
            if i.titlu == nume:
                return i
        return None





