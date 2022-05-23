import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

def one_image(w, X, Y):
    axes = plt.gca()
    axes.set_xlim([-4,4])
    axes.set_ylim([-1.5,1.5])
    d1 = {-1:'green', 1:'red'}
    im = plt.scatter(X[:,0], X[:,1], c=[d1[y] for y in Y])
    im = newline([0,-w[2]/w[1]],[-w[2]/w[0],0], 'blue')
#    im = newline([0,1/w[1]-w[2]/w[1]],[1/w[0]-w[2]/w[0],0], 'lime') #w0*x_i[0]+w1*x_i[1]+w2*1=1
#    im = newline([0,-1/w[1]-w[2]/w[1]],[-1/w[0]-w[2]/w[0],0]) #w0*x_i[0]+w1*x_i[1]+w2*1=-1
    return im

fig = plt.figure()

ims = []
for i in range(500):
    if i<=300:
        k = i
    else:
        k = (i-298)*130
    im = one_image(svm.history_w[k], X_train, Y_train)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=20, blit=True,
                                repeat_delay=500)

writer = PillowWriter(fps=20)
ani.save("my_demo.gif", writer='imagemagick')