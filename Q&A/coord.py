import copy

class Coord:

     def __init__(self,x, y, z):
          self.x = x;
          self.y = y;
          self.z = z;
     def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'
     
coord = Coord(0,0,0)
c1 = coord    #copy.copy(coord) "" Her i dint change to anythin if change copy.copy(coord) then output will be (0,0,0) ""
c2 = copy.copy(coord)
c3 = copy.deepcopy(coord)

c1.x =1
c2.y =2
c3.z =3

print(coord)
             
""" OutPut is (1, 0, 0)"""