print("Digite um endereço de e-mail válido!")
email = input("E-mail: ")   
if "@gmail.com" in email and "." in email:
    print("E-mail válido!")   
elif "@outlook.com" in email and "." in email:      
    print("E-mail válido!")
else:
    print("E-mail inválido!")