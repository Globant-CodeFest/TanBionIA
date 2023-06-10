import pandas as pd 

#levantar csv en 'C:\Users\user\Desktop\disasters\1900_2021_DISASTERS.xlsx - emdat data.csv' con separador ; 
#solo tiene que levantar las columnas que tienen datos, no las que estan vacias
df = pd.read_csv(r'C:\Users\user\Desktop\disasters\1900_2021_DISASTERS.xlsx - emdat data.csv', sep=';')

#drop columnas que tengan más de 10000 nans
df.dropna(axis=1, thresh=10000, inplace=True)

#plot disasters by year
#complete nulls with
#order by year
df['Total Deaths'].sum().plot(kind='bar', figsize=(20,10))

#graficar suma de muertes por año
df.groupby('Year')['Total Deaths'].sum().plot(kind='bar', figsize=(20,10))

#agrupar por década, pero no existe la columna década, crearla
df['Decade'] = df['Year']//10*10

#modelo de predicción de muertes por década
df_pred=df.groupby('Decade')['Total Deaths'].sum().iloc[:-1]
df_pred.plot(kind='bar', figsize=(20,10))
#modelo ARIMA
from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(df_pred, order=(1,1,1))
model_fit = model.fit()
model_fit.summary()
forecast = model_fit.get_forecast(steps=3)
y_pred=pd.DataFrame(index=[df_pred.index.max()+10, df_pred.index.max()+20, df_pred.index.max()+30], data=forecast.predicted_mean.values)
#graficar, pero en distintos colores los valores de df_pred y y los de y_pred. hacer una gráfica de barras con los valores de df_pred y y_pred, pero en la misma gráfica. Usar seaborn. Primero concatenar df_pred e y_pred
df_pred=pd.DataFrame(df_pred)
df_pred.columns=['Total Deaths']
df_pred.index.name='Decade'
df_pred.reset_index(inplace=True)
df_pred['type']='real'
y_pred.columns=['Total Deaths']
y_pred.index.name='Decade'
y_pred.reset_index(inplace=True)
y_pred['type']='pred'
df_pred=pd.concat([df_pred, y_pred])
import seaborn as sns
sns.barplot(data=df_pred, x='Decade', y='Total Deaths', hue='type')
#guardar la imagen, pero plt no está definido
import matplotlib.pyplot as plt
plt.savefig('pred.png')
#guardar df_pred como excel
df_pred.to_excel('pred.xlsx')



