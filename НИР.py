from pandas import read_excel
from statistics import mean

# disciplinesInfo = (
# 	('АЯиП (Лаб)', 2.5),
# 	('ВМ (Упр)', 5),
# 	('Ин.яз. (Упр)', 1.5),
# 	('Информатика (Упр)', 1),
# 	('Информатика (Лаб)', 1),
# 	('История РФ (Упр)', 1.5),
# 	('МЛТА (Упр)', 4),
# 	('МЛТА (Лаб)', 1),
# 	('ПРвСИИ (Упр)', 1),
# 	('РТДвПД (Лаб)', 1),
# 	('Физика (Упр)', 1),
# 	('Физика (Лаб)', 4),
# 	('Физ-ра (Упр)', 1.5),
# 	('ВвПД (Лек)', 1),
# )
# disciplinesWeight = sum(j for i, j in disciplinesInfo)
#
# class Student:
# 	def __init__(self, fullName: str, birthday: str, stipend: str, examMarks: list[int], *semesterMarks):
# 		self.fullName = fullName
# 		self.birthday = birthday
# 		self.stipend = stipend
# 		self.examMarks = examMarks
# 		self.semesterMarks = semesterMarks
#
# 		for discipline, weight in disciplinesInfo:
#
#
# 		self.examsCount = len(examMarks)
# 		self.semestersCount = len(semesterMarks)
#
# 	def __str__(self):
# 		return f'{self.fullName}: {self.examMarks}'

excel = {}
for row in list(read_excel(r'C:\Users\Роман\OneDrive\Документы\546_НИР.xlsx', header = None).fillna(0).itertuples(index = False))[1:31]:
	excel[row[0]] = row[1:14], row[14:27], row[27:-6], row[-6:-2], row[-2], row[-1]

# disciplines = (
# 	('АЯиП (Лаб)', 4),
# 	('ВМ (Упр)', 5),
# 	('Ин.яз. (Упр)', 3),
# 	('Информатика (Упр)', 1),
# 	('Информатика (Лаб)', 1),
# 	('История РФ (Упр)', 2),
# 	('МЛТА (Упр)', 5),
# 	('МЛТА (Лаб)', 5),
# 	('ПРвСИИ (Упр)', 1),
# 	('РТДвПД (Лаб)', 1),
# 	('Физика (Упр)', 5),
# 	('Физика (Лаб)', 5),
# 	('Физ-ра (Упр)', 3),
# 	('ВвПД (Лек)', 1),
# )

# disciplines = (
# 	('АЯиП (Лаб)', 1),
# 	('ВМ (Упр)', 1),
# 	('Ин.яз. (Упр)', 1),
# 	('Информатика (Упр)', 1),
# 	('Информатика (Лаб)', 1),
# 	('История РФ (Упр)', 1),
# 	('МЛТА (Упр)', 1),
# 	('МЛТА (Лаб)', 1),
# 	('ПРвСИИ (Упр)', 1),
# 	('РТДвПД (Лаб)', 1),
# 	('Физика (Упр)', 1),
# 	('Физика (Лаб)', 1),
# 	('Физ-ра (Упр)', 1),
# 	('ВвПД (Лек)', 1),
# )

disciplines = (
	('АЯиП (Лаб)', 2.5),
	('ВМ (Упр)', 5),
	('Ин.яз. (Упр)', 1.5),
	('Информатика (Упр)', 0.5),
	('Информатика (Лаб)', 0.5),
	('История РФ (Упр)', 1.5),
	('МЛТА (Упр)', 4),
	('МЛТА (Лаб)', 1),
	('ПРвСИИ (Упр)', 1),
	('РТДвПД (Лаб)', 1),
	('Физика (Упр)', 1),
	('Физика (Лаб)', 4),
	('Физ-ра (Упр)', 1.5),
	('ВвПД (Лек)', 1),
)
disciplinesWeight = sum(j for i, j in disciplines)

formedExcel = {}
for key in excel:
	studentInfo = excel[key]

	s = 0
	for mark in range(13):
		s += (studentInfo[0][mark] + studentInfo[1][mark] + studentInfo[2][mark]) * disciplines[mark][1]
	s += 2 + studentInfo[2][-1]

	formedExcel[key] = (s, studentInfo[3], studentInfo[4], studentInfo[5])

months = {
	'января': [],
	'февраля': [],
	'марта': [],
	'апреля': [],
	'мая': [],
	'июня': [],
	'июля': [],
	'августа': [],
	'сентября': [],
	'октября': [],
	'ноября': [],
	'декабря': [],
	'тест': []
}
contrlSum, examsSum = 0, 0
for key in formedExcel:
	a, e = [3, 3, 3, 1], 0
	for i in range(len(a)):
		e += formedExcel[key][1][i] * a[i]

	contrl = formedExcel[key][0] / disciplinesWeight
	exams = e / 10

	contrlSum += contrl
	examsSum += exams

	month = formedExcel[key][3].split()[1]
	months[month].append((contrl + exams) / 2)

	print(f'{key:<30}: ср.оц. {contrl:.3f} -> {exams}\t\tмаржа (погрешность) {exams - contrl:.3f}\t\tстипуха {'Да' if contrl >= 4 else 'Нет'} -> {formedExcel[key][2]}')

print(f'\nСравнение средних баллов всей группы: {contrlSum / 30:.2f} -> {examsSum / 30:.2f}\n')

# оценка модели как ложно-позитивные и ложно-негативные (также совпадающие) как уровень точности между собой, разбивка на 4 кластера