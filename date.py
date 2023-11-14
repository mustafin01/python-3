
#ЗАДАНИЕ 2
# @dataclass
# class Book:
#         title: str
#         name: str
#         author: str
#
#
#         def set_title(self):
#                 return self.title
#         def set_name(self):
#                 return self.name
#         def set_author(self):
#                 return self.author
#         def set_title(self, title):
#                 self.title = title
#         def set_name(self, name):
#                 self.name = name
#         def set_author(self, author):
#                 self.author = author
#         def __str__(self):
#                 return f'Book {self.title}'
# a = Book('h', 'g', 'f', 'j')
# print(a.get_title())
# print(a.get_name())
# print(a.get_author())





#ЗАДАНИЕ 3
# class Pet:
#     def init(self):
#         self._name = ''
#         self._animal_type = ''
#         self._age = 0
#
#     def set_name(self):
#         self._name = input("Введите имя своего домашнего животного: ")
#
#     def set_animal_type(self):
#         self._animal_type = input("Введите тип своего домашнего животного: ")
#
#     def set_age(self):
#         self._age = input("Введите возраст своего домашнего животного: ")
#
#     def get_name(self):
#         return self._name
#
#     def get_animal_type(self):
#         return self._animal_type
#
#     def get_age(self):
#         return self._age
#
# pet = Pet()
# pet.set_name()
# pet.set_animal_type()
# pet.set_age()
#
# print("Имя домашнего животного:", pet.get_name())
# print("Тип домашнего животного:", pet.get_animal_type())
# print("Возраст домашнего животного:", pet.get_age())

# ЗАДАНИЕ 4
# class Car:
#     def __init__(self, year_model, rttake):
#         self._year_model = year_model
#         self.rttake = rttake
#         self._speed = 0
#
#
#     def accelerate(self):
#         self._speed += 5
#
#     def brake(self):
#         self._speed -= 5
#
#     def get_speed(self):
#         return self._speed
#
# my_car = Car("2023 Model", "HYU TRX")
# for i in range(5):
#     my_car.accelerate()
#     print(f'Current Speed {my_car.get_speed()}')
#
# for i in range(5):
#     my_car.brake()
#     print(f'Current Speed {my_car.get_speed()}')

#ЗАДАНИЕ 5
# class PersonalInfo:
#
#     def __init__(self, _name, _address, _age, _phone_number):
#         self._age = _age
#         self._name = _name
#         self._address = _address
#         self._phone_number = _phone_number
#
#     def set_name(self, new_name):
#         self._name = new_name
#
#     def set_address(self, new_address):
#         self._address = new_address
#
#     def set_age(self, new_age):
#         self._age = new_age
#
#     def set_phone_number(self, new_phone_number):
#         self._phone_number = new_phone_number
#
#     def get_name(self):
#         return self._name
#
#     def get_phone_number(self):
#         return self._phone_number
#
#     def __str__(self):
#         return f'{self._name, self._address, self._age, self._phone_number}'
#
#
#
# my_info = PersonalInfo("Я", "Минск", 24, "365456436")
# friend1_info = PersonalInfo("Friend1 ", "Москва", 30, "563465")
# friend2_info = PersonalInfo("Friend2 ", "Санкт-Питербург", 28, "5464563536")
#
# print("My Information:")
# print(my_info)
# print("\nFriend 1 Information:")
# print(friend1_info)
# print("\nFriend 2 Information:")
# print(friend2_info)

#ЗАДАНИЕ6
# class Employee:
#     def __init__(self, _name, _number, _department, _post):
#         self._name = _name
#         self._number = _number
#         self._department = _department
#         self._post = _post
#
#     def set_name(self, new_name):
#          self._name = new_name
#
#     def set_number(self, new_number):
#          self._number = new_number
#
#     def set_department(self, new_department):
#          self._department = new_department
#
#     def set_post(self, new_post):
#          self._post = new_post
#
#     def get_name(self):
#          return self._name
#
#     def get_phone_number(self):
#          return self._number
#
#     def __str__(self):
#          return f'{self._name, self._number, self._department, self._post}'
#
#
#
# you_info1 = Employee("Сьюзан Мейерс", "47899", "Бухгалтерия", "Вице-призидент")
# you_info2 = Employee("Марк Джоунс", "39119", "ИТ", "Программист")
# you_info3 = Employee("Джой Роджерс", "81774", "Прозводственный", "Инженер")
#
# print("\nInformation:")
# print(you_info1)
# print("\nInformation:")
# print(you_info2)
# print("\nInformation:")
# print(you_info3)






