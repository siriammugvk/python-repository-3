

string="StudyTonight"
substring="Stu"

print("Does ",substring," exist in ",string,"?")

# variable to store value returned by find()
v= string.find(substring)
if v>=0:
    print("Yes")
else:
    print("False")