import gradio as gr
from main import doc_chatbot

iface = gr.Interface(fn=doc_chatbot,
                     inputs=gr.components.Textbox(lines=7, label="Enter your text"),
                     outputs="text", title="Custom-trained Chatbot")

iface.launch(share=True)
