import numpy as np
def main():
    # Create a NumPy array representing numeric data
    data = np.array([10, 20, 30, 40])

    # Compute mean and standard deviation
    mean = np.mean(data)
    std = np.std(data)

    # Normalize the data
    normalized = (data - mean) / std

    # Reshape the normalized data into a 2D array
    reshaped = normalized.reshape(2, 2)

    # Print results
    print(f"Original data: {data}")
    print(f"Mean: {mean:.2f}")
    print(f"Standard Deviation: {std:.2f}")
    print(f"Normalized data: {normalized}")
    print(f"Reshaped data:\n{reshaped}\nReshaped data shape: {reshaped.shape}")
if __name__ == "__main__":    main()