1) 
def count_vc(input_string):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    num_vowels = sum(1 for char in input_string if char in vowels)
    num_consonants = sum(1 for char in input_string if char in consonants)
    
    return num_vowels, num_consonants

user_input = input("Enter a string: ")
vowel_count, consonant_count = count_vc(user_input)

print(f"No of vowels: {vowel_count}")
print(f"No of consonants: {consonant_count}")


2)

def input_matrix(name):
    rows = int(input(f"Enter the number of rows for matrix {name}: "))
    cols = int(input(f"Enter the number of columns for matrix {name}: "))
    matrix = []

    print(f"Enter the elements of matrix {name}, row by row, each row's elements separated by spaces:")
    for i in range(rows):
        while True:
            row = input(f"Row {i+1}: ").split()
            if len(row) != cols:
                print(f"Error: Row {i+1} does not have {cols} columns. Please enter again.")
            else:
                matrix.append(list(map(int, row)))
                break

    return matrix

def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        return "Error: Matrices cannot be multiplied due to incompatible dimensions."

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

try:
    A = input_matrix('A')
    B = input_matrix('B')
    result = multiply_matrices(A, B)

    if isinstance(result, str):
        print(result)
    else:
        print("The product of the matrices is:")
        print_matrix(result)
except ValueError as e:
    print(e)

3)

def common(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
    
    common_elements = set1.intersection(set2)
    
    return len(common_elements)

list1 = list(map(int, input("Enter the elements of the first list:").split()))
list2 = list(map(int, input("Enter the elements of the second list:").split()))

num_common_elements = common(list1, list2)

print(f"The number of common elements between the two lists is: {num_common_elements}")


4)

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []

    print("Enter the elements row by row:")
    
    for i in range(rows):
        while True:
            row = input(f"Row {i+1}: ").split()
            if len(row) != cols:
                print(f"Error: Row {i+1} does not have {cols} columns. Please enter again.")
            else:
                matrix.append(list(map(int, row)))
                break
    
    return matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

matrix = input_matrix()
transpose = transpose_matrix(matrix)

print("The transpose of the matrix is:")
print_matrix(transpose)
