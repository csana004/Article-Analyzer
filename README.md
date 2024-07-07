Article Analyzer
This project analyzes the sentiment of news articles using Natural Language Processing (NLP) techniques. It fetches articles from provided URLs, summarizes them, and determines their sentiment (positive, negative, or neutral).

Features
Fetch articles from URLs
Summarize articles
Analyze sentiment of articles
Display results in a modern Tkinter GUI
Send analysis results via email
Project Setup
To set up the project and install the required dependencies, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/csana004/Article-Analyzer.git
cd Article-Analyzer
Install the Dependencies:

Ensure you have pip installed. Then, run the following commands:

bash
Copy code
pip install nltk
pip install textblob
pip install newspaper3k
Download NLTK Data:

The project uses the punkt tokenizer. To download it, run the following Python command:

python
Copy code
import nltk
nltk.download('punkt')
Run the Application:

Once the dependencies are installed, you can run the application using:

bash
Copy code
python article_analyzer.py
Usage
Enter the Article URL:
Open the application and enter the URL of the article you want to analyze.

Fetch and Analyze:
Click on the "Fetch and Analyze" button to fetch the article, summarize it, and analyze its sentiment.

View Results:
The title, authors, publication date, summary, and sentiment of the article will be displayed in the GUI.
