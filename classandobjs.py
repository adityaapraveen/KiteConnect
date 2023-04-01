class rectangle:
    def __init__(self, l,b):
        self.l = l
        self.b = b
    def get_area(self):
        area = 2*(self.l + self.b)
        return area
    
r1 = rectangle(2,4)
area = r1.get_area()
print(area)
        