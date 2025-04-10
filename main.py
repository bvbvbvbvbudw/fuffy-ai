from brain import Fuffy
from rich.console import Console

fuffy = Fuffy()
console = Console()

console.print("[bold green]Фуффи запущен![/bold green] Напиши что-нибудь:")

while True:
    try:
        user_input = input("🧑‍💻 Ты: ")
        if user_input.lower() in ["выход", "exit", "quit"]:
            break
        reply = fuffy.think(user_input)
        print("🤖 Фуффи:", reply)
    except KeyboardInterrupt:
        print("\n[!] Завершено пользователем.")
        break