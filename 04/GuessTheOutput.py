# guess the output

class A:
    def fun(self):
        print("hi")

class B:
    def fun(self):
        print("hey")

class C(A, B):
    def fun1(self):
        print("hello")

x = C()
x.fun()

# output = hi
# A's fun() already registered, so it won't allow B's fun() => no overriding

