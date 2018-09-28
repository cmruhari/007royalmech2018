import random
count=0
def myyroll():
    	return random.randint(1,6)
while(count<=100):
    n=input("press r roll the diece:")
    if(n=='r'):
       	r=myroll()
       	count=count+r
       	print("u got",r)
        print("new position is",count)

        if(count==8):
        	count=37
        	print("you got the ladder")
        elif(count==11):
        	count=2
       		print("you got the snake")
       	elif(count==13):
       	 	count=34
       	 	print("you got the ladder")
       	elif(count==25):
       		count=4
       		print("you got the snake")
       	elif(count==38):
       		count=9
       		print("you got the snake")
       	elif(count==40):
       		count=68
       		print("you the ladder")
       	elif(count==52):
       		count=81
       		print("you got the ladder")
       	elif(count==65):
       		count=46
       		print("you got the snake")
       	elif(count==76):
       		count=97
       		print("you got the ladder")
       	elif(count==89):
        	count=70
        	print("you got the snake")
        elif(count==93):
        	count=64
        	print("you got the snake")
        elif(count==100):
        	print("you win")
        	break
        elif(count>100):
        	print("you cannot move")
        	count=count-r		

       