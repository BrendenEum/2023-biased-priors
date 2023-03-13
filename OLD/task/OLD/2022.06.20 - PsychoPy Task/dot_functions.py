###################
## This script contains 2 functions and a redefinition of DotStim
###################

from functools import partial

## A function to generate coordinates for the dots using polar coords

def gen_func(bounds):
    
    radius = bounds[0]*np.sqrt(np.random.uniform(low=0, high=1, size=1))
    angle = np.random.uniform(low=0, high=bounds[1], size=1)
    
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    
    return np.array([x,y])

## A function to test if the dots are sufficiently spaced

def test_func(candidate, dots, threshold):

    if len(dots) == 0:
        return True

    distances = np.sqrt(
        np.sum(
            (candidate[np.newaxis, :] - dots) ** 2,
            axis=1
        )
    )

    return np.all(distances > threshold) 

## A function to generate spaced out dots

def generate(
    n_dots, #pssttt, heard you're looking for some dots?
    bounds=[1.0,360.0], #boundary for dots, polar coordinates
    test_func=None, #sqrt of sum of squared distance
    max_iter=10000, #how many iter b4 you quit looking for new candidates
    threshold=0.5 #how far away do all dots need to be from each other?
):

    if test_func is None:

        # default is to return True regardless of the established dots and the
        # current candidate
        test_func = lambda _, __: True

    dots = []

    iteration = 0

    while iteration < max_iter:

        candidate = gen_func(bounds)

        candidate_ok = test_func(candidate, dots, threshold)

        if candidate_ok:
            dots.append(candidate)

        if len(dots) == n_dots:
            break

        iteration += 1

    else:
        raise ValueError("Iteration limit reached")

    dots = np.array(dots)

    return dots