This is a program built to fully automate Georgia State University Drop Add. To most students coursicle is a very useful tool to see when the classes you want have seats that open up. The only issue with this is that coursicly is paid. I have issue with this on the fact that college students in america are already forced to pay obscene ammounts just to attend school so taxing them for basic stuff like know when the classes you want will become avaliable is unfair in my mind. That is why I have decided to design this program. Not only does it check when your classes are avaliable like in coursicle but it also adds them for you basically cutting out the middle man. 
For this you will need a couple things:
-The proper Python packages
-An accurate update to CRN.csv where you have the CRN number for the class, the url to the class on GoSolar, and the line number for the number of seats avaliable. What I mean by line number is that you want the line location of the ammount of open seats in the class from the raw HTML of the site. You can get this from downloading the HTML for the site looking through it until you see the exact location of it for the class you want. When adding it to CRN.csv you will want to subtract that by 1. For links with multiple class you will want to make sure that this is the line for the class you want and not the line for another class.
The only downside to this is that you will need to have this program running on your computer 24/7 inorder for it to exicute the drop add when a class becomes availiable. What I would recomend would be to run it on a VPS so that it will be able to run 24/7. I would recomend OVH just because it is really cheap but any VPS would work.
