# Instructions to use
There are two python scripts which both accomplish the same thing using slightly different programming approachs.  `main.py` uses a procedural approach, whereas `functional-approach.py` uses a functional programming approach as the name suggests.

On systems in which python3 is installed, either of these scrips can be run from the command line.  While in the containing directory use (for the main.py example) `python3 main.py` (or just `./main.py` in systems which allow executable scripts like Linux/unix systems.  Ensure that the executable-mode bit is set for the scripts using `chmod +x *.py`).  There is an optional command-line argument of the "travelling instructions", which defaults to the value provided in `Adventurer Path.md` when no argument is provided.



# Adventurer Journey - Back End
Please complete the story below and create a program to solve the problem. Commit any work back to the remote no later than 48 hours before the next interview.

*Please use whatever languages, references and tooling you would like to complete the story.*

## Story Instructions
You are an adventurer standing in the center of a map facing North, and you’re trying to weave through the terrain to your final destination. You have the directions to your destination indicating the number of steps and the direction to travel.

Adventurer Path & Instructions - [./Adventurer Path.md](./Adventurer%20Path.md)

Given the Path Instructions above, programmatically parse the instructions and determine what is the Euclidean (straight line) distance from your starting point to the destination in steps?

**Tech Notes:**
- Use whatever languages, references and tooling you would like.
- Provide any needed instructions to run program.
- Do not round to the nearest step.
- After program executes the answer should be returned.
