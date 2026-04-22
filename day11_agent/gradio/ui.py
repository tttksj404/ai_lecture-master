import gradio as gr

def greet(first_name, last_name, intensity):
    return ("Hello, " + first_name + " " + last_name + "!") * int(intensity)

with gr.Blocks() as demo:
    with gr.Row():
        first = gr.Textbox(label="First name")
        last = gr.Textbox(label="Last name")
        intensity = gr.Slider(minimum=1, maximum=5, step=1, label="Intensity")
    output = gr.Textbox(label="Greeting")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=[first, last, intensity], outputs=output)

demo.launch(share=True)