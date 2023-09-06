import numpy as np
import matplotlib.pyplot as plt
import random
import csv


# FIRST FUNCTION\ Carla Zdravkovic Hugod, August Emil Holm
possibleGrades = [12, 10, 7, 4, 2, 0, -3]

def roundGrade(grades):

    gradesRounded = []

        # Using "try"-command for len(grades) > 1.
    try:
            # For every grade, we compute the absolute value between the grade,
                # and all possible grades. These numbers are stored in newList.
        for x in grades:
            newList = []
            for y in possibleGrades:
                newList.append(abs(x-y))
                # For every newList, we locate the index of the lowest absolute value.
                    # Then we append the grade, in possibleGrades, corresponding to this index, to gradesRounded. 
                        # Assuming grades in the middle of 2 possible grades is rounded up.
            gradesRounded.append(possibleGrades[np.argmin(newList)])
        return gradesRounded
    
        # For len(grades) = 1.
    except:
        newList = []
        for y in possibleGrades:
            newList.append(abs(grades-y))
        gradesRounded.append(possibleGrades[np.argmin(newList)])
            # Making sure we return an integer.
        gradesRounded = gradesRounded[0]
        return gradesRounded

# SECOND FUNCTION\ Bertram Nyvold Larsen, August Emil Holm
def computeFinalGrades(grades):

        # Creating dictionary containing all students.
    students = {}
    for i in range(grades.shape[0]): # iterating per row
        students[i] = grades[i,:] # Pending student in row 0 with grade in corresponding columnn

        # All students with 1 or more assignments graded -3 is given the final grade -3.
    for x in students: # Iterating over each student
        for y in (students[x]): # Iterating over each grade to the corresponding student
            if y == -3:
                students[x] = -3

        # If M = 1, we return every grade as they are. 
    result = []
    if len(students[0]) == 1:
        for i in range(len(students)):
            result.append(int(students[i]))
        gradesFinal = result
        return gradesFinal

        # If M > 1.
    else:
        for i in range(len(students)):
            sumOfGrades = 0
                # Making sure we only deal with students that is not already given the final grade -3.
            if isinstance(students[i], int) == False:
                for k in range(len(students[i])):
                    sumOfGrades += students[i][k]
                    # Lowest grade subtracted from sumOfGrades. Now mean can be calculated.
                mean = (sumOfGrades - min(students[i]))/(len(students[i])-1)
                    # Using the roundGrade function on mean to get the nearest possible grade.
                students[i] = roundGrade(mean)
            # Def gradesFinal as a vector containing all values in the dictionary.
        gradesFinal = [i for i in students.values()]
        return gradesFinal

# THIRD FUNCTION\ Augus Emil Holm, Carla Zdravkovic Hugod
def gradesPlot(grades):

    # // FIRST PLOT
        # Gets list of all given grades
    gradelist = computeFinalGrades(grades)
        # List containing all possible grades as strings
    gradesToPlot = [str(x) for x in possibleGrades]

        # Count number of occurrences for each possible grade
    countlist = []
    for x in possibleGrades:
        countlist.append(gradelist.count(x))

        # Create plot
    y_pos = np.arange(len(gradesToPlot))
    plt.bar(y_pos, countlist, align='center', alpha=0.5)
    plt.xticks(y_pos, gradesToPlot)
    plt.title('Grade distribution')
    plt.xlabel("Possible Grades") # Set the x-axis label
    plt.ylabel("Number of occurrences")
    plt.title("Final Grades per assigment")
    plt.show()


    # // SECOND PLOT
    x = []
    y = []

        # For every assignement (len(M).
    for i in range(grades.shape[1]):
            # We multiply all the grades by a small number and saves them in a list.
        for num in grades[:,i]:
            # "uniform" creates random distance in given interval, between the data points.
            randomNum = random.uniform(-0.1, 0.1)
            y.append(num+randomNum)
            # And the same for the assignment number - just stored in a diffrent list.
        for k in range(grades.shape[0]):
            randomNum = random.uniform(-0.1, 0.1)
            x.append(i+1+randomNum)
        
    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.5)
    ax.set_xlabel('Assignment', fontsize=15)
    ax.set_ylabel('Grade', fontsize=15)
    ax.grid(True)
    ax.set_yticks([-3,0,2,4,7,10,12]) # Specific grades on y-axis.
    ax.set_xticks(range(1,len(grades[0,:])+1)) # Number of assigments on x-axis.
    ax.plot(np.arange(1,len(grades[0,:])+1),np.mean(grades,axis=0)) # Plots mean grade graph
    plt.title("Grades per assigment")
    fig.tight_layout()
    plt.show()

