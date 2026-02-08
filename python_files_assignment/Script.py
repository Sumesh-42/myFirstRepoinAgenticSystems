def read_numbers_from_file(file_name):
    with open(file_name, 'r') as file:
        print("File opened successfully")
        numbers = [int(line.strip()) for line in file]
        print(f"Read {len(numbers)} numbers")
    return numbers

def compute_statistics(numbers):
    total_count = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / total_count if total_count > 0 else 0
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    return total_count, total_sum, average

def log_results(file_name, total_count, total_sum, average):
    with open(file_name, 'a') as log_file:
        log_file.write("File opened successfully\n")
        log_file.write(f"Read {total_count} numbers\n")
        log_file.write(f"Sum: {total_sum}\n")
        log_file.write(f"Average: {average}\n")
        log_file.write("Processing completed\n")

def main():
    numbers = read_numbers_from_file('C:\\Users\\sumes\\Github\\myFirstRepoinAgenticSystems\\python_files_assignment\\numbers.txt')
    total_count, total_sum, average = compute_statistics(numbers)
    log_results('C:\\Users\\sumes\\Github\\myFirstRepoinAgenticSystems\\python_files_assignment\\result.log', total_count, total_sum, average)
    
if __name__ == "__main__":
    main()







