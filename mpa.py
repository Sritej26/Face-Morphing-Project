
"""
Created on Tue Jan 21 14:08:28 2020

@author: Sritej. N
"""

import cv2
import numpy as np

img=cv2.imread('Bush.jpg')
img2=cv2.imread('Clinton.jpg')
# cv2.line(img, (0, 0), (100,100), (0,255,0), 1)
# cv2.imshow('Amanda', img)
# cv2.waitKey()
# cv2.destroyAllWindows()  


img3 = np.zeros((500,500,3),np.uint8)   #img3 is final image

#only one intermediate image for now 
      
xs=[0,500,214,303,269,0,500] #control points of source x-coordinate
ys=[0,0,204,199,322,500,500] #control points of source y-coordinate

xd=[0,500,175,276,232,0,500] #control points of dest x-coordinate
yd=[0,0,250,239,381,500,500] #control points of dest y-coordinate      

mx=[] #control points in intermediate image x-coordinate 
my=[] #control points in intermediate image y-coordiantes
for i in range(0,7):
    mx.append(int(0.5*xs[i]+0.5*xd[i]))
    my.append(int(0.5*ys[i]+0.5*yd[i]))  #calculating coordinates of control points of intermediate image

def area(x1, y1, x2, y2, x3, y3):  #returns area of triangle
    return abs(((x1 * (y2 - y3) + x2 * (y3 - y1)  
                + x3 * (y1 - y2))) / 2.0) 

def isInside(x1, y1, x2, y2, x3, y3, x, y): #returns true if given point is inside the triangle
  
    # Calculate area of triangle ABC 
    A = area (x1, y1, x2, y2, x3, y3) 
  
    # Calculate area of triangle PBC  
    A1 = area (x, y, x2, y2, x3, y3) 
      
    # Calculate area of triangle PAC  
    A2 = area (x1, y1, x, y, x3, y3) 
      
    # Calculate area of triangle PAB  
    A3 = area (x1, y1, x2, y2, x, y) 
      
    # Check if sum of A1, A2 and A3  
    # is same as A 
    if(A == A1 + A2 + A3): 
        return True
    else: 
        return False
    
# rows, cols = (500, 500) 
# arr = [[0 for i in range(cols)] for j in range(rows)] 

def t(x,y,i,j): #retrurns a number n if a point (i,j) is in triangle n where as x is x-coordinates control points list of a image and y is y-coordinates control points list of image
        if(isInside(x[0],y[0],x[1],y[1],x[2],y[2],i,j)):
            return 1
        elif(isInside(x[0],y[0],x[2],y[2],x[5],y[5],i,j)):  #triangle 2 is formed by (x0,y0) ,(x2,y2) ,(x5,y5)          
            return 2
        elif(isInside(x[1],y[1],x[2],y[2],x[3],y[3],i,j)):            
            return 3
        elif(isInside(x[2],y[2],x[4],y[4],x[5],y[5],i,j)):
            return 4
        elif(isInside(x[2],y[2],x[3],y[3],x[4],y[4],i,j)):
            return 5
        elif(isInside(x[3],y[3],x[4],y[4],x[6],y[6],i,j)):
            return 6
        elif(isInside(x[1],y[1],x[3],y[3],x[6],y[6],i,j)):
            return 7
        elif(isInside(x[5],y[5],x[4],y[4],x[6],y[6],i,j)):
            return 8

def b(x0,x1,x2,y0,y1,y2,i,j): #beta calculation with (x0,y0) ,(x1,y1) ,(x2,y2) as control points forming triangle and i,j as the point for which beta is calculated
    return (((i-x0)*(y1-y0)-(j-y0)*(x1-x0))/((x2-x0)*(y1-y0)-(y2-y0)*(x1-x0)))
        
def point(m,c0,c1,c2,a,b):  #for calculating corresponding point in src and dest given alpha ,beta ...c0,c1,c2 gives corresponding control points forming triangle
    p=m[c0]+a*(m[c1]-m[c0])+b*(m[c2]-m[c0])
    pp=int(p)
    return pp
    

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):  
        r=t(mx,my,i,j)
        if(r==1): #for triangle 1 control points are (x0,y0) ,(x1,y1) ,(x2,y2)
            c0=0
            c1=1
            c2=2
            be=b(mx[0],mx[1],mx[2],my[0],my[1],my[2],i,j) #beta calculation 
            al=((i-mx[0])-(mx[2]-mx[0])*be)/(mx[1]-mx[0]) #alpha calculation
        elif(r==2):#for tri 2 control points are (x0,y0) ,(x2,y2) ,(x5,y5)
            c0=0
            c1=2
            c2=5
            be=b(mx[0],mx[2],mx[5],my[0],my[2],my[5],i,j)
            al=((i-mx[0])-(mx[5]-mx[0])*be)/(mx[2]-mx[0])
        elif(r==3):
            c0=1
            c1=2
            c2=3
            be=b(mx[1],mx[2],mx[3],my[1],my[2],my[3],i,j)
            al=((i-mx[1])-(mx[3]-mx[1])*be)/(mx[2]-mx[1])
        elif(r==4):
            c0=2
            c1=5
            c2=4
            be=b(mx[2],mx[5],mx[4],my[2],my[5],my[4],i,j)
            al=((i-mx[2])-(mx[4]-mx[2])*be)/(mx[5]-mx[2])
        elif(r==5):
            c0=2
            c1=3
            c2=4
            be=b(mx[2],mx[3],mx[4],my[2],my[3],my[4],i,j)
            al=((i-mx[2])-(mx[4]-mx[2])*be)/(mx[3]-mx[2])
        elif(r==6):
            c0=3
            c1=4
            c2=6
            be=b(mx[3],mx[4],mx[6],my[3],my[4],my[6],i,j)
            al=((i-mx[3])-(mx[6]-mx[3])*be)/(mx[4]-mx[3])
        elif(r==7):
            c0=1
            c1=3
            c2=6
            be=b(mx[1],mx[3],mx[6],my[1],my[3],my[6],i,j)
            al=((i-mx[1])-(mx[6]-mx[1])*be)/(mx[3]-mx[1])
        elif(r==8):
            c0=5
            c1=4
            c2=6
            be=b(mx[5],mx[4],mx[6],my[5],my[4],my[6],i,j)
            al=((i-mx[5])-(mx[6]-mx[5])*be)/(mx[4]-mx[5])
        pxs=point(xs,c0,c1,c2,al,be) #calculating corrsponding x-coordinate in src
        pys=point(ys,c0,c1,c2,al,be) #calculating corrsponding y-coordinate in src
        pxd=point(xd,c0,c1,c2,al,be) #x cord in dest 
        pyd=point(yd,c0,c1,c2,al,be) #y cord in dest
        img3[i][j]=0.5*img[pxs][pys]+0.5*img2[pxd][pyd] #color interpolating 
        

cv2.imshow('image', img3)
cv2.waitKey()
cv2.destroyAllWindows()  

# c0=2
# c1=3
# c2=4
# bet=b(mx[2],mx[3],mx[4],my[2],my[3],my[4],194,227)
# alp=((194-mx[2])-(mx[4]-mx[2])*bet)/(mx[3]-mx[2])  
# sx=point(xs,c0,c1,c2,alp,bet)
# sy=point(ys,c0,c1,c2,alp,bet)
# dx=point(xd,c0,c1,c2,alp,bet)
# dy=point(yd,c0,c1,c2,alp,bet)

                                