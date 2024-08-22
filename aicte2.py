import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = input("Enter the URL of the webpage you want to scrape: ")
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

page_title = soup.title.string
print("Page Title:", page_title)

page_text = soup.get_text()
print("Page Text:", page_text)

links = soup.find_all('a')
for link in links:
    href = link.get('href')
    link_text = link.string
    print(f"Link: {link_text} - URL: {href}")

image_save_dir = "C:/Users/ASUS/OneDrive/Pictures/Screenshots"

if not os.path.exists(image_save_dir):
    os.makedirs(image_save_dir)

images = soup.find_all('img')
for index, image in enumerate(images):
    img_src = image.get('src')
    full_img_src = urljoin(url, img_src)
    img_alt = image.get('alt', f'No_Alt_Text_{index}')

    img_filename = os.path.join(image_save_dir, f'{img_alt}.jpg')

    img_data = requests.get(full_img_src).content
    with open(img_filename, 'wb') as img_file:
        img_file.write(img_data)

    print(f"Image saved: {img_filename}")

with open("scraped_data.txt", "w") as file:
    file.write(f"Page Title: {page_title}\n\n")
    file.write("Page Text:\n")
    file.write(page_text + "\n\n")
    file.write("Links:\n")
    for link in links:
        href = link.get('href')
        link_text = link.string
        file.write(f"{link_text}: {href}\n")
    file.write("\nImages saved to directory:\n")
    file.write(image_save_dir)

print("Data has been scraped, images downloaded, and saved to 'scraped_data.txt'.")
