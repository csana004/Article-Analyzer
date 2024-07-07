import tkinter as tk
from tkinter import messagebox, ttk
import nltk
from textblob import TextBlob
from newspaper import Article
import threading


nltk.download('punkt')


# Function to fetch article and analyze sentiment
def fetch_article():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    # Reset previous content
    clear_content()

    # Start the progress bar
    progress_bar.start()

    def fetch_and_analyze():
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()

            title_var.set(f"Title: {article.title}")

            # Display authors in a frame
            authors_var.set(f"Authors: {', '.join(article.authors)}")
            authors_label.config(text=authors_var.get())

            # Display publication date in a frame
            pub_date_var.set(f"Publication Date: {article.publish_date}")
            pub_date_label.config(text=pub_date_var.get())

            # Display summary in a frame
            summary_var.set(f"Summary: {article.summary}")
            summary_label.config(text=summary_var.get())

            # Analyze sentiment
            analysis = TextBlob(article.text)
            polarity = analysis.polarity
            sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
            sentiment_var.set(f"Sentiment: {sentiment} (Polarity: {polarity:.2f})")
            sentiment_label.config(text=sentiment_var.get())

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        finally:
            # Stop the progress bar
            progress_bar.stop()

    # Run the fetching and analysis in a separate thread
    threading.Thread(target=fetch_and_analyze).start()


def clear_content():
    # Clear all labels
    title_var.set("")
    authors_var.set("")
    pub_date_var.set("")
    summary_var.set("")
    sentiment_var.set("")


# Set up the Tkinter window
root = tk.Tk()
root.title("Scrollable Article Sentiment Analyzer")

# Styling
root.geometry("800x600")  # Set initial window size
root.configure(bg="#f0f0f0")  # Set background color

# URL entry
url_label = tk.Label(root, text="Enter Article URL:", bg="#f0f0f0", font=("Arial", 12))
url_label.pack(pady=(20, 5))
url_entry = tk.Entry(root, width=80, font=("Arial", 12))
url_entry.pack(pady=5)

# Fetch button
fetch_button = tk.Button(root, text="Fetch and Analyze", command=fetch_article, bg="#4CAF50", fg="white",
                         font=("Arial", 12))
fetch_button.pack(pady=10)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_content, bg="#f44336", fg="white", font=("Arial", 12))
clear_button.pack(pady=10)

# Create a frame to hold the canvas and scrollbars
scrollable_frame = tk.Frame(root, bg="#e0e0e0", padx=20, pady=20)
scrollable_frame.pack(pady=20, fill=tk.BOTH, expand=True)

# Horizontal scrollbar
xscrollbar = ttk.Scrollbar(scrollable_frame, orient=tk.HORIZONTAL)
xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Vertical scrollbar
yscrollbar = ttk.Scrollbar(scrollable_frame, orient=tk.VERTICAL)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Canvas to hold labels
canvas = tk.Canvas(scrollable_frame, bg="#e0e0e0", highlightthickness=0, xscrollcommand=xscrollbar.set,
                   yscrollcommand=yscrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure scrollbars to work with canvas
xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)

# Frame inside canvas to contain labels
content_frame = tk.Frame(canvas, bg="#e0e0e0")
canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

# Title label
title_var = tk.StringVar()
title_label = tk.Label(content_frame, textvariable=title_var, wraplength=700, justify='left',
                       font=("Arial", 14, "bold"), bg="#e0e0e0")
title_label.pack(pady=(0, 10), anchor=tk.W)

# Frame for publication date
pub_date_var = tk.StringVar()
pub_date_frame = tk.Frame(content_frame, bg="#e0e0e0")
pub_date_frame.pack(pady=(0, 10), anchor=tk.W)
pub_date_label = tk.Label(pub_date_frame, textvariable=pub_date_var, wraplength=700, justify='left', font=("Arial", 12),
                          bg="#e0e0e0")
pub_date_label.pack()

# Frame for authors
authors_var = tk.StringVar()
authors_frame = tk.Frame(content_frame, bg="#e0e0e0")
authors_frame.pack(pady=(0, 10), anchor=tk.W)
authors_label = tk.Label(authors_frame, textvariable=authors_var, wraplength=700, justify='left', font=("Arial", 12),
                         bg="#e0e0e0")
authors_label.pack()

# Frame for summary
summary_var = tk.StringVar()
summary_frame = tk.Frame(content_frame, bg="#e0e0e0")
summary_frame.pack(pady=(0, 10), anchor=tk.W)
summary_label = tk.Label(summary_frame, textvariable=summary_var, wraplength=700, justify='left', font=("Arial", 12),
                         bg="#e0e0e0")
summary_label.pack()

# Frame for sentiment analysis
sentiment_var = tk.StringVar()
sentiment_frame = tk.Frame(content_frame, bg="#e0e0e0")
sentiment_frame.pack(pady=(0, 10), anchor=tk.W)
sentiment_label = tk.Label(sentiment_frame, textvariable=sentiment_var, wraplength=700, justify='left',
                           font=("Arial", 12), bg="#e0e0e0")
sentiment_label.pack()


# Update canvas scroll region
def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


content_frame.bind("<Configure>", update_scroll_region)

# Progress bar
progress_bar = ttk.Progressbar(root, mode="indeterminate")
progress_bar.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
