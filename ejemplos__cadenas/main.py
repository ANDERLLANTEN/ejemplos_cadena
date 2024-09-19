
# combinar dos cadenas
text1 = "fundamentos con"
text2 = " python"
result = text1 + text2
print(result)

#concatenar una cadena
name = "Anderson"
lastname = "Imbachi"
fullname = name + " " + lastname
print(fullname)

#formato de cadena
#format string
price = 97
text3 = f"the price is {price:.2f} dollars"
print(text3)

#math operation
text4 = f"la multiplicacion es {20 * 59}"
print(text4)

#string capitalize()
text5 = "python es un lenguaje de alto nivel de programacion"
result1 = text5.capitalize()
print(result1)

#string caseflofd()
title= "Cien Años de Soledad"
titleconvert = title.casefold()
print(titleconvert)

#string center()
fruit = "banana"
textcenter = fruit.center(  20,  "-")
print(textcenter)

#string count()
title1 = "I love apples, apple are my favorite fruit"
result2 = title1.count("apple")
print(result2)

#string endswith
text6 = "Curso, fundamentos con python."
result3 = text6.endswith(".")
print(result3)

#string expandtabs
letter = "F\tu\tp"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)

#string find
text7 = "Hola, bienvenidos a colombia."
result4 = text7.find("bienvenidos")
print(result4)

#funcion title
text8 ="welcome to my world"
result5 = text8.title()
print(result5)

#funcion isalnum
alphanumeric = "Python312"
result6 = alphanumeric.isalnum()
print(result6)

#funcion isalnum
letters = "Space X"
result7 = letters.isalnum()
print(result7)