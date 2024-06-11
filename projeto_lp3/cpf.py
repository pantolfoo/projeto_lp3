# validando biblioteca:

from validate_docbr import CPF

cpf  = CPF ()

# metodo para gerar CPF
print(cpf.generate(True))
# ***.***.***-**

print(cpf.generate(False))
# ***********

# True:
print(cpf.validate('518.874.058-36'))
print(cpf.validate('51887405836'))

# False:
print(cpf.validate('518,874,058_36'))
print(cpf.validate('51887400005836'))

