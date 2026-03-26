import numpy as np
from scipy.optimize import minimize


way_points = np.array([[1, 1],
                        [0.9, 2],
                        [0.9, 3],
                        [1.4, 4.1],
                        [1.7, 5],
                        [2.3, 6]])

a = 1.3
dt = 0.02
v_des = 10
omega = 0.23

def compute_heading_ref(p1, p2):
    theta_ref = np.arctan2(p2[1]-p1[1], p2[0]-p1[0])
    return theta_ref
def compute_distance(X, Y, p1, p2):
    x1, y1 = p1
    x2 , y2 = p2
    A = y2-y1
    B = x1-x2
    C = x2*y1 - x1*y2
    num = A*X + B*Y + C
    den = np.sqrt(A**2 + B**2)
    
    return num/den
    


def total_cost(weights):
    w_theta, w_dist, w_vel = weights
    
    if any (w<0 for w in weights):
        return 1e6
    
    X, Y, theta, v = 0.1, 3.1, 0.0, 5.5
    J = 0.0
    
    for k in range(4):
        p1 = way_points[k]
        p2 = way_points[k+1]
        
        theta_ref = compute_heading_ref(p1, p2)
        e_theta = theta - theta_ref
        e_dist = compute_distance(X, Y, p1, p2)
        e_vel = v - v_des
        
        J += (w_theta*e_theta**2 +
            w_dist*e_dist**2 +
            w_vel*e_vel**2)
        
        X += v*np.cos(theta)*dt 
        Y += v*np.sin(theta)*dt  
        theta += omega*dt
        v += a*dt
        
    return J

initial_guess = [1.0, 1.0, 1.0]
result = minimize(total_cost, initial_guess, method="Nelder-Mead")

print("Optimal Weights: ", result.x)
print("Minimum cost: ", result.fun)