Algoritmo "classifica_idade"

Var
   idade: inteiro

Inicio
   Escreva("Digite a idade: ")
   Leia(idade)

   Se (idade < 12) Então
      Escreva("Classificação: Criança")
   Senao
      Se (idade < 18) Então
         Escreva("Classificação: Adolescente")
      Senao
         Se (idade < 60) Então
            Escreva("Classificação: Adulto")
         Senao
            Escreva("Classificação: Idoso")
         FimSe
      FimSe
   FimSe

Fimalgoritmo
