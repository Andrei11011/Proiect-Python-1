from company import Company
from department import Departament
from project import Project
from task import Task
from team import Team
from resource import Resource
from employee import Employee
from budget import Budget
from finance import Finance
from sistem import Sistem
import time

def function_log(func):
    def wrapper(x):
        start_time = time.time()
        print(f"Apelare functie {func.__name__} cu argumentele {x}")
        func(x)
        end_time = time.time()
        result_time = end_time - start_time
        print(f"Functia {func.__name__} a avut un timp de executie {result_time} secunde")

    return wrapper


def function_verificare(func):
    def wrapper(x):
        if sistem.utilizator == "Angajat":
            print("Nu aveti permisiunea necesara pentru a accesa aceasta optiune")
            exit()
        else:
            func(x)
    return wrapper

def afiseaza_meniul():
    print("\nMeniu Sistem: ")
    print("1. Adaugati un proiect ")
    print("2. Elimiare proiect")
    print("3. Actualizare proiect")
    print("4. Adaugati o sarcina")
    print("5. Eliminati o sarcina")
    print("6. Actualizati o sarcina")
    print("7. Adaugare echipa")
    print("8. Eliminare echipa")
    print("9. Actualizare echipa")
    print("10. Adaugare angajat")
    print("11. Stergere angajat")
    print("12. Actualizare angajat")
    print("13. Adaugare resursa")
    print("14. Afisare proiect")
    print("15. Afisare finante")
    print("16. Generare raport")
    print("17. Creeare Departament")
    print("18. Exit")


@function_verificare
@function_log
def adauga_proiect(sistem):
    nume = input("Adauga numele proiectului: ")
    descriere = input("Adauga descrierea proiectului: ")
    data_inceput = input("Adauga data de inceput: ")
    data_sfarsit = input("Adauga data de sfarsit: ")
    buget = Budget(int(input("Adauga bugetul proiectului: ")))
    lista_sarcini = []
    while True:
        optiune = input("Doriti sa adaugati o sarcina? (da/nu): ").lower()
        if optiune == 'da':
            titlu = input("Adaugati tilul sarcinii: ")
            descriere = input("Adaugati descrierea sarcinii: ")
            termen_limita = input("Adaugati termenul limita: ")
            responsabil = input("Selectati un responsabil: ")
            ok = 0
            for i in sistem.lista_angajati:
                if i.nume == responsabil:
                    ok = 1
            if ok == 0:
                return print("Angajatul nu exista in companie !")
            status = input("Adaugati statusul sarcinii: ")
            task = Task(titlu, descriere, termen_limita, responsabil, status)
            sistem.adauga_sarcina(task)
            lista_sarcini.append(task.titlu)
        elif optiune == 'nu':
            break
        else:
            print("Opțiune invalidă! Introduceți 'da' sau 'nu'.")
    proiect = Project(nume, descriere, data_inceput, data_sfarsit, buget, lista_sarcini)
    sistem.adauga_proiect(proiect)
    print(f"Proiectul {nume}, a fost adaugat cu succes")


@function_verificare
@function_log
def stergere_proiect(sistem):
    nume = input("Adaugati numele proiectului: ")
    sistem.stergere_proiect(nume)
    print(f"Proiectul {nume} a fost sters cu succes")


@function_verificare
@function_log
def actualizare_proiect(sistem):
    nume = input("Adaugati numele proiectului care doriti sa fie actualizat: ")
    choice = input("Ce doriti sa actualizati (nume, descriere, data_inceput, data_sfarsit, buget, sarcini): ")
    for i in sistem.lista_proiecte:
        if i.nume == nume:
            valoare_noua = input(f"{choice}: ")
            if choice == "nume":
                i.nume = valoare_noua
            elif choice == "descriere":
                i.descriere = valoare_noua
            elif choice == "data_inceput":
                i.data_inceput = valoare_noua
            elif choice == "data_sfarsit":
                i.data_sfarsit = valoare_noua
            elif choice == "buget":
                i.buget = valoare_noua
            elif choice == "sarcini":
                i.sarcini = valoare_noua.split(";")
    for i in sistem.lista_proiecte:
        print(i)


