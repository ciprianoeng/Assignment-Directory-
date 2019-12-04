#Exam3
#Carlos Cipriano
#ID: 0719076


class Rectangle():
    def __init__(self):
        self.width = 12
        self.height = 15

    
    def print_dimensions(self):
        print("The dimensions of the rectangle are " + str(self.width) + "x" + str(self.height))


    def get_area(self):
        area =  self.width * self.height
        return area

   
    def get_perimeter(self):
        perimeter = (2*self.width) + (2*self.height)
        return perimeter

R = Rectangle()
R.print_dimensions()
print("The area of the rectangle is " + str(R.get_area()))
print("The perimeter of the rectangle is " + str(R.get_perimeter()))