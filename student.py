class Student:
    amount_of_students = 0
    height = 160

    def __init__(self, height=200, name='Oleg', money=0, homework=5):
        self.name = name
        self.height = height
        self.money = money
        self.homework = homework
        Student.amount_of_students += 1

    def printer(self):
        print(self.height)

    def earn(self, job):
        if job == True:
            select = input('Do you wanna work?("y"/"n") ')
            if select == 'Y' or select == 'y':
                self.money += 10
                print(self.money)
                if self.money <= 0:
                    print('You need to go to work!')
            elif select == 'N' or select == 'n':
                self.money -= 5
                print(self.money)
                if self.money <= 0:
                    print('You need to go to work!')

    def study(self, do_homework):
        if do_homework == True:
            select = input('Do you have homework to do?("y"/"n") ')
            if select == 'Y' or select == 'y':
                select1 = input('Are you gonna do your homework?("y"/"n") ')
                if select1 == 'Y' or select == 'y':
                    if self.homework > 0:
                        self.homework -= 1
                        print(self.homework)
                    if self.homework == 0:
                        print('You dont have any homework to do!')
                elif select1 == 'N' or select == 'n':
                    print('Okay. But you need to do it later.')
                    self.homework += 1
            elif select == 'N' or select == 'n':
                if self.homework > 0:
                    print("You're a liar. You have homework to do.")
                if self.homework == 0:
                    print('Cool!You can rest now.')


stud1 = Student()
stud1.printer()
print(Student.height)
while True:
    stud1.earn(True)
    stud1.study(True)
