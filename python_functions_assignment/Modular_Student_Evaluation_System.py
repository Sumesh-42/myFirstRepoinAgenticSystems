def greet_student(name):
    """Takes a student's name and returns a formatted greeting."""
    return f"Hello, {name}! Welcome to the evaluation system."

def calculate_scores(scores):
    """
    Takes a list of scores and returns:
    - number of subjects
    - average score
    """
    num_subjects = len(scores)
    average_score = sum(scores) / num_subjects
    return num_subjects, average_score

def evaluate_result(average_score):
    """
    Takes average score and returns:
    - 'Pass' if average >= 50
    - 'Fail' otherwise
    """
    if average_score >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    # Taking input from user (nothing hardcoded inside functions)
    student_name = input("Enter student name: ")

    # Calling greeting function
    greeting = greet_student(student_name)
    print(greeting)

    # Example scores passed as parameter (not inside function logic)
    scores = [70, 65, 80, 85]

    # Calling calculation function
    num_subjects, average_score = calculate_scores(scores)

    # Calling evaluation function
    final_result = evaluate_result(average_score)

    # Clean output in main()
    print("\n--- Student Performance Report ---")
    print("Name:", student_name)
    print("Number of subjects:", num_subjects)
    print("Average score:", average_score)
    print("Final Result:", final_result)

# Start the program
if __name__ == "__main__":
    main()