# #ЗАДАНИЕ 7
# class Employee:
#     def __init__(self, _name, _description, _quantity, _price):
#         self._name = _name
#         self._description = _description
#         self._quantity = _quantity
#         self._price = _price
#
#     def set_name(self, new_name):
#          self._name = new_name
#
#     def set_description(self, new_description):
#          self._description = new_description
#
#     def set_quantity(self, new_quantity):
#          self._quantity = new_quantity
#
#     def set_price(self, new_price):
#          self._price = new_price
#
#     def get_name(self):
#          return self._name
#
#     def get_description(self):
#          return self._description
#
#     def __str__(self):
#          return f'{self._name, self._number, self._quantity, self._price}'
#
#
#
# you_info1 = ("Товар №1", "Пиджак", "12", "59.95")
# you_info2 = ("Товар №2", "Дизайнерские джинсы", "40", "34.95")
# you_info3 = ("Товар №3", "Рубашка", "20", "24.95")
#
# print("\nInformation:")
# print(you_info1)
# print("\nInformation:")
# print(you_info2)
# print("\nInformation:")
# print(you_info3)


#ЗАДАНИЕ8

# class Patient:
#     def __init__(self, first_name, middle_name, last_name, address, city, region, postal_code, phone_number, emergency_contact_name, emergency_contact_phone):
#         self._first_name = first_name
#         self._middle_name = middle_name
#         self._last_name = last_name
#         self._address = address
#         self._city = city
#         self._region = region
#         self._postal_code = postal_code
#         self._phone_number = phone_number
#         self._emergency_contact_name = emergency_contact_name
#         self._emergency_contact_phone = emergency_contact_phone
#
#     def get_first_name(self):
#         return self._first_name
#
#     def get_middle_name(self):
#         return self._middle_name
#
#     def get_last_name(self):
#         return self._last_name
#
#     def get_address(self):
#         return self._address
#
#     def get_city(self):
#         return self._city
#
#     def get_region(self):
#         return self._region
#
#     def get_postal_code(self):
#         return self._postal_code
#
#     def get_phone_number(self):
#         return self._phone_number
#
#     def get_emergency_contact_name(self):
#         return self._emergency_contact_name
#
#     def get_emergency_contact_phone(self):
#         return self._emergency_contact_phone
#
#     # Setter methods for each attribute
#     def set_first_name(self, first_name):
#         self._first_name = first_name
#
#     def set_middle_name(self, middle_name):
#         self._middle_name = middle_name
#
#     def set_last_name(self, last_name):
#         self._last_name = last_name
#
#     def set_address(self, address):
#         self._address = address
#
#     def set_city(self, city):
#         self._city = city
#
#     def set_region(self, region):
#         self._region = region
#
#     def set_postal_code(self, postal_code):
#         self._postal_code = postal_code
#
#     def set_phone_number(self, phone_number):
#         self._phone_number = phone_number
#
#     def set_emergency_contact_name(self, emergency_contact_name):
#         self._emergency_contact_name = emergency_contact_name
#
#     def set_emergency_contact_phone(self, emergency_contact_phone):
#         self._emergency_contact_phone = emergency_contact_phone
#
# class Procedure:
#     def __init__(self, procedure_name, procedure_date, doctor_name, procedure_cost):
#         self._procedure_name = procedure_name
#         self._procedure_date = procedure_date
#         self._doctor_name = doctor_name
#         self._procedure_cost = procedure_cost
#
#
#     def get_procedure_name(self):
#         return self._procedure_name
#
#     def get_procedure_date(self):
#         return self._procedure_date
#
#     def get_doctor_name(self):
#         return self._doctor_name
#
#     def get_procedure_cost(self):
#         return self._procedure_cost
#
#     def set_procedure_name(self, procedure_name):
#         self._procedure_name = procedure_name
#
#     def set_procedure_date(self, procedure_date):
#         self._procedure_date = procedure_date
#
#     def set_doctor_name(self, doctor_name):
#         self._doctor_name = doctor_name
#
#     def set_procedure_cost(self, procedure_cost):
#         self._procedure_cost = procedure_cost
#
#
#
# patient = Patient("Сахбиев", "Марсель", "Рустемович", "Российская Федерация", "Набережные Челны", "Тукаевский район, с.Калмаш, ул.Тукаевская, д.21", "423800", "+7(960) 070-66-25",
#                       "Гульпихнур", "+7(552) 30-48-56")
#
#
# procedure1 = Procedure("Врачебный осмтр", "сегодняшняя", "Ирвин",250.00)
# procedure2 = Procedure("Ренгеноскопия", "сегодняшняя", "Джемисон",500.00)
# procedure3 = Procedure("Анализ крови", "сегодняшняя", "Смит",200.00 )
#
#
# print("Информация о пациенте:")
# print(f"Имя: {patient.get_first_name()} {patient.get_middle_name()} {patient.get_last_name()}")
# print(f"Адрес: {patient.get_address()}, {patient.get_city()}, {patient.get_region()}, {patient.get_postal_code()}")
# print(f"Телефон: {patient.get_phone_number()}")
# print(f"Контакт в чрезвычайной ситуации: {patient.get_emergency_contact_name()}, {patient.get_emergency_contact_phone()}\n")
#
#
# procedures = [procedure1, procedure2, procedure3]
# total_cost = 0
#
# for procedure in procedures:
#     print("Информация о процедуре:")
#     print(f"Процедура: {procedure.get_procedure_name()}")
#     print(f"Дата: {procedure.get_procedure_date()}")
#     print(f"Доктор: {procedure.get_doctor_name()}")
#     print(f"Стоимость: {procedure.get_procedure_cost()} руб.\n")
#
#     total_cost += procedure.get_procedure_cost()
#
#
# print(f"Общая стоимость процедур: {total_cost} руб.")

