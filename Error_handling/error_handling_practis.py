
def bolme():
    try:
        user = int(input("Lütfen sayı 1"))
        use1 = int(input("Lütfen sayı 2"))
        result = user/use1
        print(result)
    except ZeroDivisionError:
        print("Kim sıfıra bölünyor amk")
    except ValueError:
        print("İnt lazım bize amk")






def toplam(n1, n2):
            print(n1+n2)
def cıkarma(n1, n2):
            print(n1-n2)
def carpma(n1, n2):
            print(n1*n2)
def bolme(n1, n2):
    print(n1/n2)

def ıslemler(n1, n2, want):
    assert not ıslem == "+" or not ıslem == "-" or not ıslem == "*" or not ıslem == "/"
    print("Fuck off")
    if want == '+':
        toplam(n1, n2)
        
    elif want == '-':
        cıkarma(n1, n2)
        
    elif want == '*':
        carpma(n1, n2)
       
    elif want == '/':
        bolme(n1, n2)

ıslem = input("Lütfen ıslme")

n1 = int(input("Lütfen n1"))
n2 = int(input("Lütfen n2"))

ıslemler(n1, n2, ıslem)


 

