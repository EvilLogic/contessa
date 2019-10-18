# contessa

## A Discord Elo Bot

A very simple python bot that allows you to perform multiplayer elo calculations.
Only supports the command '&score [names]' where names is as many names as you would like, ordered by performance.
E.g. if four players played a game, player3 came in 1st, player2 came in 2nd, player4 came in third, and player1 came in 1st you would run '&score player3 player2 player4 player1'

This also only works in the 'coup' channel of your server.

~~~
[DEFAULT]
token = NjM0NTkwNDIzNTc4MzEyNzI1.XakueQ.gzzLnJ4YHeudIKbseQ0zj7QONgE
channel = coup

[SCORES]
~~~

Requires installing the pip packages configparser, elo, and discord
