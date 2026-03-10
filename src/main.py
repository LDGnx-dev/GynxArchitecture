import sys

class GynxInterpreter:
    def __init__(self):
        self.commands = {
            "SISTEM_START": self.iniciar,
            "SHOW": self.mostrar,
            "STATE": self.saturno,
            "SISTEM_FINISH": self.finalizar
        }

    def iniciar(self, nombre):
        print(f"🪐 [SYSTEM] {nombre.strip(chr(34))} - Operativo.")

    def mostrar(self, mensaje):
        print(f"💬 [DISPLAY] {mensaje.strip(chr(34))}")

    def saturno(self, nivel):
        # 1 es activo (Saturno/Tsuki en órbita)
        status = "FULL_SYNC" if nivel == "1" else "OFFLINE"
        icon = "🪐🌙" if nivel == "1" else "🌑"
        print(f"✨ [STATE] {status} {icon}")

    def finalizar(self, _=None):
        print("🚀 [LOG] GynxArchitecture: Sesión finalizada correctamente.")

    def run(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith("#"): continue
                    
                    parts = line.split(maxsplit=1)
                    cmd = parts[0]
                    args = parts[1] if len(parts) > 1 else None
                    
                    if cmd in self.commands:
                        self.commands[cmd](args)
                    else:
                        print(f"❌ [ERROR] Comando desconocido: {cmd}")
        except FileNotFoundError:
            print(f"❌ [ERROR] No se encontró el archivo: {filename}")

if __name__ == "__main__":
    interpreter = GynxInterpreter()
    interpreter.run("example.gynx")