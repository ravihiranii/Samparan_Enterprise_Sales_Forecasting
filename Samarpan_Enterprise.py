
import pandas as pd

df = pd.DataFrame()

df = pd.read_excel(r'C:\Users\Abhay\Downloads\Prayag\Prayag Update\Book1.xlsx')

print(df.head())

# Changing a Datatype:
df['Selling Price'] = df['Selling Price'].astype('int64')
print(df['Selling Price'].dtype)

# Creating a new column & using cummulative sum method:
df['Cummulative Selling Price'] = df['Selling Price'].cumsum()
print(df.head(25))

# Export dataframe into excel file: 
df.to_excel('Samarpan_Enterprise.xlsx',index=False)