# Creating a sample data array
data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]

# Calculate mean
def calculate_mean(arr):
    total_sum = sum(arr)
    count = len(arr)
    mean_value = total_sum / count
    return mean_value

# Calculate median
def calculate_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    mid = n // 2
    if n % 2 == 0:
        median_value = (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:
        median_value = sorted_arr[mid]
    return median_value

# Calculate mode
def calculate_mode(arr):
    frequency = {}
    for item in arr:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_frequency = max(frequency.values())
    mode_value = [key for key, value in frequency.items() if value == max_frequency]
    return mode_value

# Calculate variance
def calculate_variance(arr):
    mean_value = calculate_mean(arr)
    variance_sum = sum((x - mean_value) ** 2 for x in arr)
    variance = variance_sum / len(arr)
    return variance

# Calculate standard deviation
def calculate_standard_deviation(arr):
    variance = calculate_variance(arr)
    standard_deviation = variance ** 0.5
    return standard_deviation

# Display results
mean = calculate_mean(data)
median = calculate_median(data)
mode = calculate_mode(data)
variance = calculate_variance(data)
standard_deviation = calculate_standard_deviation(data)

print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
