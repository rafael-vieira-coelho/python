width = 20
print('HackerRank'.ljust(width,'-'))
print('HackerRank'.center(width,'-'))
print('HackerRank'.rjust(width,'-'))

import math

def heart(c, width):
	print ((c*2).center(width//2)*2)
	for i in range(1,width//10+1):
		print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
           (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)
	for i in range(width//4,0,-1):
		print ((c*i*4).center(width))
	print ((c*2).center(width))

c = '♥'
thickness = 40
heart(c, thickness)

thickness = 5 #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
