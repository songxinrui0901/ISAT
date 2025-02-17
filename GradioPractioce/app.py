import gradio as gr

with gr.Blocks(fill_height=True,fill_width=True) as demo:
    with gr.Accordion("Accordion"):
        with gr.Tab("Tab 1"):
            with gr.Row():
                gr.Textbox(label="Enter text")
                with gr.Column():
                    gr.Checkbox(label="Checkbox 1"),
                    gr.Checkbox(label="Checkbox 2"),
                    gr.Checkbox(label="Checkbox 3")
                gr.Text(label="Text 1",scale = 2,min_width=100)
                with gr.Column():
                    gr.Textbox(label="Enter text")
        with gr.Tab("Tab 2"):
            gr.Textbox(label="Enter text")
            gr.Chatbot(scale = 1)

if __name__ == "__main__":
    demo.launch(share=True)