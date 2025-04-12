# Fuffy - My First AI Project

Hello! I'm **Fuffy**, and this is my first AI project. The goal of this project is to create a simple conversational AI that uses a local language model.

## Prerequisites

Before running the project, make sure you have the following installed:

- **Python** (recommended version 3.8 or higher)
- **llama.cpp** (to run the language model)
- **SQLite** (for storing dialogue history)

## Setup Instructions

Follow these steps to get the project up and running:

### 1. **Build `llama.cpp`**

To use the local language model, you need to build `llama.cpp` from source. You can follow the instructions in the [llama.cpp GitHub repository](https://github.com/ggerganov/llama.cpp) to build it.

1. Clone the repository:
```
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
```

Build the project using CMake:
```
mkdir build
cd build
cmake ..
cmake --build . --config Release
```
Make sure the build is successful before proceeding.

### 2. Install the Model
You need to download the model file that will be used for inference. You can download the model (e.g., [mistral-7b-instruct-v0.1.Q4_K_M.gguf](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF?show_file_info=mistral-7b-instruct-v0.1.Q4_K_M.gguf)) from the official sources or use the huggingface_hub to download it.

Once downloaded, place the model file in the models directory of your project.

### 3. Create the consts.py File
Create a new Python file named consts.py in the project root directory. In this file, define the path to your model and the llama-cli binary:
```
MODEL_PATH = "C:/path/to/models/mistral.gguf"
LLAMA_RUN_PATH = "C:/path/to/llama.cpp/build/bin/Release/llama-run.exe"
THREADS = "8"
TOKENS = "16"
TEMP = "0.5"
TIMEOUT = 240
TELEGRAM_TOKEN = ""
```
Make sure to adjust the path to the model file and the llama-cli binary if they are located elsewhere on your system.

### 4. Run the Project
After setting up the model and configuration, you can run the project in one of the following ways:
**Using the terminal interface:**
```
python main.py
```

**Using the Telegram bot:**
```
python bots/telegram.py
```

**Using the graphical interface (GUI):**
```
python bots/fuffy_gui.py
```

This will start the conversational AI. You can interact with Fuffy by typing messages, and it will respond based on the model's training.

## Additional Notes
If you encounter any issues with building llama.cpp or running the model, refer to the official documentation.

This project is designed to be simple and local, so it does not require an internet connection to run once set up.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

MIT License: [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)
