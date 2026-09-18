import pandas as pd
from scipy.stats import spearmanr
df=pd.DataFrame({
    'X': [10,20,30,40,50],
    'Y': [12,24,33,45,60]})
corr_value,p_val=spearmanr(df['X'],df['Y'])
print(f"spearman coefficient:{corr_value}")
print(f"p_value:{p_val}")