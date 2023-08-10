import csv
import matplotlib.pyplot as plt
from math import e
import numpy as np

# # Uncomment to show time and steps of every labyrinth size from 0.1
x = []
steps = []
time = []
for j in range(3,39):
    steps = []
    time = []
    times = 0
    step = 0
    x = []
    filename = "data/modsim_0.1_"+str(j)+".csv"
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        i = 0
        for row in reader:
            if i >= 100:
                break
            x.append(int(row["Iteration of Size"]))
            steps.append(int(row["Steps"]))
            time.append(int(row["Time"]))
            # times+=int(row["Time"])
            # step+=int(row["Steps"])
            i+=1
    l = [] 
    for i in range(1,101):
        l.append(times/100)

    # print(times/100)
    # print(step/100)
    # plt.plot(x, l, "g")
    plt.plot(x, time, "r")
    plt.plot(x, steps, "b")
    plt.xlabel("Nummer der Durchläufe für: " + str(j))
    plt.ylabel("Zeit/Schritte")
    plt.legend(["Zeit", "Schritte"], loc="upper left")
    plt.show()

# # Uncomment to show time and steps of every labyrinth size from 0.2
# x = []
# steps = []
# time = []
# for j in range(3,39):
#     steps = []
#     time = []
#     x = []
#     filename = "data/modsim_0.2_"+str(j)+".csv"
#     with open(filename, "r") as file:
#         reader = csv.DictReader(file)
#         i = 0
#         for row in reader:
#             if i >= 100:
#                 break
#             x.append(int(row["Iteration of Size"]))
#             steps.append(int(row["Steps"]))
#             time.append(int(row["Time"]))
#             i+=1
       
#     plt.plot(x, time, "r")
#     plt.plot(x, steps, "b")
#     plt.xlabel("Nummer der Durchläufe für: " + str(j))
#     plt.ylabel("Zeit/Schritte")
#     plt.legend(["Time", "Steps"], loc="upper left")
#     plt.show()



# Bug 1
i=0
steps = []
x = []
j = 2
size = []
times = []
for j in range(3,39):
    time = 0
    step = 0
    filename = "data/modsim_0.1_" + str(j) + ".csv"
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        i=0
        for row in reader:
            if i >= 100:
                break
            x.append(int(row["Iteration of Size"]))
            # if step == 0 or step > int(row["Steps"]):
            #     step = int(row["Steps"])
            # if time == 0 or time > int(row["Time"]):
            #     time = int(row["Time"])
            
            step += int(row["Steps"])
            time += int(row["Time"])
            i+=1
    size.append(j)
    steps.append(step/100)
    times.append(time/100)

exp = []
for i in size:
    # exp.append(((4/6)*e)**i)
    exp.append(e**(i))

# fig = plt.figure()
# ax = fig.add_subplot(111)
# plt.plot(size, exp, 'y')
plt.plot(size, times, 'r')
plt.plot(size, steps, 'b')

# coef = np.polyfit(size, np.log(times), 1)
# y = []
# for i in size:
#     y.append(np.exp(5.915)*np.exp(0.3649 * i))
# plt.plot(size, y, '--k' )

# coef = np.polyfit(size, np.log(steps), 1)
# y = []
# for i in size:
#     y.append(np.exp(5.380)*np.exp(0.3658 * i))
# plt.plot(size, y, '--g' )















# plt.semilogy()

# plt.xlabel("Größe des Labyrinths")
# plt.ylabel("Zeit/Schritte")

# plt.legend(["Zeit", "Schritte", "Regressionskurve Zeit", "Regressionskurve Schritte"], loc="upper left")
# for i, v in enumerate(times,3):
#     ax.text(i, v+25, "%d" %v, ha="center")

# plt.show()

#Bug 2
i=0
steps = []
x = []
j = 2
size = []
times = []
for j in range(3,39):
    time = 0
    step = 0
    filename = "data/modsim_0.2_" + str(j) + ".csv"
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        i=0
        for row in reader:
            if i >= 100:
                break
            x.append(int(row["Iteration of Size"]))
            step += int(row["Steps"])
            time += int(row["Time"])
            i+=1
    size.append(j)
    steps.append(step/100)
    times.append(time/100)

# fig = plt.figure()
# ax = fig.add_subplot(111)
plt.plot(size, times, 'g')
plt.plot(size, steps, 'y')





# # Ausgleichskurve
# coef = np.polyfit(size, np.log(times), 1)
# y = []
# for i in size:
#     y.append(np.exp(5.299)*np.exp(0.3403 * i))
# plt.plot(size, y, 'k--' )

# coef = np.polyfit(size, np.log(steps), 1)
# y = []
# for i in size:
#     y.append(np.exp(4.747)*np.exp(0.3412 * i))
# plt.plot(size, y, 'g--' )








plt.semilogy()

plt.xlabel("Größe des Labyrinths")
plt.ylabel("Zeit/Schritte")

plt.legend(["Zeit v1", "Schritte v1", "Zeit v2", "Schritte v2"], loc="upper left")
# for i, v in enumerate(times,3):
    # ax.text(i, v+25, "%d" %v, ha="center")

plt.show()
