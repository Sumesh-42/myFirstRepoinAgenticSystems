import pandas as pd
def main():
    # Step 1: Create a sample dataset
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
        "Score": [95, 92, 78, 88, 85, 90, 80],
        "Passed": [True, True, False, True, False, True, False],
        "Category": ["A", "A", "B", "A", "B", "A", "B"]
    }
    df = pd.DataFrame(data)
    # Step 2: Select a single column and print it
    print("Selected 'Name' column:")
    print(df["Name"])
    # Step 3: Select multiple columns and store them in a new DataFrame
    selected_columns = df[["Name", "Score"]]
    print("\nSelected 'Name' and 'Score' columns:")
    print(selected_columns)
    # Step 4: Use iloc to retrieve the first three rows
    print("\nFirst three rows using iloc:")
    print(df.iloc[:3])
    # Step 5: Use loc after setting a meaningful index
    df.set_index("Name", inplace=True)
    print("\nDataset with 'Name' as index:")
    print(df)
    print("\nRetrieve rows for 'Alice' and 'Bob' using loc:")
    print(df.loc[["Alice", "Bob"]])
    # Step 6: Filter rows where Score > 85
    high_scores = df[df["Score"] > 85]
    print("\nRows where Score > 85:")
    print(high_scores)
    # Step 7: Filter rows where Score > 85 and Passed is True
    high_performers = df[(df["Score"] > 85) & (df["Passed"] == True)]
    print("\nHigh-performing students (Score > 85 and Passed is True):")
    print(high_performers)
    # Step 8: Sort the filtered result in descending order of Score
    sorted_high_performers = high_performers.sort_values(by="Score", ascending=False)
    print("\nHigh-performing students sorted by Score (descending):")
    print(sorted_high_performers)
    # Step 9: Chain filtering and sorting operations together
    chained_result = df[(df["Score"] > 85) & (df["Passed"] == True)].sort_values(by="Score", ascending=False)
    print("\nChained filtering and sorting result:")
    print(chained_result)
if __name__ == "__main__":    main()

