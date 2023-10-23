# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install modal-logic

from modal_logic import Formula, K, M

# Definir fórmulas
p = Formula('p')
q = Formula('q')
r = Formula('r')

# Crear una fórmula modal: "Es necesario que p o q"
necesario = K(p | q)

# Imprimir la fórmula modal
print(necesario)

# Comprobar si una fórmula es válida en un mundo posible
mundo_posible = M()
mundo_posible.add_fact(p)

# Verificar si la fórmula "Es necesario que p o q" es válida en el mundo posible
es_valida = mundo_posible.is_valid(necesario)
print(f"¿La fórmula es válida en el mundo posible? {es_valida}")
