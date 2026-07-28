class A:
    def method_a(self):
        print("Method of class A")
        
class B:
    def method_b(self):
        print("Method of class B")
        
class C(A,B):
    def method_c(self):
        print("Method of Class C")
        

cobject = C()
cobject.method_a()
cobject.method_b()
cobject.method_c()