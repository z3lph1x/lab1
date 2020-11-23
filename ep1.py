import matplotlib.pyplot as plt

with open('003.dat', 'r') as f:
    nums = f.read().split()
N = int(nums[0])
X = []
Y = []
print(N)
print(nums)
for i in range(N):
    X.append(float(nums[2*i+1]))
    Y.append(float(nums[2*(i+1)]))
print(X)
print(Y)
maxX = max(X)
minX = min(X)
maxY = max(Y)
minY = min(Y)
fig, ax = plt.subplots(1)
if (maxX - minX) / (maxY - minY) > 1:
    sz = (maxX - minX) / (maxY - minY)
    fig.set_figheight(3)
    fig.set_figwidth(sz * 2)

else:
    sz = (maxY - minY) / (maxX - minX)
    fig.set_figheight(sz * 2)
    fig.set_figwidth(3)
ax.scatter(X, Y)
ax.set_xlim([minX-3, maxX+3])
ax.set_ylim([minY-3, maxY+3])
plt.title('Number of points: '+str(N))

plt.show()

