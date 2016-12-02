import requests
from bs4 import BeautifulSoup

url = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
req = request.get(url) ### What is request? you mean requests? 
html = req.content
soup = BeautifulSoup(html, "html.parser")

for result in soup.find_all("tr", "election_item"):
    id_number = result["id"].split("-")[2]
    year = result.find("td","year first").contents[0]
    print(id_number,year)
    
### File output in ELECTION_ID ??