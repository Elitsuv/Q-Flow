def get_data():
    return input("Enter Name: ")

name = get_data()
while True:  
    try:
      age = int(input("Enter age: "))
      break  
    except ValueError:
      print("Invalid age. Please enter a number.")

issue = input("Enter the patient problem: ")

patient_data = {"name": name, "age": age, "issue": issue}
print(patient_data)