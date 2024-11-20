import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import patches
''' 
Create the P3 lattice: 
Rules:
* There are three lattice constants: 
the first two are alternating to create one line and the thirds one creates columns by shifting all line elements
* Orientations are "anti-ferromagnetic" that means that neighbouring particles are always tilted by 180 degrees
* the length of the rhombi is assumed to be 1 
* if length of rhombi is different from one, everything can be scaled 
'''

N_particles = 900 
N_side = 30
alpha=np.pi/3
delta=0.4 
l=1 
Lbox=
start = np.array([Lbox/4,Lbox/4])

sin60 = np.sin(np.pi/3.)
cos60 = np.cos(np.pi/3.)

ax0 = np.array([[1,cos60],[0,sin60]])
edges = np.zeros((4,2))
ax_n = np.zeros((2,2))

cA = np.cos(alpha)
sA = np.sin(alpha)
D = np.abs(1-2*delta) 


lattice_a1 = np.array([1 + cA*D, -sA*D])
lattice_b1 = np.array([-cA + D, sA])
lattice_b2 = np.array([1 - cA*D, sA*D])
def get_edge_points(pos_i,ax_n,sign_p):
    edge_n = np.zeros(2)
    edge_n = pos_i + sign_p[0]*ax_n[:,0]/2. + sign_p[1]*ax_n[:,1]/2.

    return edge_n

def rotation_matrix(theta):
    rot_mat = np.zeros((2,2))

    rot_mat[0,0] = np.cos(theta) 
    rot_mat[0,1] = -np.sin(theta)
    rot_mat[1,0] = np.sin(theta)
    rot_mat[1,1] = np.cos(theta)

    return rot_mat

def get_orient(v, rot_mat):
    return rot_mat.dot(v)

points = np.zeros([N_particles,2])
ci = 0

for i in range(N_side):
    for j in range(N_side):
           
            c1 = np.ceil(i/2)
            c2 = np.ceil((i-1)/2)
            c3 = j
            c4 = j

            points[ci] = c1*lattice_a1  + c2*lattice_b2 + j*lattice_b1 + j*lattice_b2
            ci+=1 
points[0] = np.array([0,0])
points = points + start 

rhombus_color='#752b54'
fig,ax=plt.subplots()
for i in range(N_particles):
    rotmat_i = rotation_matrix(2*np.pi/3)
    ax_n = get_orient(ax0, rotmat_i)

    edges[0] = get_edge_points(points[i],ax_n,np.array([-1,-1]))
    edges[1] = get_edge_points(points[i],ax_n,np.array([+1,-1]))
    edges[2] = get_edge_points(points[i],ax_n,np.array([+1,+1]))
    edges[3] = get_edge_points(points[i],ax_n,np.array([-1,+1]))

    rhombi = patches.Polygon(edges, linewidth=0.1, edgecolor='k',facecolor=rhombus_color, alpha=0.7)
    ax.add_patch(rhombi)
               
plt.xlim((-1,Lbox))
plt.ylim((-1,Lbox))
plt.axis("equal")
plt.axis('off')
plt.savefig("P3.pdf")
plt.close()

np.tofile()