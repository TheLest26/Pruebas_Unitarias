# operaciones_comparacion.py

def es_mayor_que(a, b):
    """
    Retorna True si 'a' es estrictamente mayor que 'b', de lo contrario False.
    Ejemplo: es_mayor_que(10, 5) -> True
    """
    return a > b

def es_menor_que(a, b):
    """
    Retorna True si 'a' es estrictamente menor que 'b', de lo contrario False.
    Ejemplo: es_menor_que(2, 4) -> True
    """
    return a < b

def es_mayor_o_igual_que(a, b):
    """
    Retorna True si 'a' es mayor o igual que 'b', de lo contrario False.
    Ejemplo: es_mayor_o_igual_que(5, 5) -> True
    """
    return a >= b

def es_menor_o_igual_que(a, b):
    """
    Retorna True si 'a' es menor o igual que 'b', de lo contrario False.
    Ejemplo: es_menor_o_igual_que(3, 5) -> True
    """
    return a <= b

def son_iguales(a, b):
    """
    Retorna True si 'a' y 'b' son iguales, de lo contrario False.
    Ejemplo: son_iguales(7, 7) -> True
    """
    return a == b
