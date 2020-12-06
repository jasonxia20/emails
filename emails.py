number = eval(input("how many email adresses are you entering? "))
nop = 0
nos = 0
for i in range(number):
    sop = input("enter email addresses here. if you are a student, end it with @student.college.edu, if you are a professor, end it with @prof.college.edu:")
    if "@student.college.edu" in sop:
        nos += 1
    elif "@prof.college.edu" in sop:
        nop += 1
print("there are ", nos, "students and ", nop, "professors")
