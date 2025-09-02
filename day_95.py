'''Regular Expressions in Python'''

import re

pattern =r"[A-Z]+nglish"
text='''During its 1905–06 season, New Brompton F.C., an English football club, competed in the Southern League Division One. The team began the season on 2 September 1905 in poor form; they failed to score in six of their first eight league games and, by midseason, they were near the bottom of the league table. In the new year, the team won three of its first seven Southern League games, but failed to score in eight of the final nine league games. New Brompton finished the season in 17th place out of 18 teams in the division. They also competed in the FA Cup, reaching the second round. The team played a total of 37 league and cup matches, winning 8, drawing 9 and losing 20. Bill Marriott was the club's top goalscorer, with four goals in the Southern League and one in the FA Cup. Joe English Walton (pictured) made the most appearances, playing in 36 of the team's 37 games. The highest attendance recorded at Priestfield Road was 5,500 for a game against Portsmouth on 27 January 1906.'''

# match=re.search(pattern,text)   #STOPS at first match
# print(match)

match=re.finditer(pattern,text)

for matches in match:
    print(matches)