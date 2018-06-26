# tech-af

It started with a question: Are startups in Nigeria truly innovating or are they just bringing the ideas
of Western Markets to a different market. It was partly inspired by [this tweet](https://twitter.com/tomjackson1988/status/1005051960570138624?s=12) by [Disrupt Africa](http://disrupt-africa.com/) [co-founder](https://twitter.com/tomjackson1988).


If you're interested, you can run this same study with other countries. I uploaded [a list of startups](https://data.world/omayeli/angelist-startups-in-africa) by African countries from Angelist. 

I followed this [Gensim tutorial](https://radimrehurek.com/gensim/tut1.html) to create a dictionary that is in the `dict` folder. [Gensim](https://radimrehurek.com/gensim/) is "a robust open-source vector space modeling and topic modeling toolkit implemented in Python." To put it simply, it's one of the libraries that came up when I googled how to get the similarity between two sentences - which is what I'm doing. I'm getting the similarities between a description of a nigerian startup and that of a US startup. I use [Pandas](https://pandas.pydata.org/) to read and manipulate the .csv files.

## Setup

- [Get Pip](https://pypi.org/project/pip/)
- Clone this repo.
- In the root folder: Install [Pandas](https://pandas.pydata.org/): `pip install pandas` and Install gensim with Pip:`pip install --upgrade gensim`
- Make a directory `corpus` in the root folder. You need to run `python create-dict.py` in the terminal to create the dictionary and the corpus. That should update or create a `startups.dict` file in the dict/ directory.
- Then run the `python compare-ng.py`. This will create a csv file in the sim-data/ directory. You can plug that into the JavaScript file in the `viz` folder to visualize it. 


It's likely that I missed something so if you have any questions, message me on [Twitter](https://twitter.com/YellzHeard)
