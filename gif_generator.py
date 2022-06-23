import matplotlib.pyplot as plt
import matplotlib.animation as animation

from random import randint
import sorting_steps

n = 50
array = [randint(5, 5*n) for _ in range(n)]
base_list = [(i+1)*1.5 for i in range(n)]
steps = sorting_steps.merge_sort_steps(array)
for i in range(20):
    steps.append(steps[-1])

fig, ax = plt.subplots()
def animate(step):
    plt.cla()
    ax.set_ylim(bottom=0, top=260)
    ax.bar(base_list,step, width=0.5)
ani = animation.FuncAnimation(fig, animate, frames=steps, interval=20, repeat=False)

# plt.show()
writer = animation.PillowWriter(fps=8)
writer.setup(ani, "merge.gif", dpi=150)
ani.save("merge.gif", writer=writer)
