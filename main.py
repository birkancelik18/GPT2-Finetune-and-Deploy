from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
from pydantic import BaseModel


class ShakespeareWriter:
    def talk_to_shakespeare(self):
        response = {"message": "Hello World"}
        return response

app = FastAPI()
shakespeare = ShakespeareWriter()

# CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return shakespeare

@app.post("/send-text")
def send_text(text: str):
    # Here you can perform any processing on the received text
    # For now, let's just return the received text as is
    return {"received_text": text}

@app.post("/send-text-len")
def send_text_length(text: str):
    # Calculate the length of the received text
    text_length = len(text)

    # Return the length as a JSON response
    return {"text_length": text_length}



class TextInput(BaseModel):
    text: str

@app.post("/send-model-response")
async def send_text_length(text_input: TextInput):
    loaded_model = GPT2LMHeadModel.from_pretrained("outputs/finetuned_shakespeare")
    loaded_tokenizer = GPT2Tokenizer.from_pretrained("outputs/finetuned_shakespeare")

    loaded_generator = pipeline('text-generation', model=loaded_model, tokenizer=loaded_tokenizer)

    response_model = loaded_generator(text_input.text, max_length=50, num_return_sequences=1)
    generated_text = response_model[0]["generated_text"]

    return {"response": generated_text}