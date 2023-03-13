###################
## This script contains 2 functions and a redefinition of DotStim
###################

from functools import partial

## A function to generate spaced out dots

def generate(
    n_dots,
    gen_func=None,
    test_func=None,
    max_iter=10000
):

    if gen_func is None:

        # default is to return a random location between -1 and 1 for both
        # dimensions
        gen_func = partial(
            np.random.uniform,
            low=-1.0,
            high=1.0,
            size=2
        )

    if test_func is None:

        # default is to return True regardless of the established dots and the
        # current candidate
        test_func = lambda _, __: True

    dots = []

    iteration = 0

    while iteration < max_iter:

        candidate = gen_func()

        candidate_ok = test_func(candidate, dots)

        if candidate_ok:
            dots.append(candidate)

        if len(dots) == n_dots:
            break

        iteration += 1

    else:
        raise ValueError("Iteration limit reached")

    dots = np.array(dots)

    return dots

## A function to test if the dots are sufficiently spaced

def test_func(candidate, dots):

    if len(dots) == 0:
        return True

    distances = np.sqrt(
        np.sum(
            (candidate[np.newaxis, :] - dots) ** 2,
            axis=1
        )
    )

    return np.all(distances > 0.5)

## Re-define how the DotStim function works in the PsychoPy.visual module

gen_func = partial(
    np.random.uniform,
    low=-0.5,
    high=0.5,
    size=2
)

DotStim._newDotsXY = partial(
    generate,
    gen_func=gen_func,
    test_func=test_func
)