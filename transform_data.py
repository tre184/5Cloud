import pandas as pd


# Load data from local CSV
df = pd.read_csv('./dags/files/paris_wifi.csv', delimiter=';')

# Display the DataFrame schema using df.info()
print("DataFrame Info:")
df.info()

# Display descriptive statistics using df.describe()
print("\nDescriptive Statistics:")
df.describe()

# Display the data types of each column using df.dtypes
print("\nData Types:")
print(df.dtypes)

# Display the first few rows of the DataFrame using df.head()
print("\nFirst Few Rows:")
print(df.head())

# Drop the 'geo_shape' column
df = df.drop(columns=['geo_shape'])

# Function to separate geo_point_2d into longitude and latitude
def separate_geo_point(geo_point):
    latitude, longitude = geo_point.split(', ')
    return pd.Series({'latitude': float(latitude), 'longitude': float(longitude)})

# Apply the function to the 'geo_point_2d' column
df[['latitude', 'longitude']] = df['geo_point_2d'].apply(separate_geo_point)

# Drop the original 'geo_point_2d' column
df = df.drop(columns=['geo_point_2d'])

# Rename the column
df = df.rename(columns={'etat2': 'etat'})
df = df.rename(columns={'arc_adresse': 'adresse'})
# Change the data types of the columns
df = df.astype({
    'nom_site': 'string',
    'adresse': 'string',
    'cp': 'string',
    'idpw': 'string',
    'nombre_de_borne_wifi': 'int',
    'etat': 'string'
})

# Display the data types of each column using df.dtypes
print("\nData Types:")
print(df.dtypes)

# Display the column names using df.columns
print("\nColumn Names:")
print(df.columns)
print(df)

# Save the transformed data
df.to_csv('./data/paris_wifi_data.csv', index=False)