class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

  def __repr__(self):
    return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"


def sort_students(student_list):
  # Use the sorted function to sort the list based on CGPA in descending order
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Example usage:
students = [
    Student("Aswin", "101", 3.8),
    Student("Jijo", "102", 3.9),
    Student("Serjin", "103", 3.5),
    Student("Akhino", "104", 3.7),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(
      student.name, student.roll_number,
      student.cgpa))  # Print each student object in the sorted list
