# Face-Morphing-Project
Transforming face in source image to face in target image and generating video for the same
Producing intermediate images which can show a smooth transformation
from source to destination image.

## Prerequisite:
Cv2 is required for reading,showing and writing purpose of image whereas
os module is required for just joining the intermediate images for making a
video with cv2.VideoWriter(). Since os module is preinstalled in python no
need to install it newly.
## Variables And Their Description :
img is source image , img2 is destination image , img3 is used for storing
intermediate images .
xs is an array for storing x-coordinates of source image control points
xs[0] is top left corner ,xs[1] is top right corner ,xs[2] xs[3] xs[4] are 2-eyes
and chin respectively xs[5] , xs[6] are bottom corners.
Similarly xd is an array for storing x- coordinates of destination image
control points. ys and yd stores y-coordinates of control points .
Variables be and al in frame function are Beta and Alpha respectively
(Affine coordinates)
fr is used for changing the number of intermediate images . If fr=2 then
there is only one intermediate image and if fr=10 there are 9 intermediate
images going to be produced.
tl is a triangle list which is only used for the Delaunay triangulation part .
Suppose tl [0]=(0,1,2) then its meaning is triangle’0’ is formed from control
points 0,1 and 2 . Control points 0,1 are top left,top right corners control
point 2 is eye which is on the left side of the image.

## Functions And Their Description :
Area(x1, y1, x2, y2, x3, y3) returns area of a triangle where (x1,y1) (x2,y2)
(x3,y3) are vertices of the triangle
isInside(x1, y1, x2, y2, x3, y3, x, y) returns true if a given point (x,y) is
inside the triangle else false.
tri(x,y,i,j) it says to which triangular region a point (i,j) belongs to .
x and y are control points arrays of image.
b(x0,x1,x2,y0,y1,y2,i,j): beta calculation with (x0,y0) ,(x1,y1) ,(x2,y2) as
control points forming triangle and i,j as the point for which beta is being
calculated.
point(m,c0,c1,c2,a,b): for calculating corresponding point in src and dest
given alpha ,beta ...c0,c1,c2 gives corresponding control points forming
triangle. a,b are alpha and beta . If we want to calculate corresponding
point in source image then we call x=point(xs,c0,c1,c2,a,b) and
y=point(ys,c0,c1,c2,a,b) so (x,y) gives corresponding point in sourceImage.
frame(mx,my,k,n): produces the intermediate image ,k is which
intermediate image it is and n is the total number of intermediate images .
mx , my are arrays of control points of the intermediate image .
rect_contains(rect, point) checks if a point is within the image or not.
delaunay(x,y): used for automatic triangulation of image .
x,y are arrays of control points of image.
It returns a triangle list .Suppose triangleList[0]={0,0,214,204,499,0} then
vertices of triangle 0 are (0,0) (214,204) (499,0) .
tlst(tlist,x,y) is used to just label the points returned from above function .
(0,0) is the top left corner control point which we labelled it as 0 in
xs,ys,xd,yd. So if Delaunay function gives (0,0) (214,204) (499,0) as
vertices of a triangles then tlst gives {0,2,5} since (214,204) is left side eye
which is labelled as 2 in xs,xd,ys,yd and (499,0) is bottom left corner point
which is labelled as 5 .
t1() and frames1() have the same functionality as tri() and frame() just bit
different variables and these are only used for Delaunay triangulation part.

## Procedure Followed:
The method followed to produce the intermediate images is in this way:
1. For each point in an intermediate image a function is written to find
which of the triangular region it belongs to.
2. After finding which one of the 8 triangles it belongs to, affine
coordinates i.e (alpha ,beta ) are calculated using the 3 control points
that formed the triangle.
3. Since affine coordinates remain the same for corresponding point in
source and destination color interpolation is done to calculate the color
value of point in intermediate image.
4. So for each point of the intermediate image we get a color value to form
the complete image and the same method is followed for each of the
intermediate images .
5. Finally using all intermediate images a video is made using
cv2.VideoWriter().
6. After Completing this whole task , work has been done to capture
coordinates of control points using mouse left button click.
7. Delaunay Triangulation i.e automatic triangulation has been done at
end where a function returns a list of points forming a triangle.
