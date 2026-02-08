# User Data Processing System
def calculate_average_score(users):
    average_scores = {}
    for user in users:
        average_scores[user["name"]] = sum(user["scores"]) / len(user["scores"])
    return average_scores

def has_admin_access(roles):
    return "admin" in roles
def main():
    users = [
        {"name": "Alice", "scores": [80, 85, 90, 75], "roles": {"admin", "editor"}},
        {"name": "Bob", "scores": [70, 75, 80, 65], "roles": {"viewer"}},
        {"name": "Charlie", "scores": [90, 95, 85, 80], "roles": {"admin", "viewer"}},
    ]
    
    average_scores = calculate_average_score(users)
    
    for user in users:
        name = user["name"]
        avg_score = average_scores[name]
        admin_access = has_admin_access(user["roles"])
        
        print(f"Name: {name}")
        print(f"Average Score: {avg_score}")
        print(f"Admin Access: {admin_access}\n")
if __name__ == "__main__":
    main()

