import matplotlib.pyplot as plt
import numpy

#given a complex number c, returns the number of iterations until divergence.
def mandelbrot(c, max_iteration):
    z = complex(0,0)
    iterations = 0
    while abs(z) < 4:
        if iterations == max_iteration:
            break
        z = z*z + c
        iterations += 1
    return iterations



if __name__ == '__main__':
    #interesting ranges
    #real = numpy.linspace(-2.25, 0.75, 1000)
    #imag = numpy.linspace(-1.5, 1.5, 1000)
    real = numpy.linspace(-0.22, -0.21, 1000)
    imag = numpy.linspace(-0.70, -0.69, 1000)

    xlen = len(real)
    ylen = len(imag)

    chart = numpy.empty((ylen, xlen))
    for ix in xrange(xlen):
        for iy in xrange(ylen):
            cx = real[ix]
            cy = imag[iy]
            c = complex(cx, cy)
            chart[iy, ix] = mandelbrot(c, 120) #resolution
    plt.figure(figsize=(12,12))
    plt.imshow(chart, interpolation="nearest")
    plt.show()