@function_verificare
@function_log
def adaugare_sarcina(sistem):
    titlu = input("Adaugati tilul sarcinii: ")
    descriere = input("Adaugati descrierea sarcinii: ")
    termen_limita = input("Adaugati termenul limita: ")
    responsabil = input("Selectati un responsabil: ")
    ok = 0
    for i in sistem.lista_angajati:
        if i.nume == responsabil:
            ok = 1
    if ok == 0:
        return print("Angajatul nu exista in companie !")
    status = input("Adaugati statusul sarcinii: ")
    task = Task(titlu, descriere, termen_limita, responsabil, status)
    sistem.adauga_sarcina(task)
    print("Sarcina a fost adaugata cu succes")
    return task


@function_verificare
@function_log
def stergere_sarcina(sistem):
    nume = input("Adaugati numele sarcinii: ")
    sistem.stergere_sarcina(nume)
    print(f"Sarcina {nume} a fost stersa cu succes")


@function_verificare
@function_log
def actualiare_sarcina(sistem):
    nume = input("Adaugati titlul sarcinii care doriti sa fie actualizata: ")
    choice = input("Ce doriti sa actualizati (titlu, descriere, termen_limita, responsabil, status): ")
    for i in sistem.lista_sarcini:
        if i.titlu == nume:
            valoare_noua = input(f"{choice}: ")
            if choice == "titlu":
                i.titlu = valoare_noua
            elif choice == "descriere":
                i.descriere = valoare_noua
            elif choice == "termen limita":
                i.termen_limita = valoare_noua
            elif choice == "responsabil":
                i.responsabil = valoare_noua
            elif choice == "status":
                i.status = valoare_noua
    for i in sistem.lista_sarcini:
        print(i)


@function_verificare
@function_log
def adaugare_angajat(sistem):
    nume = input("Adaugati numele angajatului: ")
    id = input("Adaugati id-ul angajatului: ")
    rol = input("Adaugati rol-ul angajatului: ")
    echipa = input("Adaugati echipa din care face parte angajatul: ")
    salariu = int(input("Adaugati salariul angajatului: "))
    angajat = Employee(nume, id, rol, echipa, salariu)
    sistem.adaugare_angajat(angajat)
    print(f"Angajatul {nume} a fost adaugat cu succes")

    proiect = input("Adaugati numele proiectului unde o sa fie angajatul respectiv.")
    sarcini = input("Adaugati saricnile pe care o sa le aiba angajatul.")
    project = sistem.cauta_proiect_dupa_nume(proiect)
    task = sistem.cauta_sarcina_dupa_titlu(sarcini)

    if project:
        project.adauga_angajat(angajat)
        print(f"Angajatul a fost adaugat proiectului {project.nume}.")
    else:
        print(f"Proiectul {proiect} nu a fost gasit. Angajatul a fost adaugat in sistem dar nu a fost alocat unui proiect.")

    if task:
        task.adauga_angajat(angajat)
        print(f"Angajatul a fost adaugat sarcinii {task.titlu}.")
    else:
        print(f"Sarcina {sarcini} nu a fost gasit. Angajatul a fost adaugat in sistem dar nu a fost alocat unei sarcini.")


@function_verificare
@function_log
def stergere_angajat(sistem):
    nume = input("Adaugati numele angajatului: ")
    sistem.stergere_angajat(nume)
    print(f"Angajat {nume} a fost sters din sistem")


