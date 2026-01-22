x = None
y ={x for x in [1,1,2,2]}
print(x,y)

"""Thats the subtle part. Let's make it super clear.
Step1: You start with: x = None
So before the comprehension, x is None

Step2: Then you do y = {x for x in [1, 1, 2, 2]}
step by step
| Step | Iterated value | x (inside comprehension) | Comment                    |
| ---- | -------------- | ------------------------ | -------------------------- |
| 1    | 1              | 1                        | x is updated from None → 1 |
| 2    | 1              | 1                        | x stays 1                  |
| 3    | 2              | 2                        | x is updated from 1 → 2    |
| 4    | 2              | 2                        | x stays 2                  |


The same variable x from outside is reused inside the comprehension.

So after the comprehension finishes, x keeps the last value, which is 2.

That’s why x = None doesn’t matter anymore—it gets overwritten by the comprehension.

✅ Key point: Set comprehensions don’t create a new scope, so they can overwrite variables from outside. """