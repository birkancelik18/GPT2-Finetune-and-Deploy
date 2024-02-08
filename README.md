# Shakespearean Text Generation with GPT-2 and FastAPI

## Overview

This repository contains a project that utilizes a fine-tuned GPT-2 model on a Shakespearean dataset for text generation. The project includes an implementation of FastAPI, a modern web framework for building APIs with Python, to provide a user-friendly interface for interacting with the generated text.

## Contents

1. [Fine-tuned GPT-2 Model](#fine-tuned-gpt-2-model)
2. [FastAPI Framework](#fastapi-framework)
3. [User Interface](#user-interface)
4. [Getting Started](#getting-started)
5. [API Endpoints](#api-endpoints)
6. [Contributing](#contributing)
7. [License](#license)

## Fine-tuned GPT-2 Model

The repository includes a fine-tuned GPT-2 model trained on a Shakespearean dataset. The model is capable of generating text in the style of Shakespeare's works.

## FastAPI Framework

FastAPI is used to create a robust and efficient web API for serving the GPT-2 model. The project includes different subpages in the FastAPI framework, providing a structured and modular API.

## User Interface

A user interface has been implemented to facilitate interaction with the GPT-2 model. After running the FastAPI application, open the `index.html` file in your browser to access the user interface.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/birkancelik18/GPT2-Finetune-and-Deploy.git
    cd GPT2-Finetune-and-Deploy
    ```

2. Create and activate a conda environment:

    ```bash
    conda create --name shakespeare-gpt2-env
    conda activate shakespeare-gpt2-env
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Download this folder that has finetuned [model weights ](https://drive.google.com/file/d/1onuyIB5c72pqiTeHvXk_3NV7KuVLoLGO/view?usp=sharing).

5. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

6. Open the `index.html` file in your browser and start interacting with the model.

## API Endpoints

### 1. Talk to Shakespeare

- **Endpoint:** `/`
  - Method: GET
  - Description: Get a simple response from Shakespeare.
  - Example:

    ```bash
    curl -X GET "http://localhost:8000/"
    ```

### 2. Send Text

- **Endpoint:** `/send-text`
  - Method: POST
  - Description: Receive and return the received text as is.
  - Example:

    ```bash
    curl -X POST "http://localhost:8000/send-text" -H "Content-Type: application/json" -d '{"text": "To be or not to be"}'
    ```

### 3. Send Text Length

- **Endpoint:** `/send-text-len`
  - Method: POST
  - Description: Calculate and return the length of the received text.
  - Example:

    ```bash
    curl -X POST "http://localhost:8000/send-text-len" -H "Content-Type: application/json" -d '{"text": "To be or not to be"}'
    ```

### 4. Send Model Response

- **Endpoint:** `/send-model-response`
  - Method: POST
  - Description: Generate Shakespearean-style text based on the received input using the fine-tuned GPT-2 model.
  - Example:

    ```bash
    curl -X POST "http://localhost:8000/send-model-response" -H "Content-Type: application/json" -d '{"text": "To be or not to be"}'
    ```

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your contributions are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.

---
