''' Marquetta Jones
October 24, 2019
Linked List Choice Board: D '''

#class definition for Node
class Node:
    def __init__(self, stuID, lName, fName, major, hours, gpa):
        self.stuID = stuID
        self.lName = lName
        self.fName = fName
        self.major = major
        self.hours = hours
        self.gpa = gpa
        self.link = None

#class definition for LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, stuID, lName, fName, major, hours, gpa):
        temp = Node(stuID, lName, fName, major, hours, gpa)
        if self.head is None:
            self.head = temp
            return
        else:
            current = self.head
            while current.link is not None:
                current = current.link
            current.link = temp

    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            current = self.head
            while current is not None:
                print(current.stuID , " ", current.fName, " ", current.lName, " ", current.major, " ", current.hours, " ", current.gpa, " ")
                current = current.link

    def updateMajor(self, stuID, newMajor):
        if self.head is None:
            print("List has no element")
            return
        else:
            current = self.head
            found = False
            if current.stuID == stuID:
                found = True
            else:
                while current.link is not None:
                    current = current.link
                    if current.stuID == stuID:
                        found = True
                        current.major = newMajor
            if found == False:
                print("Student was not found.")
            else:
                print("The student's major was updated to", newMajor)

    def categorize_students(self):
            freshman = 0
            soph = 0
            junior = 0
            senior = 0
            empty = 0
            if self.head is None:
                print("List has no element")
                return
            else:
                current = self.head
                while current is not None:
                    if current.hours >= 0 and current.hours <= 30:
                        freshman += 1
                    elif current.hours >= 31 and current.hours <= 60:
                        soph += 1
                    elif current.hours >= 61 and current.hours <= 90:
                        junior += 1
                    else:
                        senior += 1
                    current = current.link

            print("Freshmen:" , freshman)
            print("Sophomores:", soph)
            print("Juniors:", junior)
            print("Seniors:", senior)

    def write_to_outfile(self): #not printing to the outfile the students
        freshman = []
        soph = []
        junior = []
        senior = []
        outfile = open('JonesClassifications.txt','w')
        if self.head is None:
            print("List has no element")
            return
        else:
            current = self.head
            while current is not None:
                if current.hours >= 0 and current.hours <= 30:
                    freshman.append(current.fName + " " + current.lName + " - " + current.major)             
                elif current.hours >= 31 and current.hours <= 60:
                    soph.append(current.fName + " " + current.lName + " - " + current.major)
                elif current.hours >= 61 and current.hours <= 90:
                    junior.append(current.fName + " " + current.lName + " - " + current.major)
                else:
                    senior.append(current.fName + " " + current.lName + " - " + current.major)
                current = current.link
                
        outfile.write("Freshman:\n")
        for x in range(len(freshman)):
            outfile.write(freshman[x])
            outfile.write('\n')
        outfile.write("Sophomores:\n")
        for x in range(len(soph)):
            outfile.write(soph[x])
            outfile.write('\n')
        outfile.write("Juniors:\n")
        for x in range(len(junior)):
            outfile.write(junior[x])
            outfile.write('\n')
        outfile.write("Seniors:\n")
        for x in range(len(senior)):
            outfile.write(senior[x])
            outfile.write('\n')

        outfile.close()





        
def main():
    myList = LinkedList()
    
    #test code
    myList.insert_at_end("90", 'Jones', 'Marquetta', 'Comp Sci', 18, 4.0)
    myList.insert_at_end("91", 'Jones', 'Mary', 'Education', 40, 3.87)
    myList.insert_at_end("92", 'Freed', 'Maya', 'Bio', 18, 3.86)
    myList.insert_at_end("93", 'Lucas', 'Lesia', 'Pharm', 36, 3.43)

    #print("List:")
    #myList.traverse_list()

    print("Menu:")
    print("[1] - Add student to database")
    print("[2] - Change a student's major")
    print("[3] - View the list of students")
    print("[4] - Quit")
    answer = input("Choose an option:")
    while answer != '4':
        if answer == '1':
            stuID= input("Student ID?")
            lName = input("Last name?")
            fName = input("First name?")
            major = input("Major?")
            hours = int(input("Number of hours completed?"))
            gpa = float(input("Cumulative GPA?"))
            myList.insert_at_end(stuID, lName, fName, major, hours, gpa)
        elif answer == '2':
            stuID = input("What is the student's ID?")
            newMajor = input("What is the student's new major?")
            myList.updateMajor(stuID, newMajor)
        elif answer == '3':
            myList.traverse_list()
        else:
            print("Invalid input.")
        print("\nMenu:")
        print("[1] - Add student to database")
        print("[2] - Change a student's major")
        print("[3] - View the list of students")
        print("[4] - Quit")
        answer = input("Choose an option:")
        
    print("\nNumber of students in each classification:")
    myList.categorize_students()
    myList.write_to_outfile()

main()
        
        
        
    
                
