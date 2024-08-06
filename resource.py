class Resource:
    def __init__(self, nume, tip, disponibilitate, cost):
        self.nume = nume
        self.tip = tip
        self.disponibilitate = disponibilitate
        self.cost = cost

    def __str__(self):
        return (f"Nume: {self.nume}\n"
                f"Tip: {self.tip}\n"
                f"Disponibilitate: {self.disponibilitate}\n"
                f"Cost: {self.cost}")