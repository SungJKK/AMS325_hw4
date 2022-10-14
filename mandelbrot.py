import warnings

import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt

# suppress warnings
warnings.filterwarnings('ignore')


def mandelbrot(n:int, N_max:int = 50, threshold:int = 50):
    """
    Computes Mandelbrot fractal & saves figure to .png file

        @param n: int = number of points 
        @param N_max: int = max number of Mandelbrot iterations for computation
        @param threshold: int = threshold value determining whether a point is included in the set

        @return mask: numpy.ma.Core.MaskedArray = 
    """

    # Generate n x n grid of (x, y) points
    x = np.linspace(-2, 1, n)
    y = np.linspace(-1.5, 1.5, n)
    x, y = np.meshgrid(x, y, sparse = True, indexing = 'ij')

    # Generate corresponding complex value for the (x, y) points
    c = x + 1j * y

    # Start z from 0 so that the function does not diverge
    z:int = 0
    for _ in range(N_max):
        # function f_c(z) = z^2 + c
        z = np.power(z, 2) + c 

    # Determine whether point (x, y) belongs to the Mandelbrot set if it does not exceed the given threshold
    mask = np.ma.masked_where(abs(z) < threshold, z)

    # Plot the Mandelbrot Fractal graph
    plt.imshow(mask.mask.T, extent = [-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('./mandelbrot.png')

    # Return the masked numpy array
    return mask


if __name__ == '__main__':
    # mandelbrot(100)
    # mandelbrot(300)
    # mandelbrot(500)
    # mandelbrot(600)
    mandelbrot(800)




