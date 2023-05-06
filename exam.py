import os
import tkinter as tk
from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI


os.environ["OPENAI_API_KEY"] = "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"


# create the vector index
def createVectorIndex(path):
    max_input = 4096
    tokens = 256
    chunk_size = 600
    max_chunk_overlap = 20

    prompt_helper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size_limit=chunk_size)

    # LLM(Large Lng Models)
    llmPredictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-ada-001", max_tokens=tokens))

    # loading the data
    docs = SimpleDirectoryReader(path).load_data()

    service_context = ServiceContext.from_defaults(llm_predictor=llmPredictor, prompt_helper=prompt_helper)
    vectorIndex = GPTSimpleVectorIndex.from_documents(documents=docs, service_context=service_context)

    vectorIndex.save_to_disk('vectorIndex.json')
    return 'vectorIndex.json'


vectorIndex = createVectorIndex("database")


# function to get response
def get_response(prompt, vectorIndex):
    vIndex = GPTSimpleVectorIndex.load_from_disk(vectorIndex)
    response = vIndex.query(prompt, response_mode="compact")
    return response


# create the tkinter window
root = tk.Tk()
root.geometry('700x500')
root.title("Chat with AI")

# create a label for the response
response_label = tk.Label(root, text="Type your question and press Enter", font=("Arial", 18), pady=10, wraplength=600)
response_label.pack()

# create an entry for user input
input_frame = tk.Frame(root, pady=30)
input_frame.pack()

input_label = tk.Label(input_frame, text="Ask a question: ", font=("Arial", 16))
input_label.pack(side="left")

input_entry = tk.Entry(input_frame, font=("Arial", 16), width=50)
input_entry.pack(side="left", padx=10)

# create a button for user input
button_frame = tk.Frame(root)
button_frame.pack()


def handle_input():
    prompt = input_entry.get()
    response = get_response(prompt, vectorIndex)
    response_label.config(text=response)


submit_button = tk.Button(button_frame, text="Submit", font=("Arial", 16), command=handle_input)
submit_button.pack(pady=10)

# bind the input entry to the handle_input function
input_entry.bind("<Return>", lambda event: submit_button.invoke())

root.mainloop()
