"# MineSweeper" 
<<<<<<< HEAD
"MINESWEEPER" 
=======
MINESWEEPER
============

Description
------------

The objective in Minesweeper is to find and mark all the mines hidden under the grey squares, in the shortest time possible. This is done by clicking on the squares to open them. Each square will have one of the following:

 + A mine, and if you click on it you'll lose the game.
 + A number, which tells you how many of its adjacent squares have mines in them.
 + Nothing. In this case you know that none of the adjacent squares have mines, and they will be automatically opened as well.
 + It is guaranteed that the first square you open won't contain a mine, so you can start by clicking any square. Often you'll hit on an empty
   square on the first try and then you'll open up a few adjacent squares as well, which makes it easier to continue.
 + Then it's basically just looking at the numbers shown, and figuring out where the mines are.

Rules
------

There are essentially five actions you can take in Minesweeper:

* Open a square. This is done simply by left clicking on a square.

* Marking a square as a mine. This is done by right clicking on a square. A little mine icon will show up there.

* Marking a square with a question mark. This is done by right clicking twice on a square, or right clicking once on a square that's 
  already marked as a mine. Question marks are useful to mark squares you're not absolutely sure are mines, but want to make sure you
  don't accidentally open them.

* Clear any marks. Again, right click on the square. Right clicking cycles through the following states: Bomb, Question Mark, Clear.

* Opening all remaining adjacent squares to a number square. If for example you have a square with the number 1 and you have already marked
  one mine in one of the adjacent squares you can left click on the 1 square and the remaining adjacent squares will all be opened. This can
  save a lot of time while trying to quickly clear out squares. If you press on a number where not all adjacent mines have been marked,
  e.g. the number is 3 and you've only flagged one adjacent square, then the squares will not be opened, to prevent you from accidentally
  clicking on a number and blowing yourself up! In the old Windows version of this game you used both mouse buttons together to perform this
  action, but here we just use a normal left-click.

Winning
--------
 
* You've won the game when you've opened all squares that don't contain a mine. If you've opened all the empty/nr squares but haven't flagged
  the mine squares remaining, they will be auto-flagged and you have won.

* So, essentially flagging is not required, it's only there to help you keep track of where you think the mines are. The real way to win is 
  open all the non-mine squares. 
>>>>>>> fb3178c687f30c3f794168d4186fd9a0291b3a26
