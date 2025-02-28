import numpy as np
import matplotlib.pyplot as plt

def plot_polynomial_functions(functions, x_range=(-5, 5), num_points=100, labels=None):
    """Plots multiple polynomial functions with shifts and custom labels.

    Args:
        functions: A list of polynomial functions (lambda functions).
        x_range: A tuple specifying the range of x-values to plot.
        num_points: The number of points to use for plotting.
        labels: A list of custom labels for each function. If None, 
                defaults to '<lambda>'.
    """

    fig, ax = plt.subplots(figsize=(8,6))

    x = np.linspace(x_range[0], x_range[1], num_points)

    for i, function in enumerate(functions):
        y = function(x)
        label = labels[i] if labels else function.__name__  # Use custom label or default
        plt.plot(x, y, label=label)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Polynomial Functions')
    ax.legend()
    ax.grid(True)
    plt.show()

def is_even_odd_or_neither(func, x_range=(-5, 5), num_points=100):
  """
  Determines if a function is even, odd, or neither.

  Args:
    func: The function to be evaluated.
    x_range: A tuple specifying the range of x-values to consider.
    num_points: The number of points to use for evaluation.

  Returns:
    A string indicating whether the function is 'even', 'odd', or 'neither'.
  """

  x = np.linspace(x_range[0], x_range[1], num_points)

  # Check for even function: f(-x) = f(x)
  is_even = np.allclose(func(-x), func(x))

  # Check for odd function: f(-x) = -f(x)
  is_odd = np.allclose(func(-x), -func(x))

  if is_even:
    return 'even'
  elif is_odd:
    return 'odd'
  else:
    return 'neither'

