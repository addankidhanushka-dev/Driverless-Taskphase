rows_a = int(input("Enter the number of rows of a: "))
cols_a = int(input("Enter the number of cols of a: "))

rows_b = int(input("Enter the number of rows of b: "))
cols_b = int(input("Enter the number of cols of b: "))

print("Enter the elements of a: ")

A = [list(map(int, input().split())) for _ in range(rows_a)]
B = [list(map(int, input().split())) for _ in range(rows_b)]

matrix_multiply(A, B)



def matrix_multiply(A, B):
    if len(A[0])!= len(B):
        print("Error, matrices are not compatible for multiplication.")
        return

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = 0
            for k in range(len(A[0])):
                s = A[i][k] * B[k][j]
            row.append(s)
        result.append(row)

    print("Resultant matrix: ")
    for r in result:
        print(r)