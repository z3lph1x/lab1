import matplotlib.pyplot as plt
X = []
Y = []
with open('frames.dat.txt', 'r') as f:
    nums = f.read().splitlines()
for i in range(0, len(nums), 2):
    nums[i] = nums[i].split(' ')
    nums[i+1] = nums[i+1].split(' ')
    for j in range(len(nums[i])):
        nums[i][j] = float(nums[i][j])
        nums[i+1][j] = float(nums[i+1][j])
    X = nums[i]
    Y = nums[i+1]
    fig, ax = plt.subplots(1)
    fig.set_figheight(3)
    fig.set_figwidth(4)
    plt.plot(X, Y)
    ax.set_xlim(0, 17)
    ax.set_ylim(-15, 15)
    plt.title('Frame ' + str(int(i/2+1)))
    ax.grid(color='black',
            linewidth=1,
            linestyle='--')
    plt.show()



