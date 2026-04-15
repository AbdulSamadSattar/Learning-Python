students = {"111-29":"SArmad","111-30":"Jawad","111-31":"John", "111-32":"Peter"}
students["111-33"] = "Susan" # Add a new item
print("Add item:",students)

students["111-31"]="Cena"
print("\nChange item:",students)

del students["111-31"] # Delete item
print("\nDelete item:",students)

students.popitem()
print("\nPop item:",students)

students.clear()
print(students)