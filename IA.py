from groq import Groq
from dotenv import load_dotenv


load_dotenv()


print("AGENTE IA")

client = Groq()

messages = [
   {"role":"system", "content": "eres un asistente util"}
]


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
     messages=messages
)
  

  replicar_message = response.choices[0].message.content
  messages.append({"role": "assistant", "content": replicar_message })

  print(f"system : {replicar_message}")