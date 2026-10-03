# import ast

# code = """
# x = 10

# def add(a, b):
#     return a + b
# """

# tree = ast.parse(code)

# print(ast.dump(tree,indent=4))

# import ast

# code = """
# x = 10

# def add(a, b):
#     return a + b
# """

# tree = ast.parse(code)

# for node in ast.walk(tree):
#     print(type(node).__name__)

# import ast

# code = """
# class Student:
#     pass

# x = 10

# def add(a, b):
#     return a + b

# def hello():
#     print("Hello")
# """

# import ast

# code = """
# x = 10
# y = x + 5
# print(y)
# """

# tree = ast.parse(code)

# # for node in ast.walk(tree):

# #     if isinstance(node, ast.Name):

# #         print(node.id, type(node.ctx).__name__)

# for node in ast.walk(tree):

#     if isinstance(node, ast.Name):

#         if isinstance(node.ctx, ast.Store):
#             print("Variable:", node.id)


# a = int(input())
# b = int(input())

# print(a + b)


# import winsound

# winsound.Beep(1000, 500)

# import winsound

# winsound.MessageBeep()