"""
Работа №13 (Доп.) - Вариант 16 - Множества
- Вычислить: (¬(A ⋃ B) ⊕ C) - (D ⋃ C), при:
	- A = {'a', 1, 7, 'c'};
	- B = {1, 2, 3, 4};
	- C = {'a', 'b', 'c'};
	- D = {2, 3, 'b'};
	- Omega = {'a', 'b', 'c', 1, 2, 3, 4, 5, 6, 7}.
"""

A = {'a', 1, 7, 'c'}
B = {1, 2, 3, 4}
C = {'a', 'b', 'c'}
D = {2, 3, 'b'}
Omega = {'a', 'b', 'c', 1, 2, 3, 4, 5, 6, 7}

# print(((Omega - (A | B)) ^ C) - (D | C))
print(Omega.difference(A.union(B)).symmetric_difference(C).difference(D.union(C)))