@function_verificare
@function_log
def actualizare_angajat(sistem):
    nume = input("Adaugati numele angajatului pe care doriti sa il modificati: ")
    choice = input("Ce doriti sa actualizati la acest angajat (nume, id, rol, echipa, salariu) ?")
    for i in sistem.lista_angajati:
        if i.nume == nume:
            valoare_noua = input(f"{choice}: ")
            if choice == "nume":
                i.nume = valoare_noua
            elif choice == "id":
                i.id = valoare_noua
            elif choice == "rol":
                i.rol = valoare_noua
            elif choice == "echipa":
                i.echipa = valoare_noua
            elif choice == "salariu":
                i.salariu = valoare_noua
    for i in sistem.lista_angajati:
        print(i)


@function_verificare
@function_log
def adaugare_echipa(sistem):
    nume = input("Adaugati numele echipei: ")
    lista_angajati = input("Adaugati angajatii care fac parte din aceasta echipa: ").split(",")
    proiecte_alocate = input("Adaugati proiectele alocate acestei echipe: ").split(",")
    for i in lista_angajati:
        try:
            if sistem.lista_angajati == []:
                return print(f"Angajatul {i} nu face parte din companie")
            for j in sistem.lista_angajati:
                if i not in j.nume:
                    return print(f"Angajatul {i} nu face parte din companie")
        except AttributeError:
            return print(f"Angajatul {i} nu face parte din companie")
    for i in proiecte_alocate:
        try:
            if sistem.lista_proiecte == []:
                return print(f"Proiectul {i} nu exista")
            for j in sistem.lista_proiecte:
                if i not in j.nume:
                    return print(f"Proiectul {i} nu exista")
        except:
            return print(f"Proiectul {i} nu exista")
    echipa = Team(nume, lista_angajati, proiecte_alocate)
    sistem.adauga_echipa(echipa)
    print(f"Echipa {nume} a fost adaugata cu succes")


@function_verificare
@function_log
def stergere_echipa(sistem):
    nume = input(f"Adaugati numele echipei care va fi stearsa: ")
    for i in sistem.lista_echipe:
        if i.nume == nume:
            sistem.stergere_echipa(i.nume)
        else:
            print(f"Echipa {nume}, nu exista")
    print(f"Echipa {nume} a fost stearsa cu succes")


@function_verificare
@function_log
def actualizare_echipa(sistem):
    nume = input("Introduceti numele echipei: ")
    choice = input("Ce doriti sa modificati la aceasta echipa: ")
    valoare_noua = input(f"{choice}: ")
    for i in sistem.lista_echipe:
        if i.nume == nume:
            if choice == "nume":
                i.nume = valoare_noua
            elif choice == "lista angajati":
                i.lista_angajati = valoare_noua
            elif choice == "proiecte alocate":
                i.proiecte_alocate = valoare_noua
    print(f"Echipa a fost actualizata cu succes")


@function_verificare
@function_log
def adauga_resursa(sistem):
    nume = input("Adaugati numele resursei: ")
    tip = input("Adaugati tip-ul resursei: ")
    disponibilitate = input("Adaugati disponibilitatea resursei: ")
    cost = int(input("Adaugati costul resursei: "))
    resursa = Resource(nume, tip, disponibilitate, cost)
    choice = int(input("Unde doriti sa aduagati aceasta sarcina (1. Proiect / 2. Sarcini)"))
    if choice == 1:
        proiect_nume = input("Alegeti numele proiectului: ")
        proiect = sistem.cauta_proiect_dupa_nume(proiect_nume)
        if proiect:
            proiect.adauga_resursa(resursa)
            print("Resursa a fost adaugata cu succes !")
        else:
            print("Proiectul nu a fost gasit!")
    elif choice == 2:
        task_titlu = input("Alegeti titlul sarcinii.")
        task = sistem.cauta_sarcina_dupa_titlu(task_titlu)
        if task:
            task.adauga_resursa(resursa)
            print("Resursa a fost adaugata cu succes!")
        else:
            print("Task-ul nu a fost gasit")

    else:
        print("Nu ati ales o optiune corespunzatoare")


