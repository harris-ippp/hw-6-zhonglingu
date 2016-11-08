import requests
from bs4 import BeautifulSoup as bs

for line in open ("ELECTION_ID"):
    year = line.split(" ")[0]
    electionID = line.split(" ")[1].strip()
    files = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(electionID)
    resp = requests.get(files)
    soup = bs (resp.content, "html.parser")
    file_name = year+".csv"
    with open(file_name,"w") as output:
        output.write(resp.text)
