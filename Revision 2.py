#Indi Knighton
#11/12/2014
#Revision 2

name_list = []
finished = False
while not finished:
    student_name = input("Please enter a student name here (-1 to end list): ")
    if student_name == "-1":
        finished = True
    else:
        name_list.append(student_name)
display1 = int(input("Please enter the first number you wish to see here in the list: "))
display2 = int(input("Please enter the second number you wish to see in the list: "))
for index in range(display1, display2):
    print("Name {0} is {1}".format(index + 1, name_list[index]))

