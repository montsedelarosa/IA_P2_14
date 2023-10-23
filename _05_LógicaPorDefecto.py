# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

class AgenteLogicoPorDefecto:
    def __init__(self):
        # Base de conocimiento de hechos por defecto
        self.hechos_por_defecto = {
            "Puede_volar": True,  # Suponemos que los pájaros pueden volar por defecto
            "Es_un_pájaro": True  # Suponemos que si algo puede volar, es un pájaro por defecto
        }

    def verificar_hecho(self, hecho):
        if hecho in self.hechos_por_defecto:
            return self.hechos_por_defecto[hecho]
        else:
            return False  # Si el hecho no está en la base de conocimiento, por defecto asumimos que es falso

# Crear un agente lógico por defecto
agente = AgenteLogicoPorDefecto()

# Consultas
animal = "Pingüino"  # Un pingüino, que no es un pájaro
puede_volar = agente.verificar_hecho("Puede_volar")
es_un_pajaro = agente.verificar_hecho("Es_un_pájaro")

print(f"¿{animal} puede volar? {puede_volar}")
print(f"¿{animal} es un pájaro? {es_un_pajaro}")
