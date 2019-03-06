### Running the sloganverse App
Go to the directory where main.py is(cd '07 Sloganverses').
Type 'python main.py' at a terminal 
Copy paste the ip which is returned on the terminal in a browser, press enter
Enter your data and click on the yellow button 

**Step 1: What is does**
* The LSA code of slogan analysis is applied to 574 verses from Charles Bukowski poems and ONE slogan
We search the slogan ordered on the axis of the first component of LSA and associated it 
with the verse coming right after in the ordered list of verse
we then display the slogan followed by the verse
As slogan are typically super positive and Bukowski verse super critical the juxtaposition effect is funny
It is not a random retrieval of verse which gives a bit of mistery to this

**Step 2: The files**
Four files are needed for this to work: 3 are in the '05 Delay app' directory, 1 in 'templates' subdirectory of '05 Delay app'.
1. `main.py` - This is the main Python code that uses Flask and calls py_complete.py to use the model
2. `py_complete.py` - This is a separate Python script that reads in the bukowski verse get the slogan
as input and return a verse 
3. `bukowski1.xlsx` - the file containing the verses
4. `index.html` (in a templates folder)- This is the webpage that will be able to take inputs for the model and output a result on the webpage
