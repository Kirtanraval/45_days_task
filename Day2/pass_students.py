Students = {
    "Alice": 85,
    "Bob": 58,
    "Charlie": 92,
    "David": 45,
    "Eve": 76
}
for student in Students:
    if Students[student] >= 60:
        print(f"{student} has passed with a score of {Students[student]}")
    else:
        print(f"{student} has failed with a score of {Students[student]}")


marks = [78, 45, 62, 89, 55, 90, 33, 76]
for mark in marks:
    if mark >= 60:
        print(f"Mark {mark} is a passing score.")
    else:
        print(f"Mark {mark} is a failing score.")