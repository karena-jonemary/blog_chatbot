# Blog Chatbot

## Overview

Blog Chatbot is an AI-powered chatbot developed using Python and the Gemini API. The chatbot is specifically designed to answer questions related to blogging, content creation, SEO writing, article writing, copywriting, and content marketing.

The chatbot follows a strict system prompt and only responds to blogging and writing-related queries.

## Features

* AI-powered responses using Google's Gemini API
* Answers questions related to:

  * Blogging
  * Content Creation
  * SEO Writing
  * Copywriting
  * Article Writing
  * Content Marketing
  * Grammar and Editing
* Structured responses with:

  * Title
  * Headings
  * Tone Control
* Restricts responses to blogging and writing topics only
* User-friendly command-line interface

## System Prompt

```text id="q0r8b2"
You are a Blogging Assistant specialized in blogging, content creation, copywriting, SEO writing, article writing, content marketing, and writing improvement; answer only questions related to these topics, format responses with a Title, Headings, and appropriate lists, adapt the tone to the user's request, provide clear actionable advice and examples when relevant, and if a question is not related to blogging, content creation, or writing, respond exactly with: "I am sorry, I can only answer blogging and writing-related questions."
```

## Technologies Used

* Python 3
* Google Gemini API
* Generative AI

## Installation

1. Clone the repository:

```bash id="4m6md9"
git clone https://github.com/your-username/blog-chatbot.git
```

2. Navigate to the project directory:

```bash id="2b2brc"
cd blog-chatbot
```

3. Install dependencies:

```bash id="qj71km"
pip install -r requirements.txt
```

## Configuration

Add your Gemini API key in the Python file or environment variable:

```python id="98hy93"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

## Usage

Run the chatbot:

```bash id="4f9ex5"
python app.py
```

Enter a blogging-related question and the chatbot will generate a structured response.

## Example

### User Input

```text id="k9tt1k"
How can I improve my blog SEO?
```

### Chatbot Response

```text id="3h8j3g"
Title: Blog SEO Improvement Guide

Heading: Keyword Optimization

- Use relevant keywords naturally.
- Optimize meta descriptions.
- Create high-quality content.

Tone: Professional
```

## Project Structure

```text id="2aq9df"
blog-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

## Author

KARENA JONEMARY J

## License

This project is for educational and learning purposes.
