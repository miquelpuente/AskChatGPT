import openai
import os
import tkinter as tk

def button_clicked():
    respuesta = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=entry.get(), 
        max_tokens=100, 
        temperature=0.5,
    )

    response = tk.Label(root, text=entry.get() + os.linesep + respuesta.choices[0].text)
    response.pack()

# Configura la API Key
openai.api_key = os.environ["OPENAI_API_KEY"] 

# Form
root = tk.Tk()

entry = tk.Entry(root, width=500)#, label="Introduce una pregunta")
entry.pack()

button = tk.Button(root, text="Enviar", command=button_clicked)
button.pack()

root.mainloop()



    