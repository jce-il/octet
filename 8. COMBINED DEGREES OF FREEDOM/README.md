## Forward & Inverse Kinematics
Inverse Kinematics describes equations that produce angles to position a robotic arm on a specific xyz-coordinate. In other words: it is an algorithm (a function for example) that takes an xyz-coordinate as well as the length of the arm segments as parameters and returns the angles of the arm joints.

Forward Kinematics does the opposite. It takes angles and the length of the arm segments as inputs and then outputs an xyz-coordinate.

Inverse Kinematics and Forward Kinematics are used in robotics as well as in computer animation to animate objects in physical and in virtual spaces.

All the code in this project is in Python and requires the SciPy and vPython libraries for math and visualization respectively.

The Inverse Kinematics function in Python as well as a visualization function using vPython was written by [Yaouen Fily](http://people.brandeis.edu/~yffily/html/index.html) specifically for this project.
