# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install -U scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear objetos antecedentes y consecuentes
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
velocidad_ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad_ventilador')

# Definir funciones de membresía
temperatura['frío'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['templado'] = fuzz.trimf(temperatura.universe, [0, 50, 100])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

humedad['seca'] = fuzz.trimf(humedad.universe, [0, 0, 50])
humedad['normal'] = fuzz.trimf(humedad.universe, [0, 50, 100])
humedad['húmeda'] = fuzz.trimf(humedad.universe, [50, 100, 100])

velocidad_ventilador['baja'] = fuzz.trimf(velocidad_ventilador.universe, [0, 0, 50])
velocidad_ventilador['media'] = fuzz.trimf(velocidad_ventilador.universe, [0, 50, 100])
velocidad_ventilador['alta'] = fuzz.trimf(velocidad_ventilador.universe, [50, 100, 100])

# Definir reglas
regla1 = ctrl.Rule(temperatura['frío'] & humedad['seca'], velocidad_ventilador['alta'])
regla2 = ctrl.Rule(temperatura['frío'] & humedad['normal'], velocidad_ventilador['media'])
regla3 = ctrl.Rule(temperatura['frío'] & humedad['húmeda'], velocidad_ventilador['baja'])
regla4 = ctrl.Rule(temperatura['templado'] & humedad['seca'], velocidad_ventilador['alta'])
regla5 = ctrl.Rule(temperatura['templado'] & humedad['normal'], velocidad_ventilador['media'])
regla6 = ctrl.Rule(temperatura['templado'] & humedad['húmeda'], velocidad_ventilador['baja'])
regla7 = ctrl.Rule(temperatura['caliente'] & humedad['seca'], velocidad_ventilador['alta'])
regla8 = ctrl.Rule(temperatura['caliente'] & humedad['normal'], velocidad_ventilador['media'])
regla9 = ctrl.Rule(temperatura['caliente'] & humedad['húmeda'], velocidad_ventilador['baja'])

# Crear sistema de control
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9])

# Crear simulador
simulador = ctrl.ControlSystemSimulation(sistema_control)

# Definir entradas
simulador.input['temperatura'] = 75
simulador.input['humedad'] = 40

# Computar resultado
simulador.compute()

# Obtener la velocidad del ventilador
velocidad = simulador.output['velocidad_ventilador']
print(f'La velocidad del ventilador es: {velocidad:.2f}')

# Visualizar las funciones de membresía y reglas (opcional)
temperatura.view()
humedad.view()
velocidad_ventilador.view()
