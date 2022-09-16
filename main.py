c = ['c']
o = ['o']
k = ['k']
i = ['i']
e = ['e']
gl = ['_', '_', '_', '_', '_', '_']
bl = []
word = 'cookie'
gamend = False
while gamend == False:
  if gl == ['c', 'o', 'o', 'k', 'i', 'e']:
    print('You Win!')
    gamend = True
  print("------------------------------------------------------------")
  print("Bad Letters:")
  print(bl)
  print("Good Letters:")
  print(gl)
  answer = input()
  if answer in word == "cookie":
    if answer == c[0]:
      gl.insert(0, answer)
      gl.remove('_')
      c.pop()
      c.insert(0, '_')
    if answer == o[0]:
      gl.insert(1, answer)
      gl.remove('_')
      gl.insert(2, answer)
      gl.remove('_')
      o.pop()
      o.insert(0, '_')
    if answer == k[0]:
      gl.insert(3, answer)
      gl.remove('_')
      k.pop()
      k.insert(0, '_')
    if answer == i[0]:
      gl.insert(4, answer)
      gl.remove('_')
      i.pop()
      i.insert(0, '_')
    if answer == e[0]:
      gl.insert(5, answer)
      gl.remove('_')
      e.pop()
      e.insert(0, '_')
  else: 
    bl.append(answer)
    if len(bl) > 4:
      print('You Lost!')
      gamend = True
  
  
