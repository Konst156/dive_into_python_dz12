# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.


import csv


class Student:

    def __init__(self, name, subjects_file):
        self.name = name
        self.validate_name(name)

        self.subjects = self.load_subjects(subjects_file)
        self.marks = {}
        self.tests = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def validate_name(self, name):
        if not name[0].isupper() or not name.isalpha():
            raise ValueError("Имя должно начинаться с заглавной буквы и состоять только из букв")

    def load_subjects(self, file):
        subjects = []
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                subjects.append(row[0])
        return subjects

    def add_mark(self, subject, mark):
        if mark < 2 or mark > 5 or subject not in self.subjects:
            raise ValueError("Недопустимые предмет или оценка")
        self.marks[subject] = self.marks.get(subject, []) + [mark]

    def add_test(self, subject, result):
        if result < 0 or result > 100 or subject not in self.subjects:
            raise ValueError("Недопустимые предмет или результат теста")
        self.tests[subject] = self.tests.get(subject, []) + [result]

    def average_test(self, subject):
        results = self.tests.get(subject, [])
        return sum(results) / len(results) if results else 0

    def average_mark(self):
        marks = []
        for mark_list in self.marks.values():
            marks.extend(mark_list)
        return sum(marks) / len(marks)


student = Student("Ivan", "subjects.csv")

# Добавляем оценки
student.add_mark("Math", 4)
student.add_mark("Physics", 5)

# Добавляем результаты тестов
student.add_test("Math", 80)
student.add_test("Physics", 90)

# Выводим средний балл по предметам
print(student.average_test("Math"))  # 80
print(student.average_test("Physics"))  # 90

# Выводим средний балл по всем оценкам
print(student.average_mark())  # 4.5
