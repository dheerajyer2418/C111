import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#Plotting the graph
#fig = ff.create_distplot([data],["Math Scores"], show_hist= False)
#fig.show()

#Calculating the mean and the standard deviation
#mean = statistics.mean(data)
#std_deviation = statistics.stdev(data)
#print("Mean of Population: ", mean)
#print("Standard Deviation of Population: ", std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("Mean of Sampling Distribution: ", mean)
fig = ff.create_distplot([mean_list],["Student_Marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20],mode = "lines",name = "MEAN"))
fig.show()

