import numpy as np
def main():
    # Set a random seed for reproducibility
    np.random.seed(42)

    # Generate a 2D NumPy array representing a dataset
    num_samples = 100
    num_features = 3
    data = np.random.rand(num_samples, num_features)

    # Compute the mean and standard deviation per feature
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)

    # Normalize the dataset using broadcasting
    normalized = (data - mean) / std

    # Slice the normalized array to extract training and test sets
    train_size = int(0.8 * num_samples)
    train_set = normalized[:train_size]
    test_set = normalized[train_size:]

    # Modify a sliced value intentionally to demonstrate view behavior
    original_value = normalized[0, 0]
    train_set[0, 0] += 1  # This will affect the original array

    # Print the results
    print(f"Original data shape: {data.shape}")
    print(f"Mean shape: {mean.shape}")
    print(f"Standard deviation shape: {std.shape}")
    print(f"Training data shape: {train_set.shape}")
    print(f"Test data shape: {test_set.shape}")
    print("Note: Modifying the slice affected the original array")
    print(f"Original value before modification: {original_value}")
    print(f"Original value after modification: {normalized[0, 0]}")
if __name__ == "__main__":    main()
