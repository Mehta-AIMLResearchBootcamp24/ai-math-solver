import pandas as pd
import numpy as np
from math import floor

'''
    #   INSTALL LIBRARIES
    conda create -n ai-math-solver
    conda install pandas
    conda install numpy

    #   RUN CODE
    conda activate ai-math-solver
    cd /.../ai-math-solver
    python preprocessing.py
'''


# Final preprocessed data
# Note: some problems are repeated because they contain different solutions

data = pd.read_csv('C:/Users/Wasiu/OneDrive/Desktop/Projects/MehtaPlus/ai-math-solver/parsed_ArtOfProblemSolving.csv')  # REPLACE WITH YOUR OWN FILEPATH
data2 = data.drop(columns=['problem_id', 'answer'])


finalset1 = data2.copy()
# Use boolean indexing to filter the DataFrame. Code below removes all problems that are higher than problem 15, removes AJSME problems, and removes AHSME problems
finalset1[finalset1['link'].apply(lambda x: int(x.split('_')[-1]) > 15 or x.split('_')[1] == 'AJHSME' or x.split('_')[1] == 'AHSME')] = np.nan
finalset1 = finalset1.dropna()

'''Problems faced: One challenge was choosing problems that were problem 15 or below. The problem numbers
were a part of the link, and so we had to extract these numbers using the apply method, the lambda function, and the
split method to separate the link components.

Another problem we faced was sorting out only the competitions that we needed, as there were competitions other than
AMC. For this, we had to use an equivalent process as above to extract competition names we didn't want.
'''



finalset1["prompts"] = "<s> [INST] " + finalset1['problem'] + " [/INST] " + finalset1['solution'] + 'which gives answer letter ' +  finalset1["letter"] + " </s>"



datalength = len(finalset1.index)
Eightypercent = floor(datalength * 0.8)
# Twentypercent = datalength - Eightypercent


traindata = finalset1.iloc[:Eightypercent:]
traindata = traindata.drop(columns=['problem', 'link', 'solution', 'letter'])

testdata = finalset1.iloc[Eightypercent::]

traindata.to_csv("cleaned_ArtOfProblemSolvingTrain.csv")
testdata.to_csv("cleaned_ArtOfProblemSolvingTest.csv")

# print(finalset1.head())
