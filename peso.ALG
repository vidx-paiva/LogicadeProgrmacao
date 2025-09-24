Algoritmo "ponderada"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 

Var
nota1, nota2, media, notarec: real


Inicio
  escreval("Digite a primeiro nota: ")
      leia(nota1)

      escreval("Digite a segunda nota: ")
      leia(nota2)
      
      media := (nota1*2 + nota2*3) / 5
      
      se media >=7 entao
         escreval("voce obteve media", media:4:2,".Resultado:Aprovado.")
         
       senao
           escreval("Você não obteve a média para aprovação direta. (média = ", media:4:2, ")")
          escreva("Digite a nota da recuperação: ")
      leia(notaRec)

      se notaRec >= 7 entao
         escreval("Você obteve nota ", notaRec:4:2, " na recuperação. Resultado: Aprovado.")
      senao
         escreval("Você não alcançou a média para aprovação. Resultado: Reprovado.")
      fimse
   fimse

Fimalgoritmo