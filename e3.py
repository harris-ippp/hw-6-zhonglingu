### Code doesn't execute as given
import panda as pd ### You mean pandas?
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

votes = []

for line in open ("ELECTION_ID"):
    year = line.split(" ")[0]
    header = pd.read_csv(year + ".csv", nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

### The following line can't even be executed
    df = pd.read_csv(year+".csv", index_col = 0,thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = 2004
    votes.append(df)

for year in range(len(votes)):
    majorVote = pd.concat([votes[year][['Democratic','Republican','Total Votes Cast','Year']]], axis = 1).head(1)
    majorVote['Republican Vote Share'] = majorVote['Republican']/majorVote['Total Votes Cast']
    if year == 0:
        voteShare = pd.concat([majorVote], axis = 1)
    else:
        voteShare = pd.concat([voteShare, majorVote], axis = 0)

ax  = voteShare.plot(x = 'Year', y = "Republican Vote Share", \
        title = "President General Election Results in Accomack County, Virginia")
ax. get_figure().savefig("accomack.png")
### Plot is wrong