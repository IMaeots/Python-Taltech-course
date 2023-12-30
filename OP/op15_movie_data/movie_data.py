"""What should we watch, Honey?..."""
import re

import pandas as pd


def raise_error():
    """Raise value error."""
    raise ValueError("Value error.")


class MovieData:
    """
    Class MovieData.

    Here we keep the initial data and the cleaned-up aggregate dataframe.
    """

    def __init__(self):
        """
        Class initialization.

        Here we declare variables for storing initial data and a variable for storing
        an aggregate of processed initial data.
        """
        self.movies = None or pd.DataFrame
        self.ratings = None or pd.DataFrame
        self.tags = None or pd.DataFrame
        self.aggregate_movie_dataframe = None or pd.DataFrame

    def load_data(self, movies_filename: str, ratings_filename: str, tags_filename: str) -> None:
        """
        Load Data from files into dataframes.

        Raise the built-in ValueError exception if either movies_filename, ratings_filename or
        tags_filename is None.

        :param movies_filename: file path for movies.csv file.
        :param ratings_filename: file path for ratings.csv file.
        :param tags_filename: filepath for tags.csv file.
        :return: None
        """
        self.movies = pd.read_csv(movies_filename)
        self.ratings = pd.read_csv(ratings_filename)
        self.tags = pd.read_csv(tags_filename)

        if self.ratings is None or self.tags is None or self.movies is None:
            raise_error()

    def create_aggregate_movie_dataframe(self, nan_placeholder: str = '') -> None:
        """
        Create an aggregate dataframe from frames self.movies, self.ratings and self.tags.

        No columns with name 'userId' or 'timestamp' allowed. Columns should be in order
        'movieId', 'title', 'genres', 'rating', 'tag'. Several lines in the tags.csv file
        with the same movieId should be joined together under the tag column.

        When created correctly, first 3 rows of the dataframe should look like below (some spaces omitted so as not
        to create a style error):
                movieId             title                                       genres  rating              tag
        0             1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0  pixar pixar fun
        1             1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0  pixar pixar fun
        2             1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.5  pixar pixar fun

        :param nan_placeholder: Value to replace all np.nan-valued elements in column 'tag'.
        :return: None
        """
        # Format ratings and tags.
        self.ratings = self.ratings.drop(columns=['userId', 'timestamp'], axis=1)
        self.tags = (self.tags.drop(columns=['userId', 'timestamp'], axis=1)
                     .groupby("movieId").agg({'tag': lambda x: ' '.join(x)}))

        # Aggregate movie dataframe.
        movie_dataframe = self.movies.merge(self.ratings, on="movieId", how="left")
        self.aggregate_movie_dataframe = movie_dataframe.merge(self.tags, on="movieId", how="left")
        self.aggregate_movie_dataframe['tag'] = self.aggregate_movie_dataframe['tag'].fillna(nan_placeholder)

    def get_aggregate_movie_dataframe(self) -> pd.DataFrame | None:
        """
        Return aggregate_movie_dataframe variable.

        :return: pandas DataFrame
        """
        return self.aggregate_movie_dataframe

    def get_movies_dataframe(self) -> pd.DataFrame | None:
        """
        Return movies dataframe.

        :return: pandas DataFrame
        """
        return self.movies

    def get_ratings_dataframe(self) -> pd.DataFrame | None:
        """
        Return ratings dataframe.

        :return: pandas DataFrame
        """
        return self.ratings

    def get_tags_dataframe(self) -> pd.DataFrame | None:
        """
        Return tags dataframe.

        :return: pandas DataFrame
        """
        return self.tags


def extract_year_from_title(title):
    """Extract the year from the title."""
    year_pattern = re.compile(r'\((\d{4})\)')
    match = year_pattern.search(title)
    if match:
        return int(match.group(1))
    return None


