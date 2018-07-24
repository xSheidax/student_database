import json


class Database:

    def __init__(self):
        self.database = {}
        self.database_destination = 'student_database.json'
        self.filter = {
            'filter_id': False,
            'id': 0,
            'filter_name': False,
            'name': '',
            'filter_last_name': False,
            'last_name': '',
            'filter_age': False,
            'age_min': 0,
            'age_max': 0,
            'filter_pesel': True,
            'pesel': ''
        }

        self.load_student_database()

    def show_all_students(self, filter_on):
        filtered_students = {}
        if filter_on:
            for student in self.database:
                idx = False
                name = False
                last_name = False
                age = False
                pesel = False

                ## Filter with student id
                if self.filter['filter_id']:
                    if int(student) == self.filter['id']:
                        idx = True
                else:
                    idx = True

                ## Filter with student name
                if self.filter['filter_name']:
                    equal = False
                    if len(self.database[student]['name']) >= len(self.filter['name']):
                        for name_letter in range(len(self.filter['name'])):
                            if self.filter['name'][int(name_letter)] == self.database[student]['name'][int(name_letter)]:
                                equal = True
                            else:
                                equal = False
                                break
                    if equal:
                        name = True
                    else:
                        name = False
                else:
                    name = True

                ## Filter with student last name
                if self.filter['filter_last_name']:
                    equal = False
                    if len(self.database[student]['lastname']) >= len(self.filter['last_name']):
                        for name_letter in range(len(self.filter['last_name'])):
                            if self.filter['last_name'][int(name_letter)] == self.database[student]['lastname'][int(name_letter)]:
                                equal = True
                            else:
                                equal = False
                                break
                    if equal:
                        last_name = True
                    else:
                        last_name = False
                else:
                    last_name = True

                ## Filter with student age
                if self.filter['filter_age']:
                    if self.filter['age_min'] <= int(self.database[student]['age']) <= self.filter['age_max']:
                        age = True
                    else:
                        age = False
                else:
                    age = True

                ## Filter with student pesel
                if self.filter['filter_pesel']:
                    equal = False
                    if len(self.database[student]['pesel']) >= len(self.filter['pesel']):
                        for pesel_letter in range(len(self.filter['pesel'])):
                            if self.filter['pesel'][int(pesel_letter)] == self.database[student]['pesel'][int(pesel_letter)]:
                                equal = True
                            else:
                                equal = False
                                break
                    if equal:
                        pesel = True
                    else:
                        pesel = False
                else:
                    pesel = True

                if idx and name and last_name and age and pesel:
                    filtered_students[student] = self.database[student]
            print('|ID|', '|NAME|', '|LAST NAME|', '|AGE|', '|PESEL|')
            for student in filtered_students:
                print('|', student, '|', filtered_students[student]['name'], '|', filtered_students[student]['lastname'], '|',
                      filtered_students[student]['age'], '|', filtered_students[student]['pesel'], '|')



        else:
            print('|ID|', '|NAME|', '|LAST NAME|', '|AGE|', '|PESEL|')
            for student in self.database:
                print('|', student, '|', self.database[student]['name'], '|', self.database[student]['lastname'], '|',
                      self.database[student]['age'], '|', self.database[student]['pesel'], '|')

    def create_new_student(self):
        student = {
            'name': '',
            'lastname': '',
            'age': 0,
            'pesel': 0
        }

        student['name'] = input('Insert student name: ')
        student['lastname'] = input('Insert student last name: ')
        student['age'] = input('Insert student age: ')
        student['pesel'] = input('Insert student pesel: ')
        new_id = self.return_new_id()
        self.database[str(new_id)] = student
        self.save_student_database()

    def save_student_database(self):
        database = json.dumps(self.database)
        with open(self.database_destination, 'w') as file:
            file.write(database)

    def load_student_database(self):
        with open(self.database_destination, 'r') as file:
            database = file.read()
        self.database = json.loads(database)

    def modify_student(self, idx):
        try:
            print('Student id: ', idx)
            print('Student name: ', self.database[str(idx)]['name'])
            print('Student last name: ', self.database[str(idx)]['lastname'])
            print('Student age: ', self.database[str(idx)]['age'])
            print('Student pesel: ', self.database[str(idx)]['pesel'])
            print('')
            decision = input('Continue? y/n: ')
            if decision is 'y':
                print('Leave blank if no changes')
                name = input('Insert student name: ')
                last_name = input('Insert student last name: ')
                age = input('Insert student age: ')
                pesel = input('Insert student pesel: ')
                if name is not '':
                    self.database[str(idx)]['name'] = name
                if last_name is not '':
                    self.database[str(idx)]['lastname'] = last_name
                if age is not '':
                    self.database[str(idx)]['age'] = age
                if pesel is not '':
                    self.database[str(idx)]['pesel'] = pesel
                self.save_student_database()
        except KeyError:
            print('Key is not exist!')

    def delete_student(self, idx):
        try:
            print('Student id: ', idx)
            print('Student name: ', self.database[str(idx)]['name'])
            print('Student last name: ', self.database[str(idx)]['lastname'])
            print('Student age: ', self.database[str(idx)]['age'])
            print('Student pesel: ', self.database[str(idx)]['pesel'])
            print('')
            decision = input('Continue? y/n: ')
            if decision is 'y':
                del self.database[str(idx)]
                self.save_student_database()
        except KeyError:
            print('Key is not exist!')

    def return_new_id(self):
        new_id = 0
        for student in self.database:
            new_id += 1

        return new_id+1


db = Database()
db.show_all_students(False)