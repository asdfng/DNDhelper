[06/23/23-17:49] Log Initialized
[06/23/23-17:49] I'm going to start by making the system local, but in the future I'd like to connect it to a discord bot
[06/23/23-17:51] So a few things to consider before working on code, what am I trying to accomplish?
[06/23/23-17:52] I was to this program to track a few things -> buffs/debuffs, health, rounds
[06/23/23-17:53] for buffs/debuffs -> who has it, and for how long
[06/23/23-17:54]  I'll need to be able to define, who the buff is on and how long it will be active for
[06/23/23-17:58] Aside: I'll also need a way to store session information and launch at a later date
[06/23/23-18:01] Making the buff document I should make the character class
[06/23/23-18:02] first things first, I should work on a wireframe for the terminal interface
[06/23/23-18:02] Then I can thing about how the code will look
[06/23/23-18:50] I've got a good idea of what I want the screens to look like for now so I start making those first
[06/23/23-19:32] Added the basic outline for the main screen but I'd like to add some more stuff for making it look pretty
[06/23/23-20:30] decided to add an exit screen, and a nice looking header
[06/23/23-20:40] Now that I have the menu_screen made I want to start on the load_game screen
[06/23/23-20:41] That will force me to have to learn how to store and modify information using python
[06/23/23-20:42] maybe I can also store meta information in the log, I'm thinking something like SQL but there might be a better way
[06/23/23-21:05] after looking over it I'll probably go with SQLlite
[06/25/23-11:23] I'm thinking of what the modifiers class needs to keep recorded
[06/25/23-11:24] It needs the name, the type, as in buff or debuff, the effect(?)
[06/25/23-11:24] not sure if I need to worry about the effect right now cause there's a bunch of different ones
[06/25/23-11:24] maybe just for now, just add description?
[06/25/23-11:25] then I don't need to worry about the 'effects' just keeping the description logged
[06/25/23-11:26] something I will include is duration, just cause then I can keep track of the buffs current duration
[06/25/23-11:27] actually, is that something I should keep in the character class?
[06/25/23-11:27] maybe I should have a inbetween class?
[06/25/23-11:28] That could be and effect class, which would contain buff and then the time of the buff right? or maybe I should have a duration class?
[06/25/23-11:29] Each class should hold to the single responsibility principle, so I would have effect, which handles duration and mods where a mod could be a buf or debuff
[06/25/23-11:30] dang lol, I'm gonna need to make another flowchart just for the data structure ugh
[06/25/23-11:48] I added a few more files, duration, and effects
[06/25/23-11:48] I'm going to use effects as a container for duration and modifiers. That way I can keep track of the duration for each seperate modifier.
[06/25/23-11:53] I also need to start thinking about how an effect is instantiated
[06/25/23-11:55] I'm thinking there will be a button that will say add new effect, then you would select the buff and the duration
[06/25/23-11:55] you should be able to select either a buff that currently exists or make a new buff
[06/25/23-11:56] when entering the duration the user should have the option for rounds, minutes, hours
[06/25/23-12:01] Should I loop DR under the mod class? since technically it is a permanent effect
[06/25/23-12:01] technically that's not true, it could also be a spell or limited by the amount of damage someone takes
[06/25/23-12:02] I probably will have a DR class that is seperate from mods then, and handle that in mods
[06/25/23-12:03] Or maybe I should just make duration handle that? Since there's just a bunch of different duration types
[06/25/23-12:03] that would make the most sense in my opinion
[06/25/23-12:05] if that's the case mod could have different types right now, DR, TEMPHP, etc...
[06/25/23-12:05] then I could just keep everything in mod, though that violates SOLID right?
[06/25/23-12:07] actually maybe not, since it's just keeping track of the type right?
[06/25/23-12:08] it should probably be up to the character class to use the type information and duration information to apply it to the character properly
[06/25/23-12:08] or maybe there should be another class that performs all those calculations?
[06/25/23-12:14] since the calculations will only ever be done on one character I'm just going to have one class for it
[06/25/23-12:15] I'm going to move DR to mods, and probably give it it's own class too just since there are so many types
[06/25/23-12:20] So here's what I have, I have mod that I want to handle DR, and Health
[06/25/23-12:22] if DR is of a specific type I want the system to know so it can keep that type of damage from being taken
[06/25/23-12:33] Now that I know how this works, what I'll do is make derived classes, DRmod, HealthMod, InherintMod (derivative of DR mod)
[06/25/23-12:33]  just cause I can't think of anything that would be Inherint other than DR
[06/25/23-12:35] I'm going to add a bunch of pass statements just so the code still works for now
[06/25/23-12:48] Dang, this is going to be more than I thought, I'm also going to need a class for each game session haha
