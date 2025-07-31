import requests
from bs4 import BeautifulSoup

# Sample page — replace with actual URL from Sisu's public search
url = "https://sisu.helsinki.fi/student/courseunitsearch"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send the request
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find course titles — this will vary based on actual page structure
courses = soup.find_all("div", class_="course-unit-name")  # Adjust class name accordingly

# Print course titles
for course in courses:
    print(course.get_text(strip=True))