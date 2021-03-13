student1 = {} 
   
name = input("Please enter your name:")
midtermGrade = int(input("Please enter your midterm grade: "))
projectGrade = int(input("Please enter your project grade: "))
finalGrade = int(input("Please enter your final grade: "))
coursePassingGrade = (midtermGrade * 0.3) + (projectGrade * 0.3) + (finalGrade * 0.4)

student1.update({
   
      "name" : name,
      "midtermGrade" : midtermGrade,
      "projectGrade" : projectGrade,
      "finalGrade" : finalGrade,
      "coursePassingGrade" : coursePassingGrade
                                          
})

student2 = {} 
   
name = input("Please enter your name:")
midtermGrade = int(input("Please enter your midterm grade: "))
projectGrade = int(input("Please enter your project grade: "))
finalGrade = int(input("Please enter your final grade: "))
coursePassingGrade = (midtermGrade * 0.3) + (projectGrade * 0.3) + (finalGrade * 0.4)

student2.update({
   
      "name" : name,
      "midtermGrade" : midtermGrade,
      "projectGrade" : projectGrade,
      "finalGrade" : finalGrade,
      "coursePassingGrade" : coursePassingGrade
                                          
})

student3 = {} 
   
name = input("Please enter your name:")
midtermGrade = int(input("Please enter your midterm grade: "))
projectGrade = int(input("Please enter your project grade: "))
finalGrade = int(input("Please enter your final grade: "))
coursePassingGrade = (midtermGrade * 0.3) + (projectGrade * 0.3) + (finalGrade * 0.4)

student3.update({
   
      "name" : name,
      "midtermGrade" : midtermGrade,
      "projectGrade" : projectGrade,
      "finalGrade" : finalGrade,
      "coursePassingGrade" : coursePassingGrade
                                          
})

student4 = {} 
   
name = input("Please enter your name:")
midtermGrade = int(input("Please enter your midterm grade: "))
projectGrade = int(input("Please enter your project grade: "))
finalGrade = int(input("Please enter your final grade: "))
coursePassingGrade = (midtermGrade * 0.3) + (projectGrade * 0.3) + (finalGrade * 0.4)

student4.update({
   
      "name" : name,
      "midtermGrade" : midtermGrade,
      "projectGrade" : projectGrade,
      "finalGrade" : finalGrade,
      "coursePassingGrade" : coursePassingGrade
                                          
})

student5 = {} 
   
name = input("Please enter your name:")
midtermGrade = int(input("Please enter your midterm grade: "))
projectGrade = int(input("Please enter your project grade: "))
finalGrade = int(input("Please enter your final grade: "))
coursePassingGrade = (midtermGrade * 0.3) + (projectGrade * 0.3) + (finalGrade * 0.4)

student5.update({
   
      "name" : name,
      "midtermGrade" : midtermGrade,
      "projectGrade" : projectGrade,
      "finalGrade" : finalGrade,
      "coursePassingGrade" : coursePassingGrade
                                          
})



coursePassingGrades = [student1["coursePassingGrade"], student2["coursePassingGrade"], student3["coursePassingGrade"], student4["coursePassingGrade"], student5["coursePassingGrade"]]
coursePassingGrades.sort()
print(coursePassingGrades[::-1])










   
  