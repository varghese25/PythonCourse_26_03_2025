def test():
    try:
      x = 1 / 0
    except:
       return 'E'

    finally:
     return 'F'
    
print(test())
     
""""
A. E
B. F
C. o
D. Error
"""