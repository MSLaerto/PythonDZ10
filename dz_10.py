import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()


pd.get_dummies(data['whoAmI']).head() # C get_dummies

pd.DataFrame({'robot': data['whoAmI'] == 'robot' , 'human': data['whoAmI'] == 'human'}).astype(int).head() # Без get_dummies
