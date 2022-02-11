diccionario = {
  0 : 'Hasta luego curso! Turing, puedes estar orgulloso de mi',
  1 : 'Goodbye course! Turing, you can be proud of me',
  2 : 'Au revoir cours! Turing, tu peux etre fier de moi',
  3 : 'Adeus, curso! Turing, pode se orgulhar de mim',
  4 : 'Auf Wiedersehen! Turing, du kannst stolz auf mich sein'
}

numeroBase = int(input())
divisor = 5

while numeroBase >= 5:
  division = numeroBase/divisor
  modulo = int(numeroBase%5)
  numeroBase = division
  print(diccionario[modulo])
