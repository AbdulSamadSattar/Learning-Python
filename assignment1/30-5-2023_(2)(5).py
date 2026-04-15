#Make a script to design a patient information gathering system
i = 0
while 1:
    i += 1
    name = (input("\nEnter Patient's Name: "))
    dob = (input ("Enter Date of Birth(DD/MM/YYYY): "))
    nic = (input ("CNIC No: "))
    ch_name = (input ("Chaperone Name: "))
    gender =(input ("Gender: "))
    a= int(input("Height(in cm): "))
    b = int(input("Weight (in kg): "))
    c = b/(a/100)**2
    m_s= (input("Marital Status: "))
    print ("\n\n\t\t\tPatient's BioData Form")
    print ("\nPatient No:",i , "\t\t\t\t\t\t\t\tDate:4-06-2023")
    print ("Enter Patient's Name:" ,name, "\tEnter Date of Birth:" ,dob, "\t\tCNIC No: " , nic)
    print("Marital Status: " ,m_s, "\t\tChaperone Name:" , ch_name, "\t\t\tGender:" , gender)
    print ("Height:" , a, "\t\t\tWeight:" , b, "\t\t\t\tBMI:" , c)