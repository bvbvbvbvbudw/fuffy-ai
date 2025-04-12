import subprocess, os, re
from core.memory import FuffyMemory
from core.consts import MODEL_PATH, LLAMA_RUN_PATH, TOKENS, THREADS, TEMP, TIMEOUT

class Fuffy:
    def __init__(self):
        self.memory = FuffyMemory()
        self.model_path = os.path.abspath(os.path.join("models", MODEL_PATH))
        self.llama_run = os.path.abspath(LLAMA_RUN_PATH)

        if not os.path.exists(self.llama_run):
            raise FileNotFoundError(f"Llama executable not found: {self.llama_run}")
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found: {self.model_path}")
        
    def extract_fuffy_response(self, output: str) -> str:
        match = re.search(r'Assistant:\s*(.*?)(<\|im_end\|>|Fuffy:|User:|$)', output, re.DOTALL)
        if match:
            return match.group(1).strip()
    
        match = re.search(r'Fuffy:\s*(.*?)(User:|$)', output, re.DOTALL)
        if match:
            return match.group(1).strip()
    
        return output.strip()


    def think(self, prompt: str) -> str:
        self.memory.save_dialogue("user", prompt)
        
        # context = self.memory.get_last_context()
        # context отключен
        # full_prompt = f"{context}\nUser: {prompt}\nFuffy:"
        
        full_prompt = f"User: {prompt}\nFuffy:"
        command = [
            self.llama_run,
            "-t", THREADS,
            "-n", TOKENS,
            "--temp", TEMP,
            self.model_path,
            full_prompt
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding='utf-8',
                check=True,
                timeout=TIMEOUT
            )
            raw_output = result.stdout
            # self.memory.save_raw_output(raw_output)
            reply = self.extract_fuffy_response(raw_output)
            # self.memory.save_dialogue("fuffy", reply)
            return reply

        except subprocess.CalledProcessError as e:
            print(f"Error running command: {e}")
            return "Sorry, I'm having trouble thinking right now."
        except Exception as e:
            print(f"Unexpected error: {e}")
            return "Something went wrong. Please try again."