class Finance:
    def __init__(self, venituri, cheltuieli):
        self.venituri = venituri
        self.cheltuieli = cheltuieli

    def __str__(self):
        return (f"Venituri: {self.venituri}\n"
                f"Cheltuieli: {self.cheltuieli}")