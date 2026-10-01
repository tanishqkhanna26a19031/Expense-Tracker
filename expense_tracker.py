import csv
import os


def add_exp():
    f=open("expense.csv","a",newline='')
    new=os.path.getsize("expense.csv")==0
    csv_w=csv.writer(f,delimiter=',')
    n=int(input("enter no. of enteries you want to add"))
    if new:
        csv_w.writerow(["amount","category","date"])
    for i in range(n):
        amnt = int(input("enter amount"))
        category = input("enter category")
        date = input("enter date")
        L = [amnt, category, date]
        csv_w.writerow(L)
    print("added successfully")
    f.close()


def view_exp():
    f = open("expense.csv", "r", newline="")
    r = csv.reader(f)

    for i in r:
        if r.line_num==0:
            continue
        else:
            print(i)
    f.close()


def total_exp():
    f = open("expense.csv", "r", newline="")
    r = csv.reader(f)
    total = 0
    ctotal = 0
    category = input("enter category")
    header = next(r, None)
    for i in r:
        total += int(i[0])
        if i[1] == category:
            ctotal += int(i[0])
    print(category, "\t total is :", ctotal)
    print("total expense is :", total)
    f.close()


def delete_exp():
    f = open("expense.csv", "r")
    r = csv.reader(f)
    rows = list(r)
    f.close()

    if not rows:
        print("No expenses found")
        return

    cat = input("enter category")
    date = input("enter date")
    k = []
    for i in rows[1:]:
        if i[1] == cat and i[2] == date:
            continue
        k.append(i)

    f = open("expense.csv", "w", newline="")
    csvw = csv.writer(f)
    csvw.writerow(["amount", "category", "date"])
    for i in k:
        csvw.writerow(i)
    f.close()




while True:
    print("WELCOME")
    print("make a choice you want")
    print("1.add an expense")
    print("2.view your expenses")
    print("3.total or category expenses")
    print("4.delete exxpense")
    print("5.exit")

    choice = int(input("enter choice no."))
    if choice == 1:
        add_exp()
    elif choice == 2:
        view_exp()
    elif choice == 3:
        total_exp()
    elif choice == 4:
        delete_exp()
    elif choice == 5:
        print("bye")
        break
    else:
        print("invalid")
        break
    ch=input("enter choice y/n")
    if ch.lower()=="n":
        break
        