class MovieFilter:
    """
    Class MovieFilter.

    Here we keep the aggregate dataframe from MovieData class and operate on that data.
    """

    def __init__(self):
        """
        Class initialization.

        Here we only need to store the aggregate dataframe from MovieData class for now.
        For OP part, some more variables might be a good idea here.
        """
        self.movie_data = None or pd.DataFrame
        self.median_rating = None or float
        self.average_rating = None or float

    def set_movie_data(self, movie_data: pd.DataFrame) -> None:
        """
        Set the value of self.movie_data to be given argument movie_data.

        :param movie_data: pandas DataFrame object
        :return: None
        """
        self.movie_data = movie_data

    def filter_movies_by_rating_value(self, rating: float, comp: str) -> pd.DataFrame | None:
        """
        Return pandas DataFrame of self.movie_data filtered according to rating and comp string value.

        Raise the built-in ValueError exception if rating is None or < 0.
        Raise the built-in ValueError exception if comp is not 'greater_than', 'equals' or 'less_than'.

        :param rating: value for comparison operation to compare to
        :param comp: string representation of the comparison operation
        :return: pandas DataFrame object of the filtration result
        """
        if rating is None or rating < 0 or comp not in ["equals", "less_than", "greater_than"]:
            raise_error()

        if comp == "equals":
            filtered_movies = self.movie_data[self.movie_data['rating'] == rating]
        elif comp == "less_than":
            filtered_movies = self.movie_data[self.movie_data['rating'] < rating]
        else:
            filtered_movies = self.movie_data[self.movie_data['rating'] > rating]

        return filtered_movies if not filtered_movies.empty else None

    def filter_movies_by_genre(self, genre: str) -> pd.DataFrame:
        """
        Return a pandas DataFrame of self.movie_data filtered by parameter genre.

        Only rows where the given genre is in column 'genres' should be in the result.
        Operation should be case-insensitive.

        Raise the built-in ValueError exception if genre is an empty string or None.

        :param genre: string value to filter by
        :return: pandas DataFrame object of the filtration result
        """
        if not genre or genre.strip() == "":
            raise_error()

        return self.movie_data[self.movie_data['genres'].str.lower().str.contains(genre.lower())]

    def filter_movies_by_tag(self, tag: str) -> pd.DataFrame:
        """
        Return a pandas DataFrame of self.movie_data filtered by parameter tag.

        Only rows where the given tag is in column 'tag' should be left in the result.
        Operation should be case-insensitive.

        Raise the built-in ValueError exception if tag is an empty string or None.

        :param tag: string value tu filter by
        :return: pandas DataFrame object of the filtration result
        """
        if not tag or tag.strip() == "":
            raise_error()

        return self.movie_data[self.movie_data['tag'].str.lower().str.contains(tag.lower())]

    def filter_movies_by_year(self, year: int) -> pd.DataFrame:
        """
        Return a pandas DataFrame of self.movie_data filtered by year of release.

        Only rows where the year of release matches given parameter year should be left in the result.

        Raise the built-in ValueError exception if year is None or < 0.

        :param year: integer value of the year to filter by
        :return: pandas DataFrame object of the filtration result
        """
        if not year or year < 0:
            raise_error()

        return self.movie_data[self.movie_data['title'].apply(extract_year_from_title) == year]

    def get_decent_movies(self) -> pd.DataFrame:
        """
        Return all movies with a rating of at least 3.0.

        :return: pandas DataFrame object of the search result
        """
        return self.movie_data[self.movie_data['rating'] >= 3.0]

    def get_decent_comedy_movies(self) -> pd.DataFrame | None:
        """
        Return all movies with a rating of at least 3.0 and where genre is 'Comedy'.

        :return: pandas DataFrame object of the search result
        """
        return self.movie_data[(self.movie_data['genres'].str.lower().str.contains('comedy'))
                               & (self.movie_data['rating'] >= 3.0)]

    def get_decent_children_movies(self) -> pd.DataFrame | None:
        """
        Return all movies with a rating of at least 3.0 and where genre is 'Children'.

        :return: pandas DataFrame object of the search result
        """
        return self.movie_data[(self.movie_data['genres'].str.lower().str.contains('children'))
                               & (self.movie_data['rating'] >= 3.0)]

    # Start of OP methods.

    def get_median_rating(self):
        """
        Return self.median_rating.

        :return: float value of the median rating for all entries in self.movie_data
        """
        return self.median_rating

    def get_average_rating(self):
        """
        Return self.average_rating.

        :return: float value of the average rating for all entries in self.movie_data
        """
        return self.average_rating

    def calculate_rating_statistics(self):
        """
        Calculate median and average ratings for all entries in self.movie_data, rounded to three decimal places.

        Store results in self.median_rating and self.average_rating
        :return:
        """
        valid_ratings = self.movie_data['rating'].dropna()

        self.median_rating = round(valid_ratings.median(), 3)
        self.average_rating = round(valid_ratings.mean(), 3)

    def get_movies_above_average_by_genre(self, genre: str) -> pd.DataFrame:
        """Return all movies that are correct.

        Return all movies with the given genre where the rating is above
        the calculated self.average_rating value. Search is case-insensitive.
        If genre is an empty string or None, raise ValueError.

        :param genre: string value to filter by
        :return: pandas DataFrame object of the search result
        """
        if not genre:
            raise_error()

        if self.average_rating is None:
            self.calculate_rating_statistics()

        filtered_movies_by_genres = self.filter_movies_by_genre(genre)
        filtered_movies = filtered_movies_by_genres[filtered_movies_by_genres['rating'] > self.average_rating]

        return filtered_movies

    def calculate_mean_rating_for_every_movie(self) -> pd.DataFrame:
        """Return a new DataFrame.

        Return a new DataFrame where there is only one line per unique movie and the rating of every movie is the
        mean rating of all the individual ratings for that movie in self.movie_data, rounded to three decimal places.
        If the mean rating value is NaN, it should be dropped from the result.

        :return: pandas DataFrame object
        """
        # Grouping by 'movieId' and calculating mean rating.
        mean_ratings = self.movie_data.groupby('movieId').agg({'title': 'first',
                                                               'genres': 'first',
                                                               'rating': 'mean',
                                                               'tag': 'first'})

        # Dropping rows with NaN values.
        mean_ratings = mean_ratings.dropna(subset=['rating'])

        # Round to 3 decimal places.
        mean_ratings['rating'] = round(mean_ratings['rating'], 3)

        return mean_ratings

    def get_top_movies_by_genre(self, genre: str, n: int = 3) -> pd.DataFrame:
        """
        Return the top n best rated movies with the given genre. Search is case-insensitive.

        If genre is an empty string or None of if n is negative, a ValueError should be raised.

        :param genre: string value to filter by
        :param n: number of best rated movies to include in the result
        :return: pandas DataFrame object of the search result
        """
        if not genre or genre is None or n < 0:
            raise_error()

        movies = self.calculate_mean_rating_for_every_movie()
        filtered_movies = movies[movies['genres'].str.lower().str.contains(genre.lower())]

        return filtered_movies.nlargest(n, 'rating')

    def get_best_movie_by_year_genre_and_tag(self, year: int, genre: str, tag: str) -> pd.DataFrame:
        """
        Return the best rated movie with given year of release, genre and tag. Search is case-insensitive.

        If year is negative, a ValueError should be raised.
        If either tag or genre is an empty string or None, a ValueError should be raised.

        :param year: integer value to filter by
        :param genre: string value to filter by
        :param tag: string value to filter by
        :return: pandas DataFrame object of the search result
        """
        if year <= 0 or not genre or genre is None or not tag or tag is None:
            raise_error()

        movies = self.calculate_mean_rating_for_every_movie()

        # Filter movies by year, genre, and tag
        filtered_movies_by_year = movies[movies['title'].apply(extract_year_from_title) == year]
        filtered_movies_by_year_and_tag = filtered_movies_by_year[
            filtered_movies_by_year['tag'].str.lower().str.contains(tag.lower())]
        filtered_movies = filtered_movies_by_year_and_tag[
            filtered_movies_by_year_and_tag['genres'].str.lower().str.contains(genre.lower())]

        if filtered_movies.empty:
            return pd.DataFrame()

        return filtered_movies.nlargest(1, 'rating')

        # End of OP.


