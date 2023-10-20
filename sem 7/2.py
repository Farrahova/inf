class vektor:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        print((self.x**2+self.y**2+self.z**2)**0.5)

    def __add__(self, second_vektor):
        return vektor(self.x+second_vektor.x,
                      self.y+second_vektor.y,
                      self.z+second_vektor.z)
    def __sub__(self, second_vektor):
        return vektor(self.x-second_vektor.x,
                      self.y-second_vektor.y,
                      self.z-second_vektor.z)
    def __matmul__(self, second_vektor):
        return vektor(self.x * second_vektor.x,
                      self.y * second_vektor.y,
                      self.z * second_vektor.z)


a= vektor(4,12,3)
b= vektor(2,2,2)
#если для вектора b координаты x=y=z=А, то матричное произведение - произведение на число А
#если не равны, то скалярное

a.__abs__()
b.__abs__()

c = a + b
d = a - b
e=a @ b


print(c.x, c.y, c.z)
print(d.x, d.y, d.z)
print(e.x, e.y, e.z)
