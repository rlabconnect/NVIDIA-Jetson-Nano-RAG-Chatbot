from bs4 import BeautifulSoup

# Read the HTML file
with open('faq.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Use BeautifulSoup to parse HTML and get the text content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <div> with class="accordion-item"
accordion_items = soup.find_all('div', class_='accordion-item')

formatted_text = ""
for item in accordion_items:
    # Extract the text from <h2> and <div class="content">
    header_text = item.find('h2').get_text(strip=True)
    content_text = item.find('div', class_='content').get_text(strip=True)

    # Append to the formatted_text with a comma after <h2> and a new line after each <div class="accordion-item">
    formatted_text += f"{header_text}, {content_text}\n"

# Save the formatted text to a new file
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(formatted_text)
