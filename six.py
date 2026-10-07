student = {
    "name": "Ananya",
    "roll_no": 101,
    "course": "BCA",
    "marks": 85
}
print("Original Dictionary:", student)

print("Student Name:", student["name"])
print("Course (using get()):", student.get("course"))

student["marks"] = 92
student["email"] = "ananya@jain.edu"
print("After modification/addition:", student)

print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items (Key-Value pairs):", list(student.items()))

if "course" in student:
    print("Key 'course' exists in the dictionary.")

removed_value = student.pop("roll_no")
print(f"Removed Roll No value: {removed_value}")
print("Dictionary after pop:", student)

print("\n--- Iterating through dictionary ---")
for key, value in student.items():
    print(f"{key}: {value}")
