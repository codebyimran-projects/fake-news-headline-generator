# Fake News Headline Generator

A simple and interactive **Streamlit web application** that generates fictional news headlines by randomly combining subjects, actions, and topics.

> **Note:** This project generates fictional content for educational and entertainment purposes. It does not generate or verify real news.

## Features

- Generate multiple fictional headlines instantly
- Choose from different news categories
- Randomly combines:
  - Subjects
  - Actions
  - Topics
- Generate up to 10 headlines at once
- Clean dark-themed interface
- Simple and responsive Streamlit UI
- Clear generated results with one click

## News Categories

The generator currently includes:

- Technology
- Science
- Sports
- World

Each category contains its own collection of subjects, actions, and topics to create relevant fictional headlines.

## How It Works

The application uses Python's `random` module to randomly select a subject, action, and topic from separate lists.

```text
Subject + Action + Topic
```

For example:

```text
Scientists Discover a mysterious technology
```

Another combination might produce:

```text
Astronomers Detect a mysterious signal
```

Every time headlines are generated, the application creates new random combinations.

## Technologies Used

- Python
- Streamlit
- Random Module

## Project Structure

```text
fake-news-headline-generator/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/codebyimran/fake-news-headline-generator.git
```

### 2. Open the Project Folder

```bash
cd fake-news-headline-generator
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Requirements

Create a `requirements.txt` file containing:

```text
streamlit
```

## Example Output

```text
Scientists Discover a mysterious technology

Biologists Detect a hidden ocean

Football Stars Achieve a record-breaking performance

World Leaders Announce a surprising new plan
```

All generated headlines are fictional.

## Learning Objectives

This project demonstrates several Python and application-development concepts:

- Python lists
- Dictionaries
- Variables
- Loops
- Conditional logic
- Random selection
- String formatting
- Streamlit components
- Streamlit session state
- Basic UI customization

## Future Improvements

Possible future improvements include:

- More news categories
- Larger word collections
- Custom user-created word lists
- Headline history
- Copy-to-clipboard functionality
- More advanced headline templates
- Download generated headlines
- Custom headline patterns

## Disclaimer

This application is a **fictional headline generator**. Generated content should not be treated as factual news or used as a source of real-world information.

## Author

**Muhammad Imran**

Website: **[@codebyimran](https://codebyimran.com)**

Built with **Python and Streamlit**.

If you found this project useful, consider giving the repository a star.
