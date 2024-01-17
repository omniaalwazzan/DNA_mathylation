
import xgboost
import shap
import pandas as pd
import matplotlib.pyplot as plt
import torch.nn as nn


#%%

path = r'\PhD progress\DNA_methyalation\mVal_cv_feat.csv' #mVal_cv_feat
datasets= pd.read_csv(path,index_col=0)

#%%
X = datasets.iloc[:, 0:-1]
y = datasets.iloc[:, -1]#.astype(dtype=np.float)



#%%
# train an XGBoost model
model = xgboost.XGBRegressor().fit(X, y)
#%%
# explain the model's predictions using SHAP
# (same syntax works for LightGBM, CatBoost, scikit-learn, transformers, Spark, etc.)
explainer = shap.Explainer(model)
shap_values = explainer(X)
#%%
# visualize the first prediction's explanation
shap.plots.waterfall(shap_values[1000])
#%%
shap.plots.force(shap_values[0])
#%%

shap.plots.beeswarm(shap_values)
#%%

shap.plots.bar(shap_values)
#%%
