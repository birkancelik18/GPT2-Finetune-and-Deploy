# Shakespearean Text Generation with GPT-2 and FastAPI

## Overview

This repository contains a project that utilizes a fine-tuned GPT-2 model on a Shakespearean dataset for text generation. The project includes an implementation of FastAPI, a modern web framework for building APIs with Python, to provide a user-friendly interface for interacting with the generated text.

## Contents

1. [Fine-tuned GPT-2 Model](#fine-tuned-gpt-2-model)
2. [FastAPI Framework](#fastapi-framework)
3. [User Interface](#user-interface)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Fine-tuned GPT-2 Model

The repository includes a fine-tuned GPT-2 model trained on a Shakespearean dataset. The model is capable of generating text in the style of Shakespeare's works.

## FastAPI Framework

FastAPI is used to create a robust and efficient web API for serving the GPT-2 model. The project includes different subpages in the FastAPI framework, providing a structured and modular API.

## User Interface

A user interface has been implemented to facilitate interaction with the GPT-2 model. Users can input prompts and receive generated text in the Shakespearean style through a simple and intuitive interface.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

4. Access the user interface at `http://localhost:8000` and start interacting with the model.

## Usage

### API Endpoints

- **Endpoint 1:** `/generate_text`
  - Method: POST
  - Description: Generate Shakespearean text based on input prompts.
  - Example:

    ```bash
    curl -X POST "http://localhost:8000/generate_text" -H "Content-Type: application/json" -d '{"prompt": "To be or not to be"}'
    ```

### User Interface

1. Access the user interface at `http://localhost:8000`.
2. Input your desired prompt in the provided text box.
3. Click the "Generate" button to receive Shakespearean-style text.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your contributions are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.

---
