import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    len_g_coeffs = len(g_coeffs)
    len_h_coeffs = len(h_coeffs)

    highest_power_of_g = len_g_coeffs -1
    highest_power_of_h = len_h_coeffs - 1

    g = 0 

    for i in range(len_g_coeffs):
        g += g_coeffs[i]*(x**(highest_power_of_g - i))
    
    h = 0
    for i in range(len_h_coeffs):
        h += h_coeffs[i]*(x**(highest_power_of_h - i))

    g_bar = 0
    
    for i in range(highest_power_of_g):
        
        g_bar += (highest_power_of_g-i)*g_coeffs[i]*(x**(highest_power_of_g-i-1)) 
    
    h_bar = 0
    for i in range(highest_power_of_h):
        
        h_bar += (highest_power_of_h-i)*h_coeffs[i]*(x**(highest_power_of_h-i-1)) 

    answer = ((h*g_bar)-(g*h_bar))/(h*h)

    return answer
    