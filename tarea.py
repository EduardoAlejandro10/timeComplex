

## algoritmo lineal o(n)

def  bin_exp_mod(a, n, b):
    assert not (b == 0) 
    "This cannot accept modulo that is == 0"
    if n == 0: 
        return 0
        
    if n % 2 == 1:
        return (bin_exp_mod(a, n - 1, b))
        
    r = bin_exp_mod(a, n / 2, b)
    return (r * r ) % b

  
  
from collections.abc import Sequence
  
  
  ## O(n^3) complejidad exponencial 
  
def decimal_to_binary(no_of_variable: int, minterms:
      Sequence[float]) -> list[str]:
    temp = []
    for minterm in minterms:
        string = ""
        for i in range(no_of_variable):
            string = str(minterm % 2) + string
            minterm //= 2
        temp.append(string)
    return temp
  
  

## no pude pensar en alguna sugerencia para hacerlo mas efiiciente, me hace falta estudiar python soy de los que no vieron python, muchas gracias profe