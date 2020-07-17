# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("worker.txt", "r", encoding="utf-8") as workers:
    result = []
    people = []
    file = workers.read().split("\n")
    for i in file:
        i = i.split()
        if float(i[1]) < 20000:
            people.append(i[0])
        result.append(float(i[1]))
print(f"Сотрудники с зарплатой меньше 20000р - {people}. "
      f"Средняя зарплата в компании составляет {round(sum(map(float, result)) / len(result))}p")

