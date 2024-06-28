import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])

def plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(mandelbrot_image, extent=(xmin, xmax, ymin, ymax))
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()

if __name__ == "__main__":
    # Set the range and size of the plot
    xmin, xmax, ymin, ymax = -2.0, 2.0, -2.0, 2.0
    width, height = 1000, 1000
    max_iter = 256

    # Plot the Mandelbrot set
    plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
