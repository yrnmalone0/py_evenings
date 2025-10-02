'''
Local vs Global Scope Instruction:

Define a variable with the same name in both global and local scopes within a function.
Print the variable from inside the function and outside the function, observing how Python accesses each variable based on its scope (local vs global).
'''

global_var = "global variable"

def scope_function():
    #global_var = "local variable copy"
    #local_var = "local variable"
    print(global_var)

scope_function()
print(global_var)