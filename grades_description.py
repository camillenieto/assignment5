#Program 1: PUP Grading System\

def grade_percentage(grade) :
    if grade>=97 and grade<=100 :
        return "Grade/Mark: 1.0 Description: Excellent"
    else:
        if grade>=94 and grade<=96:
            return "Grade/Mark: 1.25 Description: Excellent"
        else:
            if grade>=91 and grade<=93:
                return "Grade/Mark: 1.5 Description: Very Good"
            else:
                if grade>=88 and grade>=90:
                    return "Grade/Mark: 1.75 Description: Very Good"
                else:
                    if grade>=85 and grade<=87:
                        return "Grade/Mark: 2.0 Descripton: Good"
                    else:
                        if grade>=82 and grade<=84:
                            return "Grade/Mark: 2.25 Description: Good"
                        else:
                            if grade>=79 and grade<=81:
                                return "Grade/Mark: 2.5 Description: Satisfactory"
                            else:
                                if grade>=76 and grade<=78:
                                    return "Grade/Mark: 2.75 Description: Satisfactory"
                                else:
                                    if grade==75 :
                                        return "Grade/Mark: 3.0 Description: Passing"
                                    else:
                                        if grade>=65 and grade<=74:
                                            return "Grade/Mark: 5.0 Decription: Failure"
                                        else:
                                            return "Grade/Mark: Inc. Decription: Incomplete"
                                            
#steps
#1.ask for grade percentage. 
grade_func = round(float(input("Input grade: ")))
#2.display the equivalent Grade/Mark and Description
print(grade_percentage(grade_func))
                   
        