@function_log
def afisare_proiect(sistem):
    nume = input("Detaliile carui proiect doriti sa le vedeti: ")
    if sistem.lista_proiecte == []:
        return print(f"Nu exista nici un proiect cu numele {nume}")
    else:
        for i in sistem.lista_proiecte:
            if i.nume == nume:
                print(i)
            if nume not in i.nume:
                print(f"Nu exista nici un proiect cu numele {nume}")


@function_verificare
@function_log
def afisare_finante(sistem):
    venituri = int(input("Ce suma a incasat compania: "))
    cheltuieli = int(input("Ce suma a cheltuit compania "))
    finante = Finance(venituri, cheltuieli)
    sistem.finante = finante


@function_verificare
@function_log
def generare_raport(sistem):
    choice = int(input("Ce raport doriti sa generati (1. Stare / 2. Financiar): "))
    if choice == 1:
        print("Departamentele active momentan sunt:")
        for i in sistem.lista_departamente:
            print(i)
        print("Proiectele active momentan sunt:")
        for i in sistem.lista_proiecte:
            print(i)
        print("Sarcinile active momentan sunt:")
        for i in sistem.lista_sarcini:
            print(i)
        print("Angajatii prezenti in companie sunt:")
        for i in sistem.lista_angajati:
            print(i)
        print("Echipele active momentan sunt:")
        for i in sistem.lista_echipe:
            print(i)
    elif choice == 2:
        print(f"Finantele sunt: {sistem.finante}")
    else:
        print("Nu ati ales o optiune valida!")

@function_verificare
@function_log
def creeare_departament(sistem):
    nume = input("Adaugati numele departamentului: ")
    echipa = input("Ce echipa doriti sa aduagati in departament: ")
    ok_echipa = 0
    for i in sistem.lista_echipe:
        if i.nume == echipa:
            ok_echipa = i
    proiect = input("De care proiect o sa se ocupe acest departament: ")
    ok_proiect = 0
    for i in sistem.lista_proiecte:
        if i.nume == proiect:
            ok_proiect = i
    if ok_echipa != 0 and ok_proiect != 0:
        department = Departament(nume)
        sistem.adauga_departament(department)
        department.adauga_echipe(echipa)
        department.adauga_proiect(proiect)
    elif ok_echipa == 0:
        print("Echipa respectiva nu exista! Departamentul nu a putut fi creat.")
    elif ok_proiect == 0:
        print("Proiectul respectiv nu exista! Departamentul nu a putut fi creat.")


sistem = Sistem()
pass

while True:
    sistem.utilizator = input("Buna ziua! Sunteti Angajat sau Manager: ")
    if sistem.utilizator == "Angajat" or sistem.utilizator == "Manager":
        afiseaza_meniul()
        optiune = input("Selectati o optiune: ")

        if optiune == "1":
            adauga_proiect(sistem)
        elif optiune == "2":
            stergere_proiect(sistem)
        elif optiune == "3":
            actualizare_proiect(sistem)
        elif optiune == "4":
            adaugare_sarcina(sistem)
        elif optiune == "5":
            stergere_sarcina(sistem)
        elif optiune == "6":
            actualiare_sarcina(sistem)
        elif optiune == "7":
            adaugare_echipa(sistem)
        elif optiune == "8":
            stergere_echipa(sistem)
        elif optiune == "9":
            actualizare_echipa(sistem)
        elif optiune == "10":
            adaugare_angajat(sistem)
        elif optiune == "11":
            stergere_angajat(sistem)
        elif optiune == "12":
            actualizare_angajat(sistem)
        elif optiune == "13":
            adauga_resursa(sistem)
        elif optiune == "14":
            afisare_proiect(sistem)
        elif optiune == "15":
            afisare_finante(sistem)
        elif optiune == "16":
            generare_raport(sistem)
        elif optiune == "17":
            creeare_departament(sistem)
        elif optiune == "18":
            exit()
    else:
        print("Nu ati introdus un utilizator valid!")









