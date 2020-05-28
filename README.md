# Budibak

The functionality of this programming language is to create simple 2D video games. 

# Introduction 

The project is inspired on the video game “The World’s Hardest Game” and based on our love of video games. Each level of that game it’s a different and creative challenge and that’s what we wanted to do with this project. If you dare to play “The World’s Hardest Game”, here's the link: https://www.coolmathgames.com/0-worlds-hardest-game. Good luck (you're gonna need it). 


The project helps the user create 2D platform games and helps newcomers learn about the concepts of programming. The objective of the game is for the player character to reach the goal set by the user. The project declares the levels created by the user. The levels must be written in a text file in order for it to run. The user can choose the images they want to use for each declared object.  

# Game Objects Guide
The project uses these objects:

Levels: The place where all the objects are stored. 
  There can be multiple levels on a text file. 
   When a user wants to finish writing a level and finishes declaring all the objects, the user writes “end” to finish the level. 
   
Level Attribute: Level(Name(String))

Player: The main character.  It’s the character that the user controls. The character moves with these keys: 
  
  W: moves up 
   
  A: moves left
   
   S: moves down 
   
   D: moves right
 
Player attribute: Player(xPosition(integer), yPosition(integer), imagePath(String), Behaviour(TypeDeclaration))

Behaviour:It represents the movement of the objects of the game. 
The characteristics of the movement of the object can be on a loop, continuous, or static
The user can also choose if the object suffers the effects of gravity. The effect is declared with either a true or false.  


Behaviour attribute: Behaviour(xMovement(integer), yMovement(integer), Speed(float), MovementCharacteristic(LOOP, CONTINUOUS, or DEFAULT), Gravity(boolean))

Mob: The mob are the enemies that the player avoids in the level. 
If the player touches the mob, the player dies. 

Mob attribute: Mob(xPosition(integer), yPosition(integer), imagePath(String), Behaviour(TypeDeclaration))

Object: This represents objects like the platforms, the floor, the walls, and any other normal object in a game. 
The object’s attributes can be modified based on what the user wants. 
The user can create moving platforms, and floors with so that if the player falls, the player dies. 

Object attribute: Object(xPosition(integer), yPosition(integer), imagePath(String), Behaviour(TypeDeclaration))

Goal:The goal is the object that represents the objective of the level. 
If the player touches the goal, the level is cleared and process to the next level if there is another or the game is over. 

Goal attribute: Goal(xPosition(integer), yPosition(integer), imagePath(String), Behaviour(TypeDeclaration))

# Level Sample

Level(HelloThere):

Player(60 , 525,heroball.png, Behaviour(5,5,5.0,DEFAULT, True))

Object(0, 600, awoodfloor.png, Behaviour(0,0,0.0, DEFAULT, False))

Object(420, 600, astonewall.png, Behaviour(0,0,0.0, DEFAULT, False))

Object(200, 300, astoneplat.png, Behaviour(0,0,0.0, DEFAULT, False))

Mob(200, 275, doomball.png, Behaviour(150,1,2.0, CONTINUOUS, True))

Object(45, 80, astoneplat.png, Behaviour(0,120,2.0, LOOP, False))

Object(200, 120, awoodplat.png, Behaviour(0,0,0.0, DEFAULT, False))

Object(420, 145, awoodplat.png, Behaviour(0,0,0.0, DEFAULT, False))

Object(755, 600, astoneplat.png, Behaviour(0,0,0.0, DEFAULT, False))

Object(525, 400, astonewall.png, Behaviour(0,0,0.0, DEFAULT, False))

Object(1000, 510, awoodfloor.png, Behaviour(0,0,0.0, DEFAULT, False))

Mob(615, 435, doomball.png, Behaviour(150,0,2.0, LOOP, False))

Object(635, 590, awoodplat.png, Behaviour(0,0,0.0, DEFAULT, False))

Goal(750, 575, arockorange.png, Behaviour(0,0,0.0, DEFAULT, False))

end

# To Start Playing
To run the game, the user writes the levels in a text file. 
Then, run the parser.py file and write the path of the text file. 

# Demo video
<iframe width="560" height="315" src="https://www.youtube.com/embed/t7fpgbFgL6M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Commercial video
<iframe width="560" height="315" src="https://www.youtube.com/embed/BnlcNkUZYNw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
