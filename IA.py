from groq import Groq
from dotenv import load_dotenv
import os

# lee archivo env
load_dotenv()

# titulo
print("AGENTE IA")

# declaramos la importacion grop como variable
client = Groq()



# creamos una lista donde se almacenara las comversaciones
messages = [
   {"role":"system", "content": "eres un asistente util"}
]


# funcion

def list_files_in_dir(directory ="."):
  print("⚙️ Herramienta llamado: list_files_in_dir")
  try:
      files = os.listdir(directory)
      return {"files": files}
  except Exception as e:
      print(f"hubo un problema : {e}")


tools=[
        {
            "type": "function",
            "function": {
                "name": "list_files_in_dir",
                "description": "lista los archivos que existen en un Directorio dado (por defecto en el directorio actual).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "param1": {"type": "string", "description": " Directorio para listar(opcional). por defecto en el directorio actual."}
                    }, 
                    "required": ["param1"]
                }
            }
        }
    ]

# bucle
while True:
  
  usuario = input("tu: ").strip()

  # validaciones
  if not usuario:
    continue
  
  if usuario.lower() in ("salir","exit","adios","bye","hasta luego"):
    print("hasta luego!!!")
    break
  

  messages.append({"role": "user", "content": usuario})



  response = client.chat.completions.create(
     model="llama-3.3-70b-versatile",
     messages=messages,
     tools=tools
)
  

#   replicar_message = response.choices[0].message.content
#   messages.append({"role": "assistant", "content": replicar_message })

#   print(f"Asistente : {replicar_message}")

# almacenar para el historial



