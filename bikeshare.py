"""
Bikeshare.py

Use Python to understand U.S. bikeshare data. Calculate statistics and build an
interactive environment where a user chooses the data and filter for a
dataset to analyze.

"""


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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use       a while loop to handle invalid inputs
    while True:
        try:
            city = str(input('\nWould you like to see data from Chicago, New York City, or Washington: ')).lower()
            assert city in ['chicago', 'new york city', 'washington']
            break
        except KeyboardInterrupt:
            print('\nNo input taken')
            break
        except AssertionError:
            print('\nInvalid City: Please enter either Chicago, New York City, or Washington')
        except:
            print('\nInvalid input: Please enter either chicago, new york city, or washington')

    print('\nThe city you choose is: {}'.format(city))

    # TO DO: get user input for filter_type (month, day, none)
    while True:
        try:
            message = '\nWould you like to filter the data by month, day, or not at all? Type "none" for no time filter: '
            filter_type = str(input(message)).lower()
            assert filter_type in ['month', 'day', 'none']
            break
        except KeyboardInterrupt:
            print('\nNo input taken')
            break
        except AssertionError:
            print('\nInvalid Input: Valid input are month, day, or none')
        except:
            print('\nInvalid Input: Valid input are month, day, or none')
    print('\nYou would like to see the data filtered by {}'.format(filter_type))

    month = 'all'
    day = 'all'
    if filter_type == 'month':
        # TO DO: get user input for month (all, january, february, ... , june)
        while True:
            try:
                message = '\nWhich month - January, February, March, April, May or June or all? '
                month = str(input(message)).lower()
                assert month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']
                break
            except KeyboardInterrupt:
                print('\nNo input taken')
                break
            except AssertionError:
                print('\nInvalid Input: Valid input are january, february, march, april, may, june, or all ')
            except :
                print('\nInvalid Input: Valid input are january, february, march, april, may, june, or all ')
        print('\nYou would like to see the data filtered by {}'.format(month))


    elif filter_type == 'day':
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            try:
                message = '\nWhich day - monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all? '
                day = str(input(message)).lower()
                assert day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all ']
                break
            except KeyboardInterrupt:
                print('\nNo input taken')
                break
            except AssertionError:
                print('\nInvalid Input: Valid input are monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all')
            except:
                print('\nInvalid Input: Valid input are monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all')
        print('\nYou would like to see the data filtered by {}'.format(day))



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
    file_dict = {'chicago': 'chicago.csv' , 'new york city': 'new_york_city.csv' , 'washington': 'washington.csv' }
    # Load file into a dataframe
    df = pd.read_csv(file_dict[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from start time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = [ 'janurary', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to creat the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # conver the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('The most common month for travel is {}'.format(popular_month))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of week for travel is {}'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour of day for travel is {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The most common start station is {}'.format(popular_start))

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The most common end station is {}'.format(popular_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Station Combination'].mode()[0]
    print('The most common trip is {}'.format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # TO DO: display total travel time
    df['travel_time'] = df['End Time'] - df['Start Time']
    total_time = df['travel_time'].sum()
    num_trips = df['travel_time'].count()
    print('The total travel time is {} for {} trips.'.format(total_time, num_trips))

    # TO DO: display mean travel time
    mean_travel_time = df['travel_time'].mean()
    print('The mean travel time is {}'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    vc = df['User Type'].value_counts()
    for index,value in vc.iteritems():
        print('The count of user type {} is {}.'.format(index,value))

    # TO DO: Display counts of gender
    try:
        vc = df['Gender'].value_counts()
        print(type(vc))
        for index,value in vc.iteritems():
            print('The count of gender {} is {}.'.format(index,value))
    except KeyError:
        print('Gender data is not available for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        birthyear = df['Birth Year']
        earliest = int(birthyear.min())
        recent = int(birthyear.max())
        common = int(birthyear.mode()[0])
        print('The earliest birthyear is {}.'.format(earliest))
        print('The most recent birthyear is {}.'.format(recent))
        print('The most common birthyear is {}.'.format(common))
    except KeyError:
        print('Birth Year is not available for this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_raw(df):
    indi =  'yes'
    ite = 0
    while True:
        try:
            # ask if the user wants to see individual trip data
            indi = input('\nWould you like to see (more) individual trip data? Enter yes or no.\n').lower()
            assert indi in ['yes', 'no']
            if indi == 'yes':
                if ite*5 < df.shape[0]:
                    print(df.iloc[ite*5:ite*5+5])
                    ite += 1
                else:
                    print('You have reach the end of raw data.')
                    break
            elif  indi == 'no':
                break
        except KeyboardInterrupt:
            print('\nNo input taken')
            break
        except:
            print('\nInvalid input: Please enter either yes or no')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # ask if the user wants to see individual trip data
        view_raw(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
