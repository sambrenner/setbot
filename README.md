# Setbot

A program to play the card came [Set](https://en.wikipedia.org/wiki/Set_%28game%29).

## Running the program

    python setbot.py
    
Currently Setbot has its cards hard-coded to test the algorithm. Eventually it will accept parameters.

## About

Set is a card game in which the goal is to find three cards (a "set") from the 12 cards visible. All of the cards have four properties, described below, and a set is a group of three cards where each card's properties have values that are the same as or different from the rest.

## Rules

Instead of referring to the actual properties of the Set cards (color, shape, quantity and shading), we will abstract them out into numbers. This way, every card can be encoded as [a,b,c,d], where the list index maps to the property.

```
0: shape
   0: squiggle
   1: pill
   2: diamond

1: color
   0: purple
   1: green
   2: red

2: quantity
   0: 1
   1: 2
   2: 3

3: shading
   0: blank
   1: striped
   2: solid
```

For example, this is a set:

```
  [0,0,2,1]
  [0,2,2,0]
  [0,1,2,2]
   \ \ \ \_ all different
    \ \ \__ all the same
     \ \___ all different
      \____ all the same
```

And this is not a set:

```
  [0,0,2,1]
  [1,2,1,0]
  [0,1,2,2]
   \ \ \ \_ all different
    \ \ \__ two of one, one of another
     \ \___ all different
      \____ two of one, one of another
```

## Solution

The pseudocode of a solution is as follows:

1. Pick a card
* Pick another card
* Figure out what hypothetical card would be needed to make a set
* For the remaining cards, check if they equal the hypothetical card
* If so, Set found.
* Either way, continue with the next two cards

## Next Steps

* Presumably the Set detection algorithm can be optimized
* Computer vision to find sets in a photograph of a Set game
* Wrap it all in a web interface
