A ROMHack with the end goal of making a more inclusive Harvest Moon for LGBTQ+ identities.

Currently planned features: 
  1: The ability to select your sprite between the "Boy" version of the game and the "Girl" version of the game with no further impact.
  2: The ability to select the pronouns used in reference to your character in dialog.
  3: The ability to choose your orientation, impacting which characters will be eligible spouses.
  4: Fix some rough translation issues, as well as remove the sexism present in the "Girl" version of the game.
  
Potentially more to come, depending on how development goes!

Progress so far:

We've worked out a rough text dump. No work has gone into changing the dialog as of now, but for the most part we understand how text display works and, with a bit of effort, could start replacing dialog if we wanted to. This is a task for much later.

We've found the color code used for the player's sprite, and have a decent understanding on how color is displayed now. Confident that we could edit the player's colors at will with our current understanding, after some brief testing.

We've found the game's graphical data. (at the very least a large portion of character sprites, animal sprites, player sprites, and character portraits, plus clock UI assets, television assets, and a lot more that I haven't fully worked out yet) I've managed to pinpoint the player sprites and have started work on making a nice easy to reference sprite sheet for the player's sprite and all their animations.

Current things that I want to try tackling:

I want to work out *how* the color code gets applied to the sprite. I feel like this will be very important when we start adding the other player sprite in, as well as hopefully giving us some insight into how the whole file comes together.

I'd also like to make efforts towards creating a little debugger for the sake of testing. Being able to set event flags would be immeasurably useful for testing dialog. I've got ideas for this, however my own programming knowledge is still developing, so this might take a bit to become a reality.
