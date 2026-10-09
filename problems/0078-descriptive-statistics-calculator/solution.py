import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    sum = 0
    length = len(data)
    each_value_count = {}

    for i in range(length):
        sum += data[i]
        if data[i] not in each_value_count:
            each_value_count[data[i]] = 1
        else:
            each_value_count[data[i]] += 1

    mean = (1.0 * sum) /length
    data = sorted(data)
    median = 0
    if length % 2== 0 :

        r = length //2
        sum = data[r-1]+data[r]
        median = sum /2
    else :
        r = length//2 
        median = data[r]

    mode = max(each_value_count, key=each_value_count.get)
    sum = 0
    for i in data:
        sum += (i-mean) ** 2
    
    variance = sum / length

    standard_deviation = variance**0.5
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

    return {
        'mean': round(mean, 4),
        'median': round(median, 4),
        'mode': mode,
        'variance': round(variance, 4),
        'standard_deviation': round(standard_deviation, 4),
        '25th_percentile': q1,
        '50th_percentile': q2,
        '75th_percentile': q3,
        'interquartile_range': iqr
    }    
    
        
