import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.patches as patches
from LucasKanade import LucasKanade

# write your script here, we recommend the above libraries for making your animation

frames = np.load('../data/carseq.npy')
n = frames.shape[2]

rect = np.zeros((n, 4))
rect[0, :] = [59, 116, 145, 151]
p_prev = np.zeros(2)

for i in range(50):
    print(i)
    # initial p_n
    p_n = LucasKanade(frames[:, :, i], frames[:, :, i + 1], rect[i,:], p0=np.zeros(2))

    # update
    p_star = LucasKanade(frames[:, :, 0], frames[:, :, i + 1], rect[0, :], p0=p_prev+p_n)

    # print('p_n', p_n)
    # print('p_star',p_star)
    if np.linalg.norm(p_prev+p_n-p_star) < 0.2:
        rect[i+1,:] = rect[0, :] + np.concatenate((p_star, p_star))
        p_prev = p_star
        # print('p_prev',p_prev)
    else:
        rect[i + 1, :] = rect[i, :]


    fig, ax = plt.subplots(1)
    w = rect[i, 3] - rect[i, 1]
    h = rect[i, 2] - rect[i, 0]
    co = (rect[i, 0], rect[i, 1])
    box = patches.Rectangle(co, h, w, edgecolor='r', facecolor='none')
    ax.imshow(frames[:, :, i], cmap='gray')
    ax.add_patch(box)
    fig.show()


# for i in [1, 100, 200, 300,400]:
#     fig, ax = plt.subplots(1)
#     w = rect[i, 3] - rect[i, 1]
#     h = rect[i, 2] - rect[i, 0]
#     co = (rect[i, 0], rect[i, 1])
#     box = patches.Rectangle(co, h, w, edgecolor='r', facecolor='none')
#     ax.imshow(frames[:, :, i], cmap='gray')
#     ax.add_patch(box)
#     fig.savefig('../results/1-4-'+str(i)+'.png')
#     plt.close(fig)
