# World-Cup-DS
Data Analysis on the FIFA's World Cup database since 1930 in Uruguay until the 2014 World cup in Brazil,
being split in 4 Dataframes, that show the most importants status about scoring, assisting and disciplinary measures. These
Dataframes were colected from [FIFA](http://www.fifa.com/fifa-tournaments/archive/worldcup/index.html "FIFA's Archives") and scraped using
the library *BeautifulSoup*, that the source code is available on the code **_fifa.py_** 

## Dataframe Structure
The data from the website is divided into 2 categories:
* Team Stats: that represents the team's stats as a whole 
* Individual Stats: Shows information of each player individually ~~Thats kind of obvious!~~

On the archives each category is represented with its first letter ( *t* for team and *i* for individual)
Beyond that, there are still two subcategories:
* Scoring Statistics:  Goals, assistences, penalty goals for any player that made at least one of these in a World Cup
* Disciplinary Statistics: Yellow Cards, Red Cards also for any player that received at least on of these in a World Cup 

## Some issues...

### 2014 FIFA World Cup Brazil™

Ironically the most recent database was the one that revealed the most problems to integrate with the others statistics from the other cups
and here is why: ~~Why Brazil always getting me upset? ~~

- Indexes/number ranking suddenly have dissapeared
- Position on the field wasw also removed (Role on the previous cups: Goalkeeper, Defender, MidFielder, Forward)
- No more minutes on the field during the whole competition

## Author

* Luiz Henrique Rodrigues - Meanwhile all - [loumishima](https://github.com/loumishima)

## Soon to be implemented

* Machine learning algorithms to clustering teams/players
* Preview teams strength using Qualifiers as measure
