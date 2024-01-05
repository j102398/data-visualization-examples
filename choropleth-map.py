import plotly.express as px 
import pandas as pd 

gapminder = px.data.gapminder()  # Load the Gapminder dataset using Plotly Express's built-in dataset function

gapminder.head(15)  # Display the first 15 rows of the Gapminder dataset

# Create a choropleth map using Plotly Express.
# This map will represent life expectancy ('lifeExp') across countries and years.
# It will use country codes ('iso_alpha') to locate countries on the map.
fig = px.choropleth(gapminder,
                    locations="iso_alpha",
                    color="lifeExp",
                    scope="world",
                    hover_name="country",
                    animation_frame="year")

fig.show()  # Display the choropleth map created above
