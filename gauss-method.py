from sympy import *
x,y,z = symbols('x y z')

AB = Matrix([[-8,2,-3,6], [2,10,14,7], [-2,-5,13,8]])
#B = Matrix([[8,7,-2]])

params = solve_linear_system_LU(AB,[x,y,z])
print("solutions:",params)


# from sympy import Matrix

# A = Matrix([[-8,2,-3], [2,10,14], [-2,-5,13]])
# B = Matrix([8,7,-2])

# params = A.gauss_jordan_solve(B)

# print("Solution:", params)
