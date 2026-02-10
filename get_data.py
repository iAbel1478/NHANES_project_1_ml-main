import pandas as pd

mdf = pd.read_csv('data/linked_mortality_file_1999_2000.csv') # Load mortality file
print( mdf.head() )

gdf = pd.read_sas("data/DEMO.xpt", format="xport") # Load demographics file
print( gdf.head() )

df = gdf.merge(mdf, on="SEQN", how="inner") # Merge mortality and demographics on SEQN variable
print( df.head() )