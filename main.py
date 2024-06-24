from openai import OpenAI

import gradio as gr

with open("case.txt", "r", encoding="UTF-8") as file:
    PROMPT = file.read()

with open(".env", "r", encoding="UTF-8") as file:
    env = {}
    for line in file.readlines():
        line = line.split(" = ")
        env[line[0]] = line[1]
        print(line)
    OPENAI_KEY = env["OPENAI_KEY"]

print(OPENAI_KEY)


CLIENT = OpenAI(api_key=OPENAI_KEY)


def predict(message, history):
    """Predict the next message in the conversation."""
    history_openai_format = [{"role": "system", "content": PROMPT}]
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = CLIENT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=history_openai_format,
        temperature=1.0,
        stream=True,
    )

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message


gr.ChatInterface(predict).launch(share=True)
