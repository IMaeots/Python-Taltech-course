"""What should we watch, Honey?..."""

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
        self.ratings.drop(columns=['userId', 'timestamp'], axis=1)
        self.tags.drop(columns=['userId', 'timestamp'], axis=1).groupby("movieId").agg({'tag': lambda x: ' '.join(x)})

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

    def set_movie_data(self, movie_data: pd.DataFrame) -> None:
        """
        Set the value of self.movie_data to be given argument movie_data.

        :param movie_data: pandas DataFrame object
        :return: None
        """
        pass

    def filter_movies_by_rating_value(self, rating: float, comp: str) -> pd.DataFrame | None:
        """
        Return pandas DataFrame of self.movie_data filtered according to rating and comp string value.

        Raise the built-in ValueError exception if rating is None or < 0.
        Raise the built-in ValueError exception if comp is not 'greater_than', 'equals' or 'less_than'.

        :param rating: value for comparison operation to compare to
        :param comp: string representation of the comparison operation
        :return: pandas DataFrame object of the filtration result
        """
        pass

    def filter_movies_by_genre(self, genre: str) -> pd.DataFrame:
        """
        Return a pandas DataFrame of self.movie_data filtered by parameter genre.

        Only rows where the given genre is in column 'genres' should be in the result.
        Operation should be case-insensitive.

        Raise the built-in ValueError exception if genre is an empty string or None.

        :param genre: string value to filter by
        :return: pandas DataFrame object of the filtration result
        """
        pass

    def filter_movies_by_tag(self, tag: str) -> pd.DataFrame:
        """
        Return a pandas DataFrame of self.movie_data filtered by parameter tag.

        Only rows where the given tag is in column 'tag' should be left in the result.
        Operation should be case-insensitive.

        Raise the built-in ValueError exception if tag is an empty string or None.

        :param tag: string value tu filter by
        :return: pandas DataFrame object of the filtration result
        """
        pass

    def filter_movies_by_year(self, year: int) -> pd.DataFrame:
        """
        Return a pandas DataFrame of self.movie_data filtered by year of release.

        Only rows where the year of release matches given parameter year should be left in the result.

        Raise the built-in ValueError exception if year is None or < 0.

        :param year: integer value of the year to filter by
        :return: pandas DataFrame object of the filtration result
        """
        pass

    def get_decent_movies(self) -> pd.DataFrame:
        """
        Return all movies with a rating of at least 3.0.

        :return: pandas DataFrame object of the search result
        """
        pass

    def get_decent_comedy_movies(self) -> pd.DataFrame | None:
        """
        Return all movies with a rating of at least 3.0 and where genre is 'Comedy'.

        :return: pandas DataFrame object of the search result
        """
        pass

    def get_decent_children_movies(self) -> pd.DataFrame | None:
        """
        Return all movies with a rating of at least 3.0 and where genre is 'Children'.

        :return: pandas DataFrame object of the search result
        """
        pass


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
