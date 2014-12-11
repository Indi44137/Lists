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
view = input("Please enter the numbers on the list you would wish to see: ")
for index in range(len(name_list[view])):
    print("Name {0} is {1}".format(index + 1, name_list[index]))