#ЗАДАНИЕ9

# class Employee:
#     def __init__(self, emp_id, name, department, position):
#         self.emp_id = emp_id
#         self.name = name
#         self.department = department
#         self.position = position
#
#     def __str__(self):
#         return f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Position: {self.position}"
#
#
# def display_menu():
#     print("\nМеню:")
#     print("1. Найти сотрудника")
#     print("2. Добавить сотрудника")
#     print("3. Обновить сотрудника ")
#     print("4. Удалить сотрудника")
#     print("5. Выход")
#
#
# def find_employee(employee_dict, emp_id):
#     if emp_id in employee_dict:
#         print("Сотрудник найден:")
#         print(employee_dict[emp_id])
#     else:
#         print("Сотрудник не найден.")
#
#
# def add_employee(employee_dict):
#     emp_id = int(input("Введите идентификатор сотрудника: "))
#     name = input("Введите имя сотрудника: ")
#     department = input("Войти в отдел сотрудников: ")
#     position = input("Введите должность сотрудника: ")
#
#     new_employee = Employee(emp_id, name, department, position)
#     employee_dict[emp_id] = new_employee
#     print("Сотрудник успешно добавлен.")
#
#
# def update_employee(employee_dict, emp_id):
#     if emp_id in employee_dict:
#         print("Текущая информация о сотрудниках:")
#         print(employee_dict[emp_id])
#
#         name = input("Введите новое имя: ")
#         department = input("Войти в новый отдел: ")
#         position = input("Введите новую должность: ")
#
#         employee_dict[emp_id].name = name
#         employee_dict[emp_id].department = department
#         employee_dict[emp_id].position = position
#
#         print("Информация о сотруднике успешно обновлена.")
#     else:
#         print("Сотрудник не найден.")
#
#
# def delete_employee(employee_dict, emp_id):
#     if emp_id in employee_dict:
#         del employee_dict[emp_id]
#         print("Сотрудник успешно удален.")
#     else:
#         print("Сотрудник не найден.")
#
#
# def main():
#     employees = {}
#
#     while True:
#         display_menu()
#
#         choice = input("Введите свой выбор (1-5): ")
#
#         if choice == "1":
#             emp_id = int(input("Введите идентификатор сотрудника, чтобы найти: "))
#             find_employee(employees, emp_id)
#         elif choice == "2":
#             add_employee(employees)
#         elif choice == "3":
#             emp_id = int(input("Введите идентификатор сотрудника для обновления: "))
#             update_employee(employees, emp_id)
#         elif choice == "4":
#             emp_id = int(input("Введите идентификатор сотрудника для удаления: "))
#             delete_employee(employees, emp_id)
#         elif choice == "5":
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")
#
#
# if __name__ == "__main__":
#     main()

























































































































































































