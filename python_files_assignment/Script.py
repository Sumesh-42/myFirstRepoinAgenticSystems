def read_numbers_from_file(file_name):
    """Read numbers from file and return them as a list."""
    numbers = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()      # handle whitespace
            if line:
                numbers.append(int(line))

    return numbers


def compute_statistics(numbers):
    """Compute statistics and RETURN results (no prints here)."""
    total_count = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / total_count if total_count > 0 else 0

    return total_count, total_sum, average


def log_results(log_file_name, total_count, total_sum, average):
    """Write all logs to file in append mode."""
    with open(log_file_name, 'a') as log_file:
        log_file.write("File opened successfully\n")
        log_file.write(f"Read {total_count} numbers\n")
        log_file.write(f"Sum: {total_sum}\n")
        log_file.write(f"Average: {average}\n")
        log_file.write("Processing completed\n")


def main():
    input_path = r"C:\Users\sumes\Github\myFirstRepoinAgenticSystems\python_files_assignment\numbers.txt"
    log_path = r"C:\Users\sumes\Github\myFirstRepoinAgenticSystems\python_files_assignment\result.log"

    numbers = read_numbers_from_file(input_path)

    total_count, total_sum, average = compute_statistics(numbers)

    log_results(log_path, total_count, total_sum, average)


if __name__ == "__main__":
    main()
