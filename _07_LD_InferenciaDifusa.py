# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install -U scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear objetos antecedentes y consecuentes
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir funciones de membresía
calidad['mala'] = fuzz.trimf(calidad.universe, [0, 0, 5])
calidad['aceptable'] = fuzz.trimf(calidad.universe, [0, 5, 10])
calidad['buena'] = fuzz.trimf(calidad.universe, [5, 10, 10])

servicio['pobre'] = fuzz.trimf(servicio.universe, [0, 0, 5])
servicio['aceptable'] = fuzz.trimf(servicio.universe, [0, 5, 10])
servicio['excelente'] = fuzz.trimf(servicio.universe, [5, 10, 10])

propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Definir reglas difusas
regla1 = ctrl.Rule(antecedent=(calidad['mala'] | servicio['pobre']), consequent=propina['baja'])
regla2 = ctrl.Rule(antecedent=(calidad['aceptable'] & servicio['aceptable']), consequent=propina['media'])
regla3 = ctrl.Rule(antecedent=(calidad['buena'] | servicio['excelente']), consequent=propina['alta'])

# Crear sistema de control
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])

# Crear simulador
simulador = ctrl.ControlSystemSimulation(sistema_control)

# Definir entradas
simulador.input['calidad'] = 6.5
simulador.input['servicio'] = 9.8

# Computar resultado
simulador.compute()

# Obtener el valor de propina
propina_valor = simulador.output['propina']
print(f'El valor de la propina es: {propina_valor:.2f}')

# Visualizar las funciones de membresía y reglas (opcional)
calidad.view()
servicio.view()
propina.view()
