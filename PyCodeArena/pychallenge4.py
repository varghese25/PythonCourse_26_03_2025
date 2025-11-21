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


OutPut: F

Explanation:
try block -> tries to run 1 / 0 -> this causes ZeroDivisionError
except block -> catches the error -> returns 'E'
finally block -> ALWAYS runs, even if a return happened earlier

If both except and finally have return statements, the return in finally overrides everything else

So, 
1. except wants to return 'E'
2. but finally returns 'F', so that becomes the final return value
"""