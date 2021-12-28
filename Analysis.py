last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
# Create a list called subjects and fill it with the classes you are taking:
subjects =["physics","calculus","poetry","history"]
# Create a list called grades and fill it with your scores:
grades = [98, 97, 85, 88]
# Manually (without any methods) create a two-dimensional list to combine subjects and grades. Use the table below as a reference to associated values.
gradebook = [["physics",	98], ["calculus",	97], ["poetry",	85], ["history",	88]]
print(gradebook)
# Use the .append() method to add a list with the values of "computer science" and an associated grade value of 100
gradebook.append(["computer science", 100])
print(gradebook)
# Use append to add ["visual arts", 93] to gradebook.
gradebook.append(["visual arts", 93])
print(gradebook)
# Access the index of the grade for your visual arts class and modify it to be 5 points greater.
gradebook[-1][-1] = 98
print(gradebook)
# Switch from a numerical grade value to a Pass/Fail option for your poetry class.
gradebook[2].remove(85)
gradebook[2].append("Pass") 
print(gradebook)
# Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook
full_gradebook = last_semester_gradebook  + gradebook
print(full_gradebook)