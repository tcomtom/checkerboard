# Checkers
A simple checkerboard using Flask routes.

1. http://localhost:5000 - should display 8 by 8 checkerboard
2. http://localhost:5000/4 - should display 8 by 4 checkerboard
3. http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 4. 10 checkerboard.  Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)