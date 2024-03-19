import math

class Kepler():
    
    # 10 points for using the right kind of data structure and managing the data structure correctly 
    def __init__(self):
        self.observations = {}
    def observe(self, planet_name, position, time):                                
        planet_obs = self.observations.setdefault(planet_name,[])
        planet_obs.append((position,time))
        
    def get_period(self,planet_name):     # 8 points
        planet_obs = self.observations.get(planet_name, [])
        if len(planet_obs) < 2:  # 2 points for the test
            return None
        else:
            ts = []
            for i in range(len(planet_obs) - 1): # 3 points for handling consecutive observations
                (a1,t1) = planet_obs[i]
                (a2,t2) = planet_obs[i+1]
                a = a2-a1
                ts.append(2*math.pi*(t2-t1)/a)
            return sum(ts) / len(ts) # 3 points for the correct averaging
     
    def get_radius(self,planet_name): # 5 points
        t = self.get_period(planet_name)
        if not t: return None  # 2 points for the test
        return (t**2 * G * M / (4 * math.pi ** 2)) ** (1/3) # 3 points for the formula
    def print_planets(self): # 2 points
        for p in self.observations:
            print(p, self.get_period(p), self.get_radius(p))

M = 1.991e30
G = 6.67e-11
