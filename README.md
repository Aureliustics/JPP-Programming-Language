<h1>J++ Programming Language</h1>
<h3>My attempt on creating an interpreted programming language called J++ made using Python (also an interpreted language) which gets interpreted by Skulpt on CodeHS. Triple layer interpretation 🤯. Definitely very messy code but I just wanted to see if I could make it in such a restraining environment like CodeHS. Very basic functionality and is more of a proof of concept than anything viable.</h3>

<h1>Usage</h1>
<ul>
  <li>Must be ran in a <a href="https://codehs.com/" target="_blank">CodeHS</a> sandbox</li>
  <li>Once logged into Codehs, click "Sandbox" in the navigation bar</li>
  <li>Click "Create Program" then select "Python (turtle)" and create program</li>
  <li>Copy and paste the code into your sandbox then run</li>
  <li>Try some of the J++ code below</li>
</ul>

<h1>Code Examples</h1>
```
jout << "Hello World"; # Inspriation from cout from C++. Basically just prints a string to console. #
jin << x; # Same thing as cin from C++. Takes input for variable. #

loop(4){
    jout << "Hello World": # prints "Hello World" four times #
};

move(50, forward); # creates a square #
move(50, up);
move(50, backward);
move(50, down);

square(50, center); # create a square centered on the turtle with length of 50px #

triangle(25, bottom); # create a triangle right under the turtle with length of 25px #

9 * 9; # You can evaluate mathematical expressions but with only 2 operands and without order of operations #
15 / 5;
2 + 2;
```

