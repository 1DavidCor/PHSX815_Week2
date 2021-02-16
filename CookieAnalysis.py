#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times_default = Sorter.DefaultSort(times)
    times_avg_default = Sorter.DefaultSort(times_avg)
    
    # try some other methods! see how long they take
    times_bubble = Sorter.BubbleSort(times)
    times_avg_bubble = Sorter.BubbleSort(times_avg)
    times_insertion = Sorter.InsertionSort(times)
    times_avg_insertion = Sorter.InsertionSort(times_avg)
    times_quick = Sorter.QuickSort(times)
    times_avg_quick = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE
    rainbow = ['#ff0000', '#ffa500', '#ffff00', '#008000','#10a5f5', '#673ab7', '#ee82ee']
    
    plt.figure()
    plt.title("Default Sort: rate = 2.0 cookies/day")
    plt.ylabel("Probability")
    plt.xlabel("Time between missing cookies [days]")
    plt.xlim(0, np.max(times_default))
    #plt.ylim(0, 1)
    plt.hist(times_default, 100, density=True, color=rainbow[0], alpha=0.75)
    
    plt.figure()
    plt.title("Default Sort Average: rate = 2.0 cookies/day")
    plt.ylabel("Probability")
    plt.xlabel("Average time between missing cookies [days]")
    #plt.xlim(0, np.max(times_avg_default))
    #plt.ylim(0, 1)
    plt.hist(times_avg_default, 100, density=True, color=rainbow[1], alpha=0.75)
    
    plt.figure()
    plt.title("Bubble Sort: rate = 2.0 cookies/day")
    plt.ylabel("Probability")
    plt.xlabel("Time between missing cookies [days]")
    plt.xlim(0, np.max(times_bubble))
    #plt.ylim(0, 1)
    plt.hist(times_bubble, 100, density=True, color=rainbow[2], alpha=0.75)
    
    plt.figure()
    plt.title("Bubble Sort Average: rate = 2.0 cookies/day")
    plt.ylabel("Probability")
    plt.xlabel("Average time between missing cookies [days]")
    #plt.xlim(0, np.max(times_avg_default))
    #plt.ylim(0, 1)
    plt.hist(times_avg_bubble, 100, density=True, color=rainbow[3], alpha=0.75)
    
    plt.figure()
    plt.title("Insertion Sort: rate = 2.0 cookies/day")
    plt.ylabel("Probability")
    plt.xlabel("Time between missing cookies [days]")
    plt.xlim(0, np.max(times_insertion))
    #plt.ylim(0, 1)
    plt.hist(times_insertion, 100, density=True, color=rainbow[4], alpha=0.75)
    
    plt.figure()
    plt.title("Insertion Sort Average: rate = 2.0 cookies/day")
    plt.ylabel("Probability")
    plt.xlabel("Average time between missing cookies [days]")
    #plt.xlim(0, np.max(times_avg_default))
    #plt.ylim(0, 1)
    plt.hist(times_avg_insertion, 100, density=True, color=rainbow[5], alpha=0.75)
    
    plt.figure()
    plt.title("Quick Sort: rate = 2.0 cookies/day")
    plt.ylabel("Probability")
    plt.xlabel("Time between missing cookies [days]")
    plt.xlim(0, np.max(times_quick))
    #plt.ylim(0, 1)
    plt.hist(times_quick, 100, density=True, color=rainbow[6], alpha=0.75)
    
    plt.figure()
    plt.title("Quick Sort Average: rate = 2.0 cookies/day")
    plt.ylabel("Probability")
    plt.xlabel("Average time between missing cookies [days]")
    #plt.xlim(0, np.max(times_avg_default))
    #plt.ylim(0, 1)
    plt.hist(times_avg_quick, 100, density=True, color=rainbow[0], alpha=0.75)
    
    plt.show()
    
    
