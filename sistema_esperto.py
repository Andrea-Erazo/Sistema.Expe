from experta import KnowledgeEngine, Rule, Fact

# Definir las reglas del sistema experto
class MiSistemaExperto(KnowledgeEnginefie):
    def __init__(self):
        super().__init__()
        self.rules = [
            Rule(Fact(symptom='fiebre'), Fact(recommendation='Tomar un antipirético.')),
            Rule(Fact(symptom='tos'), Fact(recommendation='Tomar un jarabe para la tos.')),
            Rule(Fact(symptom='dolor de cabeza'), Fact(recommendation='Descansar y mantenerse hidratado.'))
        ]

    def run(self):
        print("Bienvenido al sistema experto de salud.")
        symptom = input("Introduce tu síntoma: ")
        self.declare(Fact(symptom=symptom))
        
        # Ejecutar las reglas
        self.run_rules()

        # Obtener y mostrar la recomendación
        for fact in self.facts:
            if fact.get('recommendation'):
                print(f"Recomendación: {fact['recommendation']}")

if __name__ == "__main__":
    sistema = MiSistemaExperto()
    sistema.run()
git checkout -b main
