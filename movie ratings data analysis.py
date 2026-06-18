import pandas as pd
df=pd.read_excel("Movie Ratings data analysis.xlsx")

#Highest Rated Movie
high_rated_movie=df.sort_values(by="Rating",ascending=False).head()

#Average rating per genre
avg_rating=df.groupby("Genre")["Rating"].mean().sort_values(ascending=False)

#Top Movies after 2015
top_movies_after_2015=df[df["Year"]>2015].sort_values(by="Rating",ascending=False).head()

#Most Popular Genre
most_popular_genre=df.groupby("Genre")["Votes"].sum().sort_values(ascending=False)
print("Highest Rated Movie:\n",high_rated_movie)
print("\nAverage rating per genre:\n",avg_rating)
print("\nTop Movies after 2015:\n",top_movies_after_2015)
print("\nMost Popular Genre:\n",most_popular_genre)



