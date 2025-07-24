A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}  
C = {5, 6, 7, 8, 9}
D = {1, 3, 7, 9, 10}
result=(A&B)^(A&C)^(A&D)^(B&C)^(B&D)^(C&D)^(A&B&C)^(A&B&D)^(B&C&D)
print(f"Elements in exactly 2 sets: {result}")