from calcs import semestral, anual

choice = input('"SEMESTRAL"/"ANUAL": ').lower()

while (choice != 'semestral') and (choice != 'anual'):
    choice = input('"SEMESTRAL"/"ANUAL": ').lower()

#Semestral
if choice == 'semestral':
    grade1 = float(input("Nota do 1° Bimestre: "))
    grade2 = float(input("Nota do 2° Bimestre: "))
    semestral(grade1, grade2)

#Anual
elif choice == 'anual':
    grade1 = float(input("Nota do 1° Bimestre: "))
    grade2 = float(input("Nota do 2° Bimestre: "))
    grade3 = float(input("Nota do 3° Bimestre: "))
    grade4 = float(input("Nota do 4° Bimestre: "))
    anual(grade1, grade2, grade3, grade4)
