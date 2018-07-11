class parent():
    def __init__(self, last,h_color):
        self.last_name = last
        self.hair_color = h_color
class child(parent):
    def __init__(self, last,h_color,eye_color):
        parent.__init__(self, last,h_color)
        self.eye_color = eye_color
my = child("ghgh","dfgdfg","hjgjghj")
print(my.last_name)
print(my.hair_color)
print(my.eye_color)
    