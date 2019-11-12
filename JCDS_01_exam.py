def sep():
    print("--------------------------------------------------------------------------")
def cekPrima(x):
    prima = False
    listX = range(2,x)
    if x>1 :
        if x == 2:
            prima = True
        for i in listX:
            if x % i==0:
                prima = False
                break
            else:
                prima = True
    else:
        prima = False
    return prima
def cekKomposit(x):
    kom = False
    listX = range(2,x)
    if x>1 :
        if x == 2:
            kom = False
        for i in listX:
            if x % i==0:
                kom = True
                break
            else:
                kom = False
    else:
        kom = True
    return kom
def examNomor1():
# A = himpunan (set) bilangan genap antara 1 dan 20.
    setA = set(filter(lambda a: True if a%2==0 else False, list(range(1,20+1))))
    print("Himpunan A : ", setA)

# B = himpunan (set) bilangan ganjil antara 1 dan 20.
    setB = set(filter(lambda a: True if a%2!=0 else False, list(range(1,20+1))))
    print("Himpunan B: ",setB)

# C = himpunan (set) bilangan negatif lebih dari -10.
    setC = set(range(-9,0))
    print("Himpunan C : ",setC)

# D = himpunan (set) bilangan prima antara 1 dan 20.
    setD = set(filter(cekPrima, range(21)))
    print("Himpunan D : ",setD)

# E = himpunan (set) bilangan komposit antara 1 dan 20.
    setE = set(filter(cekKomposit, range(1,21)))
    print("Himpunan E : ",setE)
    sep()
# # soal
# a. A ∪ B ∪ C ∪ D ∪ E
    jawaban1a = setA | setB | setC | setD | setE
    print("A ∪ B ∪ C ∪ D ∪ E : ", jawaban1a)

# b. (A ∩ B) ∪ (D ∩ E)
    jawaban1b = (setA & setB) | (setD & setE)
    print("(A ∩ B) ∪ (D ∩ E) : ", jawaban1b)

# c. (A ∪ B) ∩ (D ∪ E)
    jawaban1c = (setA | setB) & (setD | setE)
    print("(A ∪ B) ∩ (D ∪ E) : ", jawaban1c)

# d. (A ∪ B) - (D ∪ E)
    jawaban1d = (setA | setB).difference(setD | setE)
    print("(A ∪ B) - (D ∪ E) : ",jawaban1d)

# e. (A ∪ B ∪ C) - (A ∩ E)
    jawaban1e = (setA | setB | setC).difference(setA & setE)
    print("(A ∪ B ∪ C) - (A ∩ E) : ", jawaban1e)

def main():
    examNomor1()
    examNomor2()

if __name__ == '__main__':
    main()
    