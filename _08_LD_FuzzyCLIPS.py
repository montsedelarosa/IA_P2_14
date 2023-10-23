# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install pyclips

import clips

# Inicializar el entorno de CLIPS
environment = clips.Environment()

# Cargar la extensión de Fuzzy CLIPS
environment.load("libfuzzyclips")

# Crear un nuevo sistema de inferencia difusa
environment.build("(defsystem restaurant-fuzzy)")

# Definir conjuntos difusos para la calidad y el servicio
environment.build('''
    (fuzzy-defuzzify quality 0 10 0.1)
    (fuzzy-defuzzify service 0 10 0.1)
''')

# Definir reglas difusas
environment.build('''
    (fuzzy-defrule rule1
        (quality poor)
        (service poor)
        =>
        (assert (tip 5))
    )
    (fuzzy-defrule rule2
        (quality good)
        (service good)
        =>
        (assert (tip 20))
    )
''')

# Insertar hechos en el sistema
environment.assert_string('(quality poor)')
environment.assert_string('(service good)')

# Ejecutar el sistema de inferencia
environment.run()

# Obtener el valor de la variable de salida (tip)
tip_fact = environment.find_fact('tip')
tip_value = tip_fact.slot_value('value')

print(f'El valor de la propina es: {tip_value}')
