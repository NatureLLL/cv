import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.patches as patches
from LucasKanade import LucasKanade

# write your script here, we recommend the above libraries for making your animation

frames = np.load('../data/carseq.npy')
n = frames.shape[2]
# print(n)

# (num_frame,4)
rect = np.zeros((n, 4))
rect[0, :] = [59, 116, 145, 151]

for i in range(n-1):
    p = LucasKanade(frames[:, :, i], frames[:, :, i + 1], rect[i,:], p0=np.zeros(2))
    rect[i + 1, :] = rect[i, :] + np.concatenate((p, p))

for i in [1, 100, 200, 300,400]:
    fig, ax = plt.subplots(1)
    w = rect[i, 3] - rect[i, 1]
    h = rect[i, 2] - rect[i, 0]
    co = (rect[i, 0], rect[i, 1])
    box = patches.Rectangle(co, h, w, edgecolor='r', facecolor='none')
    ax.imshow(frames[:, :, i], cmap='gray')
    ax.add_patch(box)
    fig.savefig('../1-3-'+str(i)+'.png')
    plt.close(fig)