if __name__ == '__main__':
    # this pd.option_context menu is for better display purposes
    # in terminal when using print. Keep these settings the same
    # unless you wish to display more than 10 rows
    with pd.option_context('display.max_rows', 10,
                           'display.max_columns', 5,
                           'display.width', 200):
        my_movie_data = MovieData()

        # give correct path names here. These names are only good if you
        # installed the 3 data files in 'EX/ex15_movie_data/ml-latest-small/'
        my_movie_data.load_data("ml-latest-small/movies.csv", "ml-latest-small/ratings.csv", "ml-latest-small/tags.csv")
        print(my_movie_data.get_movies_dataframe())  # ->
        #       movieId                    title                                       genres
        # 0           1         Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy
        # 1           2           Jumanji (1995)                   Adventure|Children|Fantasy
        # 2           3  Grumpier Old Men (1995)                               Comedy|Romance
        # 3           4 Waiting to Exhale (1995)                         Comedy|Drama|Romance
        # ...
        # [9742 rows x 3 columns]  <- if your numbers match the numbers shown here it's a good
        #                             chance your function is getting the correct results.

        print(my_movie_data.get_ratings_dataframe())  # ->
        #       userId      movieId     rating      timestamp
        # 0          1            1        4.0      964982703
        # 1          1            3        4.0      964981247
        # 2          1            6        4.0      964982224
        # 3          1           47        5.0      964983815
        # ...
        # [100836 rows x 4 columns]

        print(my_movie_data.get_tags_dataframe())  # ->
        #       userId      movieId             tag     timestamp
        # 0          2        60756           funny    1445714994
        # 1          2        60756 Highly quotable    1445714996
        # 2          2        60756    will ferrell    1445714992
        # 3          2        89774    Boxing story    1445715207
        # ...
        # [3683 rows x 4 columns]

        my_movie_data.create_aggregate_movie_dataframe('--empty--')
        print(my_movie_data.get_aggregate_movie_dataframe())  # ->
        #       movieId             title                                       genres  rating               tag
        # 0           1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0   pixar pixar fun
        # 1           1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0   pixar pixar fun
        # 2           1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0   pixar pixar fun
        # 3           1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0   pixar pixar fun
        # ...
        # [100854 rows x 5 columns]
        # last rows in the aggregate dataframe will have the tag field set to '--empty--' since here
        # it is the nan_placeholder value given to the function.

        my_movie_filter = MovieFilter()
        my_movie_filter.set_movie_data(my_movie_data.get_aggregate_movie_dataframe())
        print(my_movie_filter.filter_movies_by_rating_value(2.1, 'less_than'))  # ->
        #       movieId             title                                       genres  rating               tag
        # 26          1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     0.5   pixar pixar fun
        # 43          1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     2.0   pixar pixar fun
        # 52          1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     2.0   pixar pixar fun
        # 69          1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     2.0   pixar pixar fun
        # ...
        # [13523 rows x 5 columns]

        print(my_movie_filter.filter_movies_by_year(1988))  # ->
        #        movieId                    title                                           genres  rating        tag
        # 17962      709  Oliver & Company (1988)      Adventure|Animation|Children|Comedy|Musical     5.0  --empty--
        # 17963      709  Oliver & Company (1988)      Adventure|Animation|Children|Comedy|Musical     2.0  --empty--
        # 17964      709  Oliver & Company (1988)      Adventure|Animation|Children|Comedy|Musical     3.0  --empty--
        # 17964      709  Oliver & Company (1988)      Adventure|Animation|Children|Comedy|Musical     3.5  --empty--
        # ...
        # [1551 rows x 5 columns]

        print(my_movie_filter.get_decent_movies())
        # -> first five rows all Toy Story
        # dataframe size [81763 rows x 5 columns]
        print(my_movie_filter.get_decent_comedy_movies())
        # -> first five rows all Toy Story
        # dataframe size [30274 rows x 5 columns]
        print(my_movie_filter.get_decent_children_movies())
        # -> first 5 rows all Toy Story
        # dataframe size [7326 rows x 5 columns]

        print(my_movie_filter.calculate_mean_rating_for_every_movie())

        print()

        print(my_movie_filter.get_top_movies_by_genre('Musical', 5))

        print()

        print(my_movie_filter.get_best_movie_by_year_genre_and_tag(1999, "comedy", "pixar"))
