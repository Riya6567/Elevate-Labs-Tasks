# Web Scraper for News Headlines

## 📘 Project Overview
This project is a simple **web scraper** that automatically collects the **latest news headlines** from a public news website using **Python**, **requests**, and **BeautifulSoup**.  
The scraped headlines are saved into a `.txt` file for further analysis or record keeping.

---

## 🧠 Objective
To **automate the collection of top headlines** from a news website and store them in a text file.

---

## ⚙️ Tools & Technologies
- **Python 3**
- **requests** → to fetch the webpage HTML  
- **BeautifulSoup (bs4)** → to parse and extract data from HTML  

---

## 🧩 Key Concepts
- HTTP Requests  
- Web Scraping  
- HTML Parsing  
- File Handling in Python  

---

## 📝 Implementation Steps

1. **Fetch HTML**
   - Use the `requests` library to send an HTTP GET request to a news website (e.g., [BBC News](https://www.bbc.com/news)).

2. **Parse HTML**
   - Use `BeautifulSoup` to parse the HTML structure and extract all the `<h2>` tags that contain news headlines.

3. **Store Headlines**
   - Write the extracted headlines into a text file named `headlines.txt`.

---
