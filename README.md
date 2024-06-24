# Counseling GPT

This is the Counseling Tool to train Teacher-Counselor how to face the student and help student elaborate their situation.

## Environment

We can use mincromamba to create the environment as follow

`micromamba env create -n counsiling_env -f requirements.yaml`

Create the virtual environment

`micromamba activate counsiling_env`

To access OPENAI GPT, you need provide the API key in `.env` file.

You can get API key from this page: [OPENAI API KEY](https://platform.openai.com/api-keys)

## Start

You need provdie `.case` to create the virtual student. The teacher user will conusiling with this virtual student.

You can start the program with `python3 main.py`. It will start gradio interface, you only provide the gradio link let the Teacher-Counselor to exercise.
