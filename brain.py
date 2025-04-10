import subprocess
from memory import FuffyMemory
from consts import model, path_to_llama

class Fuffy:
    def __init__(self):
        self.memory = FuffyMemory()
        self.model_path = f"models/{model}"

    def think(self, prompt: str) -> str:
        self.memory.save_dialogue("user", prompt)

        context = self.memory.get_last_context()
        full_prompt = f"{context}\nUser: {prompt}\nFuffy:"

        result = subprocess.run(
            [path_to_llama, "-m", self.model_path, "-p", full_prompt, "-n", "200"],
            capture_output=True, text=True
        )

        output = result.stdout.split("Fuffy:")[-1].strip()
        self.memory.save_dialogue("fuffy", output)
        return output