import asgn_13_8 as asgn
import gpacalc as gpa

print('Marksheet Generator')
print('Made by: A.Samad & Talha')

while 1:
    print('for log in system press:\'enter\'' )
    choice = input("press enter to continue")
    if choice == '':
        asgn.admin()
    if choice == '2':
        gpa.gpa()
    else:
        print('invlaid choice')