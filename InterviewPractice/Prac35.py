list_=['A1', 'B2','C3']
print(list_[-1][-1][-1])


"""
Step 1 👉 list_[-1]

Pick the last item from the list:

['A1', 'B2', 'C3']
              ↑
            last = 'C3'


            So now you have:

'C3'

Step 2 👉 'C3'[-1]

Pick the last letter from 'C3':

'C3'
  ↑
 last = '3'

Now you have:

'3'
Step 3 👉 '3'[-1]

Pick the last letter from '3':

'3'
 ↑
still '3'
Final Answer:
3


Explanation:
This code outputs 3 because if first accessess the last element of the list ('C3'),
then the last character of that string ('3'), and finally the last character of that single-character string (stil '3').

"""