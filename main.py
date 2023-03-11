class Solution:
  def generate(self, numRows: int) -> list[list[int]]: # akes an integer numRows as input and returns a list of lists of integers.
    triangle = [] # The variable triangle is initialized as an empty list.
    for row_num in range(numRows): #A for loop is used to iterate through each row of the triangle.
      row = [None for _ in range(row_num+1)] #A new list is created for each row with None as its elements.
      row[0], row[-1] = 1, 1 # The first and last elements of the row are set to 1.
      for j in range(1, len(row)-1):# Another for loop is used to iterate through the elements of the row, except the first and the last elements.
         row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]# The elements are set to the sum of the corresponding elements in the previous row of the triangle.
         triangle.append(row) #The row is then appended to the triangle.
    return triangle

# Take user input for numRows
numRows = int(input("Enter the number of rows to generate in Pascal's triangle: "))

# Create an instance of the Solution class and call the generate() method
sol = Solution()
pascal_triangle = sol.generate(numRows)

# Display the Pascal's triangle
print("Pascal's Triangle:")
for row in pascal_triangle:
    print(row)

# Take user input for i and j
i, j = map(int, input("Enter the row and column indices to get the corresponding value: ").split())

# Display the corresponding value at the given indices
print(f"Value at ({i}, {j}) = {pascal_triangle[i-1][j-1]}")
