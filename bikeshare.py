import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    # user input city code:
    while True:
        city = input("Enter city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city, try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    # user input month code:
    while True:
        month = input("Enter month (all, january, february, ... june): ").lower()
        if month in ['all','january','february','march','april','may','june']:
            break
        else:
            print("Invalid month.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # user input day of week code:
    while True:
        day = input("Enter day (all, monday, tuesday, ... sunday): ").lower()
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            print("Invalid day.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    #Load data code:
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name().str.lower()

    #filter by month if applicable
    if month != 'all':
        months = ['january','february','march','april','may','june']
        df = df[df['month'] == months.index(month) + 1]

    #filter by day if applicable
    if day != 'all':
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month:", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("Most common day:", df['day'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("Most common hour:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("Most common start station:", df['Start Station'].mode()[0])
    print("Most common end station:", df['End Station'].mode()[0])

    df['trip'] = df['Start Station'] + " to " + df['End Station']
    print("Most common trip:", df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print("Total travel time:", df['Trip Duration'].sum())
    print("Average travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print(df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print("Earliest:", int(df['Birth Year'].min()))
        print("Latest:", int(df['Birth Year'].max()))
        print("Most common:", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Display 5 lines of raw data based on user request"""
    start_loc = 0

    while True:
        display = input("\nWould you like to see 5 lines of raw data? (yes/no): ").lower()

        if display == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5

            if start_loc >= len(df):
                print("No more data to display.")
                break
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()