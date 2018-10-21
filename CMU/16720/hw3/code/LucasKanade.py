import numpy as np
from scipy.interpolate import RectBivariateSpline


def LucasKanade(It, It1, rect, p0=np.zeros(2)):
    # Input:
    #	It: template image
    #	It1: Current image
    #	rect: Current position of the car
    #	(top left, bot right coordinates)
    #	p0: Initial movement vector [dp_x0, dp_y0]
    # Output:
    #	p: movement vector [dp_x, dp_y]

    p = p0
    delta_p = 0
    diff = 1
    thr = 0.5

    # compute spline function
    func_I = RectBivariateSpline(np.arange(It1.shape[0]), np.arange(It1.shape[1]), It1)
    func_T = RectBivariateSpline(np.arange(It.shape[0]), np.arange(It.shape[1]), It)

    # todo: check whether x row and y column
    # template image rectangle
    x = np.arange(rect[0], rect[2] + 1)
    y = np.arange(rect[1], rect[3] + 1)

    xv, yv = np.meshgrid(x, y)
    xv = xv.flatten()
    yv = yv.flatten()
    # T = func_T.ev(xv, yv)
    # debug
    T = func_T.ev(yv, xv)

    N = len(xv)

    print('-----------',p)
    #debug
    xx, yy = np.meshgrid(np.arange(0,rect[2]-rect[0]+1), np.arange(0,rect[3]-rect[1]+1))
    xx = xx.flatten()
    yy = yy.flatten()

    while diff > thr:
        # compute derivative of I'
        x_ = xv + p[0]
        y_ = yv + p[1]
        # I1_dx = np.reshape(func_I.ev(x_, y_, dx=1), (N, 1))
        # I1_dy = np.reshape(func_I.ev(x_, y_, dy=1), (N, 1))
        #debug
        I1_dx = np.reshape(func_I.ev(y_, x_, dy=1), (N, 1))
        I1_dy = np.reshape(func_I.ev(y_, x_, dx=1), (N, 1))

        # compute A
        A = np.concatenate((I1_dx, I1_dy), axis=1)

        # compute b
        # b = np.reshape(T - func_I.ev(x_, y_), (N, 1))
        #debug
        b = np.reshape(T - func_I.ev(y_, x_), (N, 1))

        # solve delta_p
        tmp = np.linalg.lstsq(A, b, rcond=None)[0]
        tmp = tmp.reshape(-1)
        diff = np.linalg.norm(tmp - delta_p)

        # update delta_p
        delta_p = tmp
        # update p
        p += delta_p

        print('diff',diff)


    return p
