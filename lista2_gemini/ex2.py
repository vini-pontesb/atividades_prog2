class A:
    def acao(self):
        print("A")

class B(A):
    def acao(self):
        print("B")

class C(A):
    def acao(self):
        print("C")

class D(B,C):
    pass

dzinho = D()
dzinho.acao()
print(D.mro())
