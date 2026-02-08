# Store employee details in a tuple
employee = (101, "Rahul", "IT")

# Store roles in a set
roles = {"admin", "editor", "viewer"}

# Print employee info using tuple indexing
print("Employee ID:", employee[0])
print("Employee Name:", employee[1])
print("Department:", employee[2])

# Check for admin access using 'in'
if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")
