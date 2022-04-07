Web VPython 3.2
'''
Imports CSV
'''
f = read_local_file(scene.title_anchor)

data = f.text
current_text = ""
p_array = [] # Distance to the origin in meters
th_array = [] # Polar angle in radians
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


for k in range(360): # Basically ends up rotating the pattern, probability density is spherically symmetric
    for i, ival in enumerate(th_array): # For loop for array of theta angles
        for j,jval in enumerate(p_array): # For loop for array of distances to the origin
            electron = sphere(pos=sph_to_cart(p_array[j], th_array[i], pi*k/180), radius = 0.5*10**-16, opacity = prob_dens[i])