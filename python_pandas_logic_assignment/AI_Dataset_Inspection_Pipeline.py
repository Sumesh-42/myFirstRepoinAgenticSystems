import pandas as pd
def main():
    # Step 1: Create a sample dataset and save it as a CSV file
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
        "Age": [25, 30, 35, 40, 45, 50, 55],
        "Score": [85, 90, 78, 92, 88, 95, 80],
        "Label": ["A", "A", "B", "A", "B", "A", "B"]
    }
    df = pd.DataFrame(data)
    df.to_csv("sample_dataset.csv", index=False)
    # Step 2: Load the dataset using pd.read_csv()
    df_loaded = pd.read_csv("sample_dataset.csv")
    # Step 3: Display the first 5 rows (head())
    print("First 5 rows:")
    print(df_loaded.head())
    # Step 4: Display the last 5 rows (tail())
    print("\nLast 5 rows:")
    print(df_loaded.tail())
    # Step 5: Display structural information (info())
    print("\nDataset Info:")
    print(df_loaded.info())
    # Step 6: Display summary statistics (describe())
    print("\nSummary Statistics:")
    print(df_loaded.describe())
    # Step 7: Select a single column and store it in a variable
    age_column = df_loaded["Age"]
    print("\nSelected 'Age' column:")
    print(age_column)
    # Step 8: Select multiple columns and store them in a new DataFrame
    selected_columns = df_loaded[["Name", "Score"]]
    print("\nSelected 'Name' and 'Score' columns:")
    print(selected_columns)
    # Step 9: Filter rows based on a numerical condition (Score > 80)
    filtered_rows = df_loaded[df_loaded["Score"] > 80]
    print("\nFiltered rows (Score > 80):")
    print(filtered_rows)
if __name__ == "__main__":    main()    
