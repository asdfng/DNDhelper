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
