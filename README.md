this source-code is under Apache License 2.0 , read LISCENCE for more information

# Loading
## easy loading bar  !


loading is a way to do loading bar in python
- fully customizable
- easy to use


# how to use  :
```py
bar = Bar(100)
for i in range(1000):
    bar.update(message=i)
```

# example :
```py
loading = Bar(100,lenght=50,time=True)
for yeet in range(100):
    if loading.update(message=yeet,time=(100-yeet) ):
        time.sleep(1)
    else:
        break
```

## explication :

when you init the Bar , the first args is the number of iterations
so if you do Bar(1000)
you have to do 1000 iteration for finish the bar

for make the bar iterate , use .update


#
#
#
#
#
#

| class | utility | required argument | return |
| ------ | ------ | ---- | ------ |
| Bar | init the bar | total (number of iteration) |  Bar instance |


| fonction | utility | required argument | return |
| ------ | ------ | ---- | ------ |
| update | iterate the Bar | None | bool |

### kwarg :
for Bar
| kwarg | utility | default argument |
| ------ | ------ | ---- |
| lenght | the lenght of the bar  | 100 
| time | if you want to show a timer  | False
| progress | the progresse of the bar  | 0
| start_char | the first char of the bar | "["
| start\_middle\_char | the middle char  | "="
| white_char | the whitespace char  | " " (a whitespace)
| end\_middle\_char | usualy the cursor  | ">"
| end_char | the last char  | "]"

for update
| kwarg | utility | default argument |
| ------ | ------ | ---- |
| message | like the advancement of the loading (or like log)  | None 
| time | **you have to active time setting when init the bar** define the remaning time | 0 (give it in second)


## Installation
download bar.py and import it in your project (check that it is in the right path)
ex : 
```
from bar import Bar
```
# tested on :
- windows 10
- debian 9
- ubuntu 18.04

with python 3.9.2

# todo : 
- [x] fully customizable
- [x] crusade the bugs 
- [ ] more things ?
- [x] drinking a  coffee
- [x] eat
- [ ] sleep
