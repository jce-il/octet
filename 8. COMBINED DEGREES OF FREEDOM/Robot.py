### forward and invert kinematic functions
### code taken from the blog in "A Piece of the Pie Chart" project site
### http://www.anninaruest.com/pie/2014/07/inverse-kinematics-and-the-m100rak/


import vpython as vp


#unit vectors
ex = vp.vector(1,0,0)  
ey = vp.vector(0,1,0)
ez = vp.vector(0,0,1)

# inputs: angles a1, a2, a3 and a4 and the length of the arm segments l2,l3,l4
# outputs: a set of coordinates
def arms(a1,a2,a3,a4,l2,l3,l4):
	er = cos(a1)*ex + sin(a1)*ey
	u2 = l2 * ( cos(a2)*er + sin(a2)*ez )
	u3 = l3 * ( cos(a2+a3)*er + sin(a2+a3)*ez )
	u4 = l4 * ( cos(a2+a3+a4)*er + sin(a2+a3+a4)*ez )
#	u4 = l4 * er
	return u2,u3,u4

# input: coordinates x,y,z of the target point, lengths b,c of the arms
# output: angles a1,a2,a3 of the joints, in degrees
def invert(x,y,z,l2,l3,l4):
    s  = "(%g,%g,%g) is out of range." % tuple(around([x,y,z],2))
    a1 = arctan2(y,x)
    r  = hypot(x,y) - l4
    u3 = ( r**2 + z**2 - l2**2 - l3**2 ) / ( 2*l2*l3 )
    if abs(u3)>1:    raise Exception(s)
    a3 = -arccos(u3)
    v  = l2 + l3*u3
    w  = -l3 * sqrt(1-u3**2)  # this is sin(a3), &gt;0 assuming 0&lt;a3&lt;pi
    a2 = arctan2(v*z-w*r,v*r+w*z)
    #    # at this point a2<=0; take the other solution
    #    a2 = 2*arctan2(z,r) - a2
    #    a3 = -a3
    if a2<0 or a2>pi:    raise Exception(s)
    a4 = - a2 - a3
    #    return r2d(a1,a2,a3)
    return a1,a2,a3,a4
	
# Test the mathmatics by drawing the arm in 3D with vpython	
def draw_robot(x,y,z,l2,l3,l4):
	# first draw x,y,z axes
	p0 = 10*vp.vector(-1,-1,0)
	for e in ex,ey,ez: vp.arrow(pos=p0,axis=5*e,shaftwidth=0.5,color=e)
	a1,a2,a3,a4 = invert(x,y,z,l2,l3,l4)                  # compute joint angles
	u2,u3,u4 = arms(a1,a2,a3,a4,l2,l3,l4)                    # compute arm vectors
	w = 0.2                                          # arm radius and base thickness
	u0 = w*ez 
	v0 = cos(a1)*ex + sin(a1)*ey                     # "front" direction
	r = 3                                            # radius of the base
	vp.cylinder(pos=-u0,axis=2*u0,radius=r)         # draw base
	vp.cylinder(pos=-u0+0.8*r*v0,axis=2*u0,radius=0.1*r,color=vp.vector(0.5,0.5,0.5)) # draw grey circle that indicates base direction
	vp.cylinder(pos=vp.vector(0,0,0),axis=u2,radius=w,color=vp.vector(0.7,1,0.7)) # draw arm 2
	vp.sphere(pos=u2,radius=w)                                  # draw joint 2
	vp.cylinder(pos=u2,axis=u3,radius=w,color=vp.vector(0.7,0.7,1))      # draw arm 3
	vp.sphere(pos=u2+u3,radius=w)                               # draw joint 3
	vp.cylinder(pos=u2+u3,axis=u4,radius=w,color=vp.vector(0.7,0.7,1))   # draw arm 4
	vp.sphere(pos=u2+u3+u4,radius=2*w,color=vp.vector(0,1,0))            # draw end of arm 4
	vp.sphere(pos=vp.vector(x,y,z),radius=2*w,color=vp.vector(1,0,0))             # draw target point
	#the last two lines are doing the same but are there for debugging 
    


draw_robot(5,3,4,2,3,4)

