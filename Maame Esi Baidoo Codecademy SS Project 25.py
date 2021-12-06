# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
#To display different plots at once
#Plotting histogram for flights to determine when is the best time to take a flight
plt.figure(1)
plt.subplot(211)
plt.hist(flights, range = (0, 365), bins = 365)
plt.xlabel("Day of the year")
plt.ylabel("Flights count")
plt.title("Frequency of flights per day")
#Plotting histogram for in_bloom to determine when is the best time to visit Acadia or Maine
plt.subplot(212)
plt.hist(in_bloom, range = (0, 365), bins = 365)
plt.ylabel("Bloom count")
plt.xlabel("Day of the year")
plt.title("Frequency of Blooms per day")
#To prevent labels from overlapping
plt.tight_layout()

plt.show()