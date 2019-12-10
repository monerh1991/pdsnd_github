import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january','february','march','april','may','june']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ("enter city name :\n").strip().lower()
    while not city in CITY_DATA:
        city = input ("enter city name again please :\n").strip().lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input ("enter month name :\n").strip().lower()
    while not month in MONTHS:
        month = input ("enter month name again please :\n").strip().lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ("enter day name :\n").strip().lower()
    while not day in DAYS:
        day = input ("enter day name again please :\n").strip().lower()



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()

    if month != 'All':
        df = df[df['month'] == month.title()]

    if day != 'All':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common start month:\n{} \n".format(popular_month))


    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print("Most common start day of week:\n{} \n".format(popular_day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour:\n{} \n".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most common start station:\n{} \n".format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most common end station:\n{} \n".format(popular_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['road']= df['Start Station'] + df['End Station']
    most_frequent_combination = df['road'].mode()[0]
    print("Most frequent combination of start station and end station trip:\n{} \n".format(most_frequent_combination))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time:\n{} \n".format(total_travel_time))



    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time:\n{} \n".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print("counts of user types:\n{} \n".format(counts_of_user_types))


    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        print('this city have no gender \n')
    else:
        counts_of_gender = df['Gender'].value_counts()
        print("counts of gender:\n{} \n".format(counts_of_gender))


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('this city have no birth year data \n')
    else:
        popular_birth_year = df['Birth Year'].mode()[0]
        print("most common year of birth:\n{} \n".format(popular_birth_year))


    erliest_birth_year = df['Birth Year'].min()
    print("erliest year of birth:\n{} \n".format(erliest_birth_year))

    most_recent_birth_year = df['Birth Year'].max()
    print("most recent year of birth:\n{} \n".format(most_recent_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        want_raw_data = input ("Would you like to see the raw data? ").strip().lower()
        start = 0
        end = 5
        while(want_raw_data == "yes"):
            print(df.iloc[start:end])
            start += 5
            end += 5
            want_raw_data = input ("Would you like to see the raw data? ").strip().lower()

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
