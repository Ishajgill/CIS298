#
number = 0
some_file = open("number.txt",'w')
while number < 10:
    some_file.write(f"{number}\n")
    number +=1

some_file.close()
some_file_to_read = open('testt.txt')
line = some_file_to_read.readline()
while line:
    print(line,end="")
    line = some_file_to_read.readline()

some_file_to_read.close()
class_name = input("Enter the name of your class")
try:
    gradebook = open(f'{class_name}.txt','w')
    # empty lists to store names,scores
    names =[]
    scores = []
    #individual name = first line
    name = gradebook.readline()
    #while there's a name score = float value
    while name:
        score = float(gradebook.readline())
        names.append(name)
        scores.append(score)
        name = gradebook.readline()

except:
    gradebook = open(f'{class_name}.txt', 'w')
    gradebook.close()
    names =[]
    scores =[]
choice = ""
while choice != '4':
    print("1 - add student")
    print("2 - edit student")
    print("3 - display entire gradebook")
    print("4 - edit")
    print("5 - save input")
    choice = input()
    if choice == '1':
        name = input("Enter the student name")
        score = float(input("Enter the score"))
        names.append(name)
        scores.append(score)
    elif choice == '2':
      print("cant do that yet")
    elif choice == '3':
        for index in range(len(names)):
            print(f'{names[index]} - {scores[index]}')
    elif choice == '4':
    #auto close when done editing here
        with open(f'{class_name}.txt','w') as gradebook:
            for index in range(len(names)):
                gradebook.write(f'{names[index]}\n')
                gradebook.write(f'{scores[index]}\n')







