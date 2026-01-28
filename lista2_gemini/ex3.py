class A:
    def acao(self):
        print("A")

class B(A):
    def acao(self):
        super().acao()
        print("B")

class C(A):
    def acao(self):
        super().acao()
        print("C")

class D(B, C):
    pass

d = D()
d.acao()
print(D.mro())
