""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc

class Point:
        def __init__(self,coord):
            self.coord = coord
        
        def distance(self):
            return sum(map(lambda x: x*x,self.coord))
            
    
        def plot(self, color = 'blue'):  #2D Plot
            plt.scatter(self.coord[0],self.coord[1],color = color)



def approximate_pi(n): # Ex1
    #n is the number of points
    # Write your code here
    
    count = 0
    for i in range(n):
        point = Point([random.uniform(-1,1),random.uniform(-1,1)])
        if point.distance() <=1:
            count += 1
            point.plot()
        else:
            point.plot(color = 'red')
   
    
    return 4*count/n

def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    #d is the number of dimensions of the sphere 
    point_lst = [Point([random.uniform(-1,1) for _ in range(d)]) for _ in range(n)]
    count = len(list(filter(lambda x: x.distance() <= 1, point_lst)))
    return (2**d)*count/n


def hypersphere_exact(n,d): #Ex2, real value
    # n is the number of points
    # d is the number of dimensions of the sphere 

    return (m.pi**(d/2))/m.gamma((d/2)+1)


#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes

    with future.ProcessPoolExecutor() as ex:
        process = []
        for _ in range(np):
            process.append(ex.submit(sphere_volume,n,d))
        
        res = [process[i].result() for i in range(np)]
        

    return sum(res)/np


#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes

    

    with future.ProcessPoolExecutor() as ex:
        
        def Point_lst(n,d):
            return [Point([random.uniform(-1,1) for _ in range(d)]) for _ in range(n)]
        
        def Inside(lst):
            for i in range(lst):
                return lst[i].distance <= 1



        p1 = ex.submit(Point_lst,n,d)
        p1res = [p1[i].res for i in range(n)]
        p2 = ex.submit(Inside,p1res)

    
    
    return 
    
def main():
    '''
   print(approximate_pi(1500))

    plt.show()

    #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
 
    #Ex2
    n = 100000
    d = 2
    print(sphere_volume(n,d))
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")


    n = 100000
    d = 11
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")
'''
   # Ex3
    n = 10**5
    d = 10
    res = []
    start = pc()
    for y in range (10):
        res.append(sphere_volume(n,d))
    stop = pc()
    print(f'average result is :{sum(res)/10}')
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    start = pc()
    print(f'result for parallell: {sphere_volume_parallel1(100000,10)}')
    stop = pc()
    print(f'time for parallell: {stop-start}')
'''
    #Ex4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")
'''
    
    

if __name__ == '__main__':
	main()
