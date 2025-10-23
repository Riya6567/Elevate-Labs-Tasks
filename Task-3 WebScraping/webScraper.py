import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

# Step 1: Fetch the HTML content
response = requests.get(URL)

# Check if request was successful
if response.status_code == 200:
    html_content = response.text

    # Step 2: Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Step 3: Extract headlines (BBC uses <h2> for top headlines)
    headlines = []
    for h2_tag in soup.find_all("h2"):
        headline = h2_tag.get_text().strip()
        if headline:
            headlines.append(headline)

    # Step 4: Save to a .txt file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for line in headlines:
            file.write(line + "\n")

    print(f"Successfully scraped {len(headlines)} headlines.")
    print("Headlines saved in 'headlines.txt'")

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
