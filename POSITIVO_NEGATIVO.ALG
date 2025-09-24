Algoritmo "Positivo_negativo"
Var
   numero: inteiro
// Escreva um algoritmo que leia um número e verifique
// se ele é positivo ou negativo
Inicio
   escreva("Digite um número: ")
   leia(numero)

   se numero > 0 entao
      escreva("O número é positivo")
   senao
      se numero < 0 entao
         escreva("O número é negativo")
      senao
         escreva("O número é zero")
      fimse
   fimse
Fimalgoritmo
