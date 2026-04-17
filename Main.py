#Created by Grant Samon 
#This code will calculate the average and give wether the individual has passed or not

#Calculates average function
#This code will calculate th average of the 3 marks given by the student and then proceeds to divide those marks by 3
def calculate_average(mark1,mark2,mark3):
    #TODO: Calcuate and return average
    return (mark1 + mark2 + mark3) / 3

#Grade Function
#The grade function essentially gives the leaner a grade based on the overall average of the 3 marks that the student inputted
def get_grade(average):
    # A = 75 and above, B = 60 to 74, C = 50 to 59, F below 50 
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

#Pass or Fail Function
#This function checks wether the student passed or failed based on the grade they got and the overall pecentage , you pass if your 
#average is above 50 and fail if its below that number
def check_pass_fail(average): 
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
    
#Display Results Function
#This function displays the results of the given information 
def display_result(name, average, grade, status): 
    print("name: "+name)
    print("average: "+ str(average))
    print("grade: "+grade)
    print("status: "+status)



#Asks user for marks
def main(): 
    num_students = int(input("How many students? ")) 
    for i in range(num_students): 
        print("\nStudent", i + 1) 
        name = input("Enter name: ") 
        mark1 = float(input("Enter mark 1: ")) 
        if mark1 >100:
            print("Mark is out of scope")
            num_students=num_students-1
            
        mark2 = float(input("Enter mark 2: ")) 
        mark3 = float(input("Enter mark 3: ")) 
        
        average = calculate_average(mark1, mark2, mark3)
        grade = get_grade(average) 
        status = check_pass_fail(average)
        display_result(name, average, grade, status)

main()

