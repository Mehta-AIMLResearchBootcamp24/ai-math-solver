import pandas as pd

data = pd.read_csv("C:\\Users\\Wasiu\\OneDrive\\Desktop\\Projects\\MehtaPlus\\ai-math-solver\\parsed_ArtOfProblemSolving.csv")      #   REPLACE WITH YOUR OWN FILEPATH

data = data.drop(columns=['problem_id', 'answer'])

data['problem_no'] = data['link'].apply(lambda x: int(x.split("_")[-1]))
data['test'] = data['link'].apply(lambda x: x.split("/")[-2])

data = data.drop(data[data.problem_no > 15].index)

data.to_csv("cleaned_ArtOfProblemSolving.csv")