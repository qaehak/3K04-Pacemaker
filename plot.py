# Test how to plot data

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#create data frame
#df = pd.DataFrame({'x': [0,1,2,3],
#                   'y': [0,1,2,3]})

# with open("test_data.txt", 'r') as f:
#     lines = f.readlines()
#     x = [int(line.split()[0]) for line in lines]
#     y = [int(line.split()[1]) for line in lines]
#     df = pd.DataFrame({x,y})
#--------------PREVIOUS TESTER CODE---------------------------------------
df = pd.read_csv("test_data.txt",sep='\s+',header=None)
df = pd.DataFrame(df)

x1 = df[0]
y1 = df[1]
#set up seaborn
sns.set()

#set axis
ax = sns.lineplot(data=df, x=x1,y=y1)
print(x1)
print(y1)

plt.title("Test")

#save plot as png
plt.savefig("testplot.png")

#display plot
plt.show()
#-------------------------------------------------------

#get realtime data for number of seconds
#figure out how we are going to format data in x,y
#to constantly update graph, once a specific buffer of points were recieved, replot graph
time = 0
while(True):
    time = time + 1
    print('time:', time)
    data_raw = ser.readline(1)
    print(data_raw)
    print("\n")
    if time == 100:
        break
    