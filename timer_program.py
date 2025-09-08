'''5. Timer Program (`time`)
 
* Input: `countdown(5)`
* Output:
 
  ```
  5  
  4  
  3  
  2  
  1  
  Time’s up!
'''

import time

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)  
        seconds -= 1
    print("Time’s up!")


countdown(6)
