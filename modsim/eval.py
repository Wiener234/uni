import csv
import matplotlib.pyplot as plt
from math import e

#One run
# x = []
# steps = []
# time = []
# with open("modsim_0.1_32.csv", "r") as file:
#     reader = csv.DictReader(file)
#     i = 0
#     for row in reader:
#         if i >= 100:
#             break
#         x.append(int(row["Iteration of Size"]))
#         steps.append(int(row["Steps"]))
#         time.append(int(row["Time"]))
#         i+=1
        
# plt.plot(x, steps, "g")
# plt.plot(x, time, "y")
# plt.show()




#Bug 1
i=0
steps = []
x = []
j = 2
size = []
times = []
for j in range(3,33):
    time = 0
    step = 0
    filename = "modsim_0.1_" + str(j) + ".csv"
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

exp = []
for i in size:
    exp.append(((4/6)*e)**i)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(size, exp, 'g')
plt.plot(size, times, 'r')
plt.plot(size, steps, 'b')

# plt.axis([3,32,1,times[len(times)-1]])

# plt.semilogy()
# for i, v in enumerate(times,3):
#     ax.text(i, v+25, "%d" %v, ha="center")

plt.show()

#Bug 2
# i=0
# steps = []
# x = []
# j = 2
# size = []
# times = []
# for j in range(3,33):
#     time = 0
#     step = 0
#     filename = "modsim_0.2_" + str(j) + ".csv"
#     with open(filename, "r") as file:
#         reader = csv.DictReader(file)
#         i=0
#         for row in reader:
#             if i >= 100:
#                 break
#             x.append(int(row["Iteration of Size"]))
#             step += int(row["Steps"])
#             time += int(row["Time"])
#             i+=1
#     size.append(j)
#     steps.append(step/100)
#     times.append(time/100)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# plt.plot(size, times, 'r')
# plt.plot(size, steps, 'b')

# plt.axis([3,32,1,times[len(times)-1]])

# plt.semilogy()
# # for i, v in enumerate(times,3):
# #     ax.text(i, v+25, "%d" %v, ha="center")

# plt.show()
