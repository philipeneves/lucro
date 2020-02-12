input= [7,6,4,3,1]
compra = 0
venda = 0
for i in range(len(input)):
  if (input[i] == min(input)):    
    compra = input[i];    
  elif (i + 1 < len(input)):      
    if (input[i] > input[i + 1]):      
      if (compra > 0):   
        venda = input[i];

if (venda - compra > 0):
  print(venda - compra);
else:
  print(0);
