import numpy as np
import scipy.optimize as optimize

def analyze_critical_points(func, start_points):
    results = []
    for point in start_points:
        try:
            result = optimize.minimize(func, point)
            if result.success:
                results.append((result.x, result.fun))
            else:
                raise ValueError('Optimization failed at point: {}'.format(point))
        except Exception as e:
            print(f'Error occurred at {point}: {e}')
            results.append((point, None))
    return results

# Example usage
if __name__ == '__main__':
    obj_func = lambda x: (x - 3) ** 2
    start_pts = [0, 1, 5]
    print(analyze_critical_points(obj_func, start_pts))