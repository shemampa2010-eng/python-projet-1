needed_to_pass = 50
students_marks = [78,85,92,45,67]
for student_mark in range(len(students_marks)):
 numero_etudiant = student_mark + 1
 note_etudiant = students_marks [student_mark]


# total = sum(students_marks)
# average = total/len(students_marks)
index = 1
Admis_counter = 0
Refuse_counter = 0
for student_mark in students_marks :

 if student_mark < needed_to_pass :
  print ("Studiant" , index , ":", student_mark , "Refuse")
  Admis_counter += 1
 else :
  print("Studiant" , index ,":", student_mark, "Admis" )
  Refuse_counter += 1
index += 1
print ( "Admis", ":" , Admis_counter ,"\nRefuse",":", Refuse_counter)
 