import matplotlib.pyplot as plt

marks = []
kol = []
with open('students.csv', 'r') as f:
    pr = f.read().splitlines()
name = pr[0].split(';')[0]
pr.append('prep0; 000; 0')
for i in range(len(pr)):
    pr[i] = pr[i].split(';')
    if (pr[i][0] == name) and (pr[i][0] != 'prep0'):
        marks.append(int(pr[i][2]))
    else:
        marks.sort()
        print(pr[i-1][0])
        print('marks')
        print(list(set(marks)))
        cur = 0
        for j in range(len(marks)):
            if marks[j] != cur:
                kol.append(marks.count(marks[j]))
                cur = marks[j]
        print('kol')
        print(kol)
        fig, ax = plt.subplots(1)
        fig.set_figheight(3)
        fig.set_figwidth(4)
        ax.scatter(list(set(marks)), kol)
        ax.set_xlim(3, 10)
        ax.set_ylim(0, 7)
        plt.title(str(name))
        ax.set_xlabel("Оценки", fontsize=15, color='blue')
        ax.set_ylabel("Количество", fontsize=15, color='orange')
        ax.grid(color='black',
                linewidth=1,
                linestyle='--')
        plt.show()
        marks.clear()
        kol.clear()
        marks.append(int(pr[i][2]))
        name = pr[i][0]
marks.clear()
kol.clear()
pr.sort(key = lambda x : x[1], reverse=True)
name = pr[0][1]
for i in range(len(pr)):
    if (pr[i][1] == name) and (pr[i][1] != '000'):
        marks.append(int(pr[i][2]))
    else:
        marks.sort()
        print(pr[i - 1][1])
        print('marks')
        print(list(set(marks)))
        cur = 0
        for j in range(len(marks)):
            if marks[j] != cur:
                kol.append(marks.count(marks[j]))
                cur = marks[j]
        print('kol')
        print(kol)
        fig, ax = plt.subplots(1)
        fig.set_figheight(3)
        fig.set_figwidth(4)
        ax.scatter(list(set(marks)), kol)
        ax.set_xlim(3, 10)
        ax.set_ylim(0, 7)
        plt.title(str(name))
        ax.set_xlabel("Оценки", fontsize=15, color='blue')
        ax.set_ylabel("Количество", fontsize=15, color='orange')
        ax.grid(color='black',
                linewidth=1,
                linestyle='--')
        plt.show()
        marks.clear()
        kol.clear()
        marks.append(int(pr[i][2]))
        name = pr[i][1]





