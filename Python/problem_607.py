import matplotlib.pyplot as plt
import numpy as np

def optimise_points():
    x = [-50, -25*np.sqrt(2), -15*np.sqrt(2), -5*np.sqrt(2),
                5*np.sqrt(2), 15*np.sqrt(2), 25*np.sqrt(2), 50]
    y = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(0, -6, -1):
        eps = 10 ** i
        t = time(x, y)
        
        change = True
        while change:
            change = False
            
            for j in range(1, 7):
                x[j] += eps
                y[j] += eps
                if time(x, y) < t:
                    change = True
                    t = time(x, y)
                    continue
                else:
                    x[j] -= eps
                    y[j] -= eps
                    
                x[j] -= eps
                y[j] -= eps
                if time(x,y) < t:
                    change = True
                    t = time(x, y)
                    continue
                else:
                    x[j] += eps
                    y[j] += eps
                
    print(round(t, 10))
    return x, y
                
        
def time(x, y):
    return (np.sqrt((y[1]-y[0])**2 + (x[1]-x[0])**2)/10
            + np.sqrt((y[2]-y[1])**2 + (x[2]-x[1])**2)/9
            + np.sqrt((y[3]-y[2])**2 + (x[3]-x[2])**2)/8
            + np.sqrt((y[4]-y[3])**2 + (x[4]-x[3])**2)/7
            + np.sqrt((y[5]-y[4])**2 + (x[5]-x[4])**2)/6
            + np.sqrt((y[6]-y[5])**2 + (x[6]-x[5])**2)/5
            + np.sqrt((y[7]-y[6])**2 + (x[7]-x[6])**2)/10)

def draw_map(x, y):
    fig, ax = plt.subplots()
    
    ax.fill_between([-100, 100], [-100+25*np.sqrt(2), 100+25*np.sqrt(2)], [-100+15*np.sqrt(2), 100+15*np.sqrt(2)], color=(0, 0.7, 0))
    ax.fill_between([-100, 100], [-100+15*np.sqrt(2), 100+15*np.sqrt(2)], [-100+5*np.sqrt(2), 100+5*np.sqrt(2)], color=(0, 0.6, 0))
    ax.fill_between([-100, 100], [-100+5*np.sqrt(2), 100+5*np.sqrt(2)], [-100-5*np.sqrt(2), 100-5*np.sqrt(2)], color=(0, 0.5, 0))
    ax.fill_between([-100, 100], [-100-5*np.sqrt(2), 100-5*np.sqrt(2)], [-100-15*np.sqrt(2), 100-15*np.sqrt(2)], color=(0, 0.4, 0))
    ax.fill_between([-100, 100], [-100-15*np.sqrt(2), 100-15*np.sqrt(2)], [-100-25*np.sqrt(2), 100-25*np.sqrt(2)], color=(0, 0.3, 0))
    
    plt.plot(x, y, marker="x", color="r")
    
    plt.axis("equal")
    plt.xlim([-60, 60])
    plt.ylim([-40, 40])
    
    plt.show()

if __name__ == "__main__":
    x, y = optimise_points()
    draw_map(x, y)
    