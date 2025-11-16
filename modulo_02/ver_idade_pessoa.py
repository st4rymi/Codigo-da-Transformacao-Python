'''
Primicias
   Verificar a idade da pessoa.
Saber a idade da pessoa;
armazenar a idade em uma variavel (int);
caso a idade seja maior que 18 anos;
mostrar a mensagem "Você é maior de idade";
se não for maior que 18 anos mostrar a mensagem "Você é menor de idade".;

'''
# Criando Estruturas
print("\n---------------------")
print("\f Bem-Vindo(a), amigo(a)!!")
print("\n---------------------")

nome_pessoa = str(input("Qual o seu nome? "))

idade_pessoa = int(input("Qual é sua idade? "))

if idade_pessoa >= 18:
   print ("Muito bem! Você é maior de idade. ^-^ ")

   else:
      print ("Aah, que pena! Você é menor de idade. Tente na próxima.. >.< ")

      print(f"Olá, {nome_pessoa}! Sua idade é {idade_pessoa}.")