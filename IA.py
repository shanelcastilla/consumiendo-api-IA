from groq import Groq
from dotenv import load_dotenv
import os
import json

# lee archivo env
load_dotenv()

# titulo
print("AGENTE IA")

# declaramos la importacion grop como variable
client = Groq()



# creamos una lista donde se almacenara las comversaciones
messages = [
   { "role":"system", "content": "eres un asistente util" }
]


# funcion asignada 

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
                        "directory": {"type": "string", "description": "Directorio para listar (opcional). Por defecto es el directorio actual."}
                    }, 
                    "required": []
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
  
  # obtener la respuesta del modelo
  assistant_message = response.choices[0].message
  
  # agregar mensaje del asistente al historial
  messages.append({"role": "assistant", "content": assistant_message.content or ""})
  
  # holverificar si hay tool calls
  if assistant_message.tool_calls:
      for tool_call in assistant_message.tool_calls:
          ft_name = tool_call.function.name
          args = json.loads(tool_call.function.arguments)
          
          print(f"el modelo considera llamar a la herramienta {ft_name}")
          
          # ejecutar la herramienta
          if ft_name == "list_files_in_dir":
              result = list_files_in_dir(args.get("directory", "."))
              print(f"Resultado: {result}")
  else:
      # si no hay tool calls, solo mostrar el mensaje
      if assistant_message.content:
          print(f"ASISTENTE : {assistant_message.content}")