shutprogram = False



    # Main beginning
    # OUTER MAIN SCRIPT. Takes care of loading data\ Carla Zdravkovic Hugod
while True:

    if shutprogram == True:
        break
    

    userinput = input("Welcome to our grading program :D\n"
                      'Please type in the name of a CSV datafile\n'
                      "For example: studentdata.csv\n"
                      ':')

        # Makes sure the datafile is valid, and reads the file
    try:
        with open(userinput) as fin:
            rows = []
            csvin = csv.DictReader(fin)
            for row in csvin:
                row.update((k, v) for k, v in row.items() if k != 'Item')
                rows.append(row)

            # Prints out number of students and assignments
        print()
        print('Congratulations! Your datafile is valid')
        print()
        print('Number of students: '+str(len(rows)))  
        print()  
        print('Number of assignments: '+str(len(rows[0])-2))
        print()

            # Creates matrix containing only the grades for each student (NxM)
        matrix = np.empty(shape=(len(rows), len(rows[0])-2), dtype=int)

        for i in range(len(rows[0])-2):
            string = ['Assignment', str(i+1)]
            matrix[0,i]=rows[0][''.join(string)]
            for k in range(len(rows)-1):
                matrix[k+1,i]=rows[k+1][''.join(string)]
        

            # INNER MAIN SCRIPT\ Bertram Nyvold Larsen
        while True:
            wish = input('Please choose what you want to do by typing the number\n'
                         'corresponding to the action you wish to take:\n'
                         '1. Load new data\n'
                         '2. Check for data errors\n'
                         '3. Generate Plots\n'
                         '4. Display list of grades\n'
                         '5. Quit program\n'
                         'Answer: ')

                # If user want to load new data, we break this inner while true loop.
            if wish == '1':
                break

                # If user want to quit program, we break both while true loops.
            if wish == '5':
                shutprogram = True
                break

                # If the user want to check for data errors:
                    # We compare alle studentIDs with eachother, to see if a studentId
                        # is used more that once. We also check that every grade in the matrix
                            # is also in the possibleGrade list.
            if wish == '2':
                studentID = [rows[i]['StudentID'] for i in range(len(rows))]
                studentIdValid = True
                for i in range(len(studentID)):
                    for k in range(len(studentID)):
                        if i != k:
                            if studentID[i] == studentID[k]:
                                studentIdValid = False
                                print()
                                print('Error: StudentID '+str(rows[i]['StudentID'])+' seen more than once in datafile')
                if studentIdValid == True:
                    print()
                    print('All studentID valid')

                gradesvalid = True
                for x in matrix:
                    for y in x:
                        if y not in possibleGrades:
                            gradesvalid = False
                            print()
                            print('Error. Datafile contains invalid grade: '+str(y))
                if gradesvalid == True:
                    print()
                    print('All grades are valid')
                    print()

                    # Plots.
            if wish == '3':
                gradesPlot(matrix)

            if wish == '4':

                    # Gets list of all student names
                        # Assuming, duplicates are removed from the data, 
                        # before plotting final grade list.
                studentsName = []
                for i in range(len(rows)):
                    studentsName.append(rows[i]['Name']) 

                    # This list will store smaller lists containing the final grade and
                        # the grade for every assignment for every student.
                listOfGradesAndFinalGrades = []

                finalGrades = computeFinalGrades(matrix)

                for i in range(len(rows)):
                    newList34 = []
                    newList34.append(str(finalGrades[i]))
                    newList34.append(str(matrix[i,:].tolist()))
                    listOfGradesAndFinalGrades.append(newList34) 

                        # Creating a dictionary.
                dicts = dict(zip(sorted(studentsName), listOfGradesAndFinalGrades))


                        # This prints out the formatted dictionary.
                print ("{:<20} {:<15} {:<10}".format('Student Name','Final Grade','All grades'))
                for k, v in dicts.items():
                    finalGrade, allGrades = v
                    print ("{:<20} {:<15} {:<10}".format(k,finalGrade,allGrades))

                
    except:
        print('Datafile not valid - try again')
            
       
