# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install pyModelChecking

from pyModelChecking import ModelChecking
from pyModelChecking.semantics import KripkeStructure

# Crear un modelo de Kripke
model = KripkeStructure()

# Agregar estados al modelo
model.add_states(['s0', 's1', 's2', 's3'])

# Definir relaciones de transición entre estados
model.add_transition('s0', 's1')
model.add_transition('s0', 's2')
model.add_transition('s1', 's3')
model.add_transition('s2', 's3')

# Definir etiquetas en los estados (proposiciones atómicas)
model.set_label('s0', 'p')
model.set_label('s1', 'q')
model.set_label('s2', 'p')
model.set_label('s3', 'r')

# Crear una instancia del verificador de modelos
verificador = ModelChecking(model)

# Definir una fórmula LTL a verificar
formula = 'G(p -> X(q U r))'

# Verificar la fórmula en el modelo
resultado = verificador.check_ltl(formula)

if resultado:
    print(f'La fórmula "{formula}" es válida en el modelo.')
else:
    print(f'La fórmula "{formula}" no es válida en el modelo.')
