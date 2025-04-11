import subprocess

FORBIDDEN_COMMANDS = [
    "rm -rf", "format", "shutdown -h", "del C:\\", "poweroff",
    "mkfs", ":(){:|:&};:", "shutdown /r", "shutdown /s", "kill", "taskkill"
]

def is_command_safe(cmd: str) -> bool:
    return not any(forbidden in cmd.lower() for forbidden in FORBIDDEN_COMMANDS)

def execute_command(command: str) -> str:
    command = command.strip().splitlines()[0]

    if not is_command_safe(command):
        return f"❌ Команда запрещена по соображениям безопасности: `{command}`"

    try:
        subprocess.Popen(command, shell=True)
        return f"✅ Выполняю: `{command}`"
    except Exception as e:
        return f"⚠️ Ошибка при выполнении: {e}"