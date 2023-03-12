import os
import openai
import gradio as gr
  

openai.api_key = "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"

start_sequence ="\nComputer:"
restart_sequence= "\nHuman:"
prmp = "The following consersation with Robot !!"
def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prmp, 
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " Computer:"]
    )
    return response.choices[0].text

def conversation_history(input, history):
    history = history or []
    s = list(sum(history,()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    print("output : ", output)
    history.append((input, output))
    return history, history


blocks = gr.Blocks()

with blocks:
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prmp)
    state = gr.State()
    submit = gr.Button("Click")
    submit.click(conversation_history, inputs=[message, state], outputs=[chatbot, state])

blocks.launch(debug=True)
