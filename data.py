from typing import Counter
import plotly.figure_factory as ff
import statistics
import pandas as pd
import csv 
import random 
 
df = pd.read_csv("./data.csv")
data = df["reading_time"].tolist()
print("population mean",statistics.mean(data))
print("population standardDeviation",statistics.stdev(data))
 
fig = ff.create_distplot([data],["reading_time"],show_hist = False)
fig.show()
 

def random_set_of_mean(Counter):
    dataset = []
    for i in range (0,Counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
        sample_counter_mean = statistics.mean(dataset)
        #print("sample_mean",sample_counter_mean)
       # print("sample_counter_standard_deviation",statistics.stdev(dataset))
    return sample_counter_mean
    
def setup():
    mean_list = []
    for i in range (0,100):
        set_of_sample_mean = random_set_of_mean(30)
        mean_list.append(set_of_sample_mean)
    print("sampling_mean",statistics.mean(mean_list)),
    print("sampling_standard_deviation",statistics.stdev(mean_list))
    fig = ff.create_distplot([mean_list],["sampling reading_time"],show_hist = False)
    fig.show()

setup()

#standard deviation of smapling mean = 1/10 of population standard deviation
#the distribution is not normal when the sample sizes are small but if the sample sizes are big then that sample follows normal distribution
#sampling mean = population mean 
#samplingError = population standard deviation / squrt(sampling size)