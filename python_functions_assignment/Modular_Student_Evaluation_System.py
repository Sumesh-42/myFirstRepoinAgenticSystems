def greet_student(name):
    """Takes a student's name and returns a formatted greeting."""
    return f"Hello, {name}! Welcome to the evaluation system."

def calculate_scores(scores):
    """Takes a list of scores and returns number of subjects and average."""
    num_subjects = len(scores)
    average_score = sum(scores) / num_subjects
    return num_subjects, average_score

def evaluate_result(average_score):
    """Returns Pass or Fail based on average score."""
    if average_score >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    # Taking student name input
    student_name = input("Enter student name: ")
    print(greet_student(student_name))

    # Example scores (you can change these)
    scores = [70, 65, 80, 85]

    # Calling score calculation function
    num_subjects, average_score = calculate_scores(scores)

    # Calling evaluation function
    final_result = evaluate_result(average_score)

    # Clean formatted output
    print("\n--- Student Performance Report ---")
    print("Name:", student_name)
    print("Number of subjects:", num_subjects)
    print("Average score:", average_score)
    print("Final Result:", final_result)

# Run the program
if __name__ == "__main__":
    main()
