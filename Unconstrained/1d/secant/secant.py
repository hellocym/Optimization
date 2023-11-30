# This file contains the implementation of the secant method for finding the
# root of a function.

def secant(f, x0, x1, tol, maxiter):
    """
    This function implements the secant method for finding the root of a
    function.

    Parameters
    ----------
    f : function
        The function whose root is to be found.
    x0 : float
        The first initial guess.
    x1 : float
        The second initial guess.
    tol : float
        The tolerance for the stopping criterion.
    maxiter : int
        The maximum number of iterations.

    Returns
    -------
    x : float
        The root of the function.
    niter : int
        The number of iterations required to reach the root.
    """
    # Initialize the iteration counter.
    niter = 0
    # Initialize the error.
    err = tol + 1
    # Iterate until the stopping criterion is satisfied.
    while err > tol and niter < maxiter:
        # Calculate the next iterate.
        x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        # Update the error.
        err = abs(x - x1)
        # Update the iteration counter.
        niter += 1
        # Update the previous iterates.
        x0 = x1
        x1 = x
    # Return the root and the number of iterations.
    return x, niter