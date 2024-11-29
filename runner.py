import sys
import os

# Додаємо всі підкаталоги проекту до sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
for root, dirs, files in os.walk(project_root):
    if '__pycache__' not in root:  # Виключаємо кешовані файли
        sys.path.append(root)

# Імпортуємо основні функції кожної лабораторної роботи
from lab1.runner1 import main as run_lab1
from lab2.runner2 import main as run_lab2   
from lab3.runner3 import main as run_lab3
from lab4.runner4 import main as run_lab4
from lab5.runner5 import main as run_lab5
from lab6.runner6 import main as run_lab6
from lab7.runner7 import main as run_lab7
from lab8.runner8 import main as run_lab8

class LabFacade:
    """Фасадний клас для запуску лабораторних робіт."""
    
    def __init__(self):
        self.lab_runners = {
            "1": run_lab1,
            "2": run_lab2,
            "3": run_lab3,
            "4": run_lab4,
            "5": run_lab5,
            "6": run_lab6,
            "7": run_lab7,
            "8": run_lab8
        }
    
    def run_lab(self, lab_number):
        """Запуск відповідної лабораторної роботи на основі вибраного номера."""
        if lab_number in self.lab_runners:
            print(f"Запуск лабораторної роботи №{lab_number}...")
            self.lab_runners[lab_number]()  # Запускаємо обрану лабораторну роботу
        else:
            print("Невірний номер лабораторної роботи. Спробуйте ще раз.")

def main():
    facade = LabFacade()
    
    while True:
        print("\nМеню запуску лабораторних робіт:")
        for i in range(1, 9):
            print(f"{i} - Лабораторна робота {i}")
        print("0 - Вийти")

        choice = input("Виберіть номер лабораторної роботи для запуску або 0 для виходу: ")
        
        if choice == "0":
            print("Вихід з програми.")
            break
        else:
            facade.run_lab(choice)

if __name__ == "__main__":
    main()
