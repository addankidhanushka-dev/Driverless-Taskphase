import numpy as np
cones = {
    "B1" : (12,7),
    "B2" : (8,6),
    "Y1" : (13,4),
    "Y2" : (9,3)
}

def to_car_frame(cones, xg, yg, theta_deg):
    theta = np.radians(theta_deg)
    
    R = np.array([[np.cos(theta), np.sin(theta)],
                 [-np.sin(theta), np.cos(theta)]])
    
    result = {}
    for name, (x,y) in cones.items():
        dx = xg - x
        dy = yg - y
        (xc, yc) = R@np.array([dx, dy])
        result[name] = (float(round(xc,3)), float(round(yc,3)))
        
    return result

initial_pos = to_car_frame(cones, 10, 5, 30)
new_pos = to_car_frame(cones, 10.874, 5.525, 32)

for name, (x,y) in initial_pos.items():
    print(name, (x,y))
    
print
for name, (x,y) in new_pos.items():
    print(name, (x,y))
    

        

    
    
    