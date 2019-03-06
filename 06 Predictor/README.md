### Running the predictor App
Go to the directory where main.py is(cd '06 Predictor').
Type 'python main.py' at a terminal 
Copy paste the ip which is returned on the terminal in a browser, press enter
Enter your data and click on the yellow button 

**Step 1: The model in pickle format**
* The model was created in a previous version of: 02 Predicting Company type by Slogans.ipynb
where classes were 1 to 11 instead of 15-60 in latest version
It is a logistic regression on the vectorized slogans

**Step 2: The files**
Four files are needed for this to work: 3 are in the '06 Predictor app' directory, 1 in 'templates' subdirectory of '06 predictor '.
1. `main.py` - This is the main Python code that uses Flask and calls py_GICS_predict.py 
(GICS is the) name of the classification
2. `py_GICS_predict.py` - This is a separate Python script that reads in the pickled model and the directory of words and return the classified company
3. `slogpred.p` - The pickled logistic model
4. `colonnes.p` - The pickled list of words to use to vectorized the slogan entered agains
5. `index.html` (in a templates folder)- - This is the webpage that will be able to take inputs for the model and output a result on the webpage
