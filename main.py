class Estudiante:
    def __init__(self, nombre, curso, notas, apoderado, contacto, faltas, anot_positivas, anot_negativas):
        self.nombre = nombre
        self.curso = curso
        self.notas = notas
        self.apoderado = apoderado
        self.contacto = contacto
        self.faltas = faltas
        self.anot_positivas = anot_positivas
        self.anot_negativas = anot_negativas
    def calcular_promedio(self):
        if not self.notas:
            return 0.0
        return round(sum(self.notas) / len(self.notas), 1)

    def evaluar_riesgo(self):
        promedio = self.calcular_promedio()
        riesgo_academico = promedio < 4.0
        riesgo_conducta = self.faltas > 15 or self.anot_negativas > 5
        if riesgo_academico and riesgo_conducta:
            return "riesgo critico (Académico y Conducta/Asistencia)"
        elif riesgo_academico:
            return "riesgo academico (Promedio menor a 4.0)"
        elif riesgo_conducta:
            return "riesgo por asistencia o conducta"
        else:
            return "sin riesgo"
        
    def mostrar_informacion(self):
        promedio = self.calcular_promedio()
        riesgo = self.evaluar_riesgo()
        print(f"\n--- informe de {self.nombre} ({self.curso}) ---")
        print(f"Notas: {self.notas} | Promedio: {promedio}")
        print(f"Apoderado: {self.apoderado} | Contacto: {self.contacto}")
        print(f"Faltas: {self.faltas} | Positivas: {self.anot_positivas} | Negativas: {self.anot_negativas}")
        print(f"Estado: {riesgo}")

class SistemaEscolar:
    def __init__(self):
        self.estudiantes = []

    def registrar_estudiante(self):
        print("\n Registro de estudiante ")
        nombre = input("Nombre completo: ")
        curso = input("Curso: ")
        notas_input = input("Notas (separadas por espacio, ej: 5.5 6.0): ")
        notas = [float(n) for n in notas_input.split()] if notas_input else []
        apoderado = input("Nombre del apoderado: ")
        contacto = input("Contacto: ")
        faltas = int(input("Número de faltas: "))
        anot_pos = int(input("Anotaciones positivas: "))
        anot_neg = int(input("Anotaciones negativas: "))
        nuevo = Estudiante(nombre, curso, notas, apoderado, contacto, faltas, anot_pos, anot_neg)
        self.estudiantes.append(nuevo)
        print("Estudiante registrado con éxito")

    def buscar_estudiante(self):
        print("\n Busqueda ")
        nombre_buscado = input("Nombre del estudiante: ").strip().lower()
        curso_buscado = input("Curso: ").strip().lower()
        for est in self.estudiantes:
            if est.nombre.lower() == nombre_buscado and est.curso.lower() == curso_buscado:
                est.mostrar_informacion()
                return
       
        print("No se encontró al estudiante.")

def menu():
    sistema = SistemaEscolar()
   
    while True:
        print("\n Menú")
        print("1. Registrar Estudiante")
        print("2. Buscar Estudiante")
        print("3. Salir")
       
        opcion = input("Opción: ")
        if opcion == "1":
            sistema.registrar_estudiante()
        elif opcion == "2":
            sistema.buscar_estudiante()
        elif opcion == "3":