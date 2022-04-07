Web VPython 3.2
'''
Imports CSV
'''
f = read_local_file(scene.title_anchor)

data = f.text
current_text = ""
p_array = [] # Distance to the origin in meters
th_array = [] # Polar angle in radians
az_array = [] # Azimuthal angle in radians
prob_dens = [] # 2D array, each probability density is indexed by a radius and an angle theta
counter = 0
for c in data:
    if c == "\r":
        pass # Ignore return characters
    else if c == "," or c == "\n":
        if counter == 0:
            p_array.append(float(current_text))
            current_text = ""
            counter = counter + 1
        else if counter == 1:
            th_array.append(float(current_text))
            current_text = ""
            counter = counter + 1
        else if counter == 2:
            az_array.append(float(current_text))
            current_text = ""
            counter = counter + 1
        else if counter == 3:
            prob_dens.append(float(current_text)) # CAUSES COULD NOT CONVERT STRING TO FLOAT
            current_text = ""
            counter = 0
    else:
        current_text = current_text + c # Builds a string, going letter by letter
print(p_array)
print(th_array)
print(prob_dens)
'''
Creates the nucleus of the helium atom
'''
proton1 = sphere(pos=vector(1.7*10**-15,1.7*10**-15,0), radius=1.7*10**-15, color=color.red)
proton2 = sphere(pos=vector(-1.7*10**-15,-1.7*10**-15,0), radius=1.7*10**-15, color=color.red)
neutron1 = sphere(pos=vector(-1.7*10**-15,1.7*10**-15,0), radius=1.7*10**-15, color=color.yellow)
neutron2 = sphere(pos=vector(1.7*10**-15,-1.7*10**-15,0), radius=1.7*10**-15, color=color.yellow)
'''
Imports CSV and creates array for the radii, polar angle and their corresponding probability densities.
Our probability densities should not depend on the azimuthal angle.
'''

def sph_to_cart(p, the, phi):
    ansx = p*sin(phi)*cos(the)
    ansy = p*sin(phi)*sin(the)
    ansz = p*cos(phi)
    result = vector(ansx,ansy,ansz) # Result is vector in x,y,z
    return result

def visualize_sphere(in_p, in_prob):
    for k in range(360):
        for j in range(360):
            for i,ival in enumerate(in_p):
                electron = sphere(pos=sph_to_cart(in_p[i], pi*j/180, pi*k/180), radius = 0.5*10**-16, opacity = in_prob[i])

# Visualization for cylindrically symmetric orbitals with prob_dens input. Assumes there is a value for p, th, and prob for each row in the csv table
def visualize_cylinder(in_p, in_th, in_prob):
    for k in range(360): # Basically ends up rotating the pattern, probability density is cylindrically symmetric
        for i, ival in enumerate(in_th): # For loop for array of theta angles
            electron = sphere(pos=sph_to_cart(in_p[i], in_th[i], pi*k/180), radius = 0.5*10**-16, opacity = in_prob[i])

def visualize_general(in_p, in_th, in_az, in_prob):
    for i, ival in enumerate(in_p): # Already assuming there are an equal number of inputs for p, th, az, and prob
        electron = sphere(pos=sph_to_cart(in_p[i], in_th[i], in_az[i]), radius = 0.5*10**-16, opacity = in_prob[i])

visualize_sphere(p_array, prob_dens)
#visualize_general(p_array, th_array, az_array, prob_dens)