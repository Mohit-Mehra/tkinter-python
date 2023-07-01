import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def get_news_titles():
    try:
        url = url_entry.get()
        response = requests.get(url)
        response.raise_for_status()  # Verifică dacă cererea a avut succes
        
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2')  # Modificați selectorul ('h2') în funcție de structura paginii web
        
        titles_listbox.delete(0, tk.END)  # Curăță lista de titluri anterioare
        
        for title in titles:
            titles_listbox.insert(tk.END, title.text)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An error occurred. Please check the URL and try again.")

root = tk.Tk()
root.title("News Title Downloader")
root.geometry("400x300")

url_label = tk.Label(root, text="URL:")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

download_button = tk.Button(root, text="Download", command=get_news_titles)
download_button.pack()

titles_label = tk.Label(root, text="Titles:")
titles_label.pack()
titles_listbox = tk.Listbox(root)
titles_listbox.pack()

root.mainloop()
