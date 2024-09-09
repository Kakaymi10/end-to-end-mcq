# MCQ Generator AI

## Project Overview

The **MCQ Generator AI** is an end-to-end project that generates Multiple-Choice Questions (MCQs) automatically from provided text or documents. This tool uses OpenAI's GPT models and LangChain to extract key concepts and generate high-quality questions, answers, and explanations, making it suitable for quiz generation and educational purposes.

## Features

- **Automated MCQ Generation**: Creates multiple-choice questions from any text input using OpenAI's GPT API.
- **Customizable**: Specify the number of questions, difficulty level, and topics.
- **Answer Explanations**: Provides explanations for the correct answers to enhance learning.
- **LangChain Integration**: Leverages LangChain to manage LLM interactions and streamline question generation.

## Technologies Used

- **Python**: Core programming language.
- **OpenAI API**: Powers the natural language generation for questions and answers.
- **LangChain**: Framework for managing interactions with language models.
- **Flask/FastAPI** (Optional): For running the MCQ generator as a web service.
- **Git**: Version control for project management.

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/MCQ-Generator-AI.git
   cd MCQ-Generator-AI
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root with your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. **Generate MCQs from Text Input**

   To generate MCQs from a text file:

   ```bash
   python mcq_generator.py --input "path_to_text_file.txt" --num_questions 10
   ```

2. **Run as a Web App (Optional)**

   To serve the MCQ generator through a web interface, run:

   ```bash
   python app.py
   ```

   This will start a web service at `http://localhost:5000` (or the port specified in the script).

## Example

Given the following text input:

```
Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems. Specific applications of AI include expert systems, natural language processing (NLP), and speech recognition.
```

The MCQ Generator AI may produce a question like this:

```
Q1. What is the primary focus of Artificial Intelligence (AI)?

  a) Human psychology
  b) Simulation of human intelligence processes
  c) Development of hardware systems
  d) Improving software efficiency

Correct answer: b) Simulation of human intelligence processes
Explanation: AI focuses on replicating human-like intelligence in machines, allowing them to perform tasks typically requiring human cognition.
```

## Customization

You can customize the question generation by adjusting the parameters in the `mcq_generator.py` script or in API calls. Customizable options include:
- **Number of questions**
- **Difficulty level**
- **Specific topics or keywords**

## Contribution

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request
