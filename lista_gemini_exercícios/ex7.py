class A:
    def falar(self):
        print("A")

class B(A):
    def falar(self):
        print("B")
        super().falar()

class C(A):
    def falar(self):
        print("C")
        super().falar()

class D(B, C):
    def falar(self):
        print("D")
        super().falar()

letra_d = D()
letra_d.falar()
print(D.mro())