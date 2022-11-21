# Adventure game

Create a text-based adventure game where the player gets to choose from options presented to them.

The game could be set anywhere, so let your imagination wander! Is it about navigating the narrow halls of the campus, or having a fun night at Klusteri? Maybe you need to save TKO-äly ry from the brink of a budgetary catastrophe or just survive life.

You can make this as complicated as you'd like, but be aware of if-else nightmares! Consider methods and generalization, but the most important part is to have fun. If you're feeling burned out by code, you can also focus on writing the storyline for a bit.

```
You arrive at Gurula. There's two people sitting by the table. A third one lounges on the sofa. They look at you with raised eyebrows.

[1] Buy a NOCCO from RV
[2] Talk to the <Person on the Sofa>
[3] Leave

Choice > 
```

**Corresponding template:** [adventure-game.py][template]

Ideas on improvements:
- Make the game not crash when a user enters text as an input
- Having the previous decisions affect steps without having to rewrite them multiple times (managing state)
- Adding minigames to steps
- Adding fancy [text-based graphics](https://www.asciiart.eu/) or [colours](https://stackoverflow.com/a/287944)
- (advanced) Add a graphical user interface with choices as buttons

[template]: ../templates/adventure-game.py