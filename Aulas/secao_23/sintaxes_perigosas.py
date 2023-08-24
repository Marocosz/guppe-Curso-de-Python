"""
Alerta sobre sintaxes perigosas

== -> Usado para chegar valor

is -> Usado para checar se objetos são os mesmos

"""

var1 = 'Marcos'
var2 = 'Marcos'
var3 = var1

# print(var1 is 'Marcos')  # SyntaxWarning: "is" with a literal. Did you mean "=="?
print(var1 is var3)  # True
print(var1 is var2)  # True
print(var1 == var2)  # True
print(var1 == var3)  # True
print(var1 == 'Marcos')  # True
