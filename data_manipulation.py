import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def max_employment(countries, employment):
   
    max_index = np.argmax(employment)
    max_country = countries[max_index]
    max_value = employment[max_index]

    return (max_country, max_value)

def min_employment(countries, employment):
   
    min_index = np.argmin(employment)
    min_country = countries[min_index]
    min_value = employment[min_index]

    return (min_country, min_value)

def overall_completion_rate(female_completion, male_completion):
    return (female_completion + male_completion)/2.0

def standardize_data(values):
    mean = values.mean()
    std_dev = np.std(values)
    
    return (values - mean) /std_dev

def mean_time_for_paid_students(time_spent, days_to_cancel):
    students_paying_flags = days_to_cancel >=  7
    time_spent_for_paid_students = time_spent[students_paying_flags]
    
    return np.mean(time_spent_for_paid_students)

def mean_time_for_paid_students(time_spent, days_to_cancel):
    paying_status_flags = days_to_cancel >= 7
    time_spent_for_paid_students = time_spent[paying_status_flags]
    
    return time_spent_for_paid_students.mean()
   
def variable_correlation(serie1, serie2):
    '''
    Fill in this function to calculate the number of data points for which
    the directions of variable1 and variable2 relative to the mean are the
    same, and the number of data points for which they are different.
    Direction here means whether each value is above or below its mean.
    
    You can classify cases where the value is equal to the mean for one or
    both variables however you like.
    
    Each argument will be a Pandas series.
    
    For example, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([4, 5, 6, 7]), then the output would be (4, 0).
    This is because 1 and 4 are both below their means, 2 and 5 are both
    below, 3 and 6 are both above, and 4 and 7 are both above.
    
    On the other hand, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([7, 6, 5, 4]), then the output would be (0, 4).
    This is because 1 is below its mean but 7 is above its mean, and
    so on.
    '''
    mean1 = serie1.mean()
    mean2 = serie2.mean()
    
    direction_flags_serie1 = serie1 > mean1
    direction_flags_serie2 = serie2 > mean2
    
    num_same_direction = (direction_flags_serie1 == direction_flags_serie2).sum()
    num_different_direction = (direction_flags_serie1 != direction_flags_serie2).sum()
    
    return (num_same_direction, num_different_direction)


def reverse_string(string):
    firstName , lastName =string.split(" ")
    print(f"{lastName} {firstName}")
    return f"{lastName} {firstName}"

def reverse_names(names):
    '''
    Fill in this function to return a new series where each name
    in the input series has been transformed from the format
    "Firstname Lastname" to "Lastname, FirstName".
    
    Try to use the Pandas apply() function rather than a loop.
    '''    
    reversed_names=names.apply(reverse_string)
    return reversed_names




def main(): 
    
    ###########################  DATA    ######################################
    
    # First 20 countries with employment data
    countries = np.array([
        'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
        'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
        'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
        'Belize', 'Benin', 'Bhutan', 'Bolivia',
        'Bosnia and Herzegovina'
    ])
    
    # Employment data in 2007 for those 20 countries
    employment = np.array([
        55.70000076,  51.40000153,  50.5       ,  75.69999695,
        58.40000153,  40.09999847,  61.5       ,  57.09999847,
        60.90000153,  66.59999847,  60.40000153,  68.09999847,
        66.90000153,  53.40000153,  48.59999847,  56.79999924,
        71.59999847,  58.40000153,  70.40000153,  41.20000076
    ])
        
    # Female school completion rate in 2007 for those 20 countries
    female_completion = np.array([
        97.35583,  104.62379,  103.02998,   95.14321,  103.69019,
        98.49185,  100.88828,   95.43974,   92.11484,   91.54804,
        95.98029,   98.22902,   96.12179,  119.28105,   97.84627,
        29.07386,   38.41644,   90.70509,   51.7478 ,   95.45072
    ])
    
    # Male school completion rate in 2007 for those 20 countries
    male_completion = np.array([
         95.47622,  100.66476,   99.7926 ,   91.48936,  103.22096,
         97.80458,  103.81398,   88.11736,   93.55611,   87.76347,
        102.45714,   98.73953,   92.22388,  115.3892 ,   98.70502,
         37.00692,   45.39401,   91.22084,   62.42028,   90.66958
    ])
    
    
    # Time spent in the classroom in the first week for 20 students
    time_spent = np.array([
           12.89697233,    0.        ,   64.55043217,    0.        ,
           24.2315615 ,   39.991625  ,    0.        ,    0.        ,
          147.20683783,    0.        ,    0.        ,    0.        ,
           45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
            0.        ,   54.9204785 ,   26.78142417,    0.
    ])
    
    # Days to cancel for 20 students
    days_to_cancel = np.array([
          4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
         38,  98,   2, 249,   2, 127,  35
    ])
    
    countries_pd = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

    

    
    ###########################################################################
       
    # Accessing elements
    if False:
        print(countries[0])
        print(countries[3])
    
    # Slicing
    if False:
        print(countries[0:3])
        print(countries[:3])
        print(countries[17:])
        print(countries[:])
        print("\n")
        print (countries)
    
    # Element types
    if False:
        print(countries.dtype)
        print("\n")
        print(employment.dtype)
        print(np.array([0, 1, 2, 3]).dtype)
        print(np.array([1.0, 1.5, 2.0, 2.5]).dtype)
        print(np.array([True, False, True]).dtype)
        print(np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype)
    
    # Looping
    if False:
        for country in countries:
            print('Examining country {}'.format(country))
    
        for i in range(len(countries)):
            country = countries[i]
            country_employment = employment[i]
            print('Country {} has employment {}'.format(country, country_employment))
        
       
        for country , emp in zip(countries,employment):
            print(f'country {country} has employment {emp}')
    
    # Numpy functions
    if False:
        print(employment.mean())
        print(employment.std())
        print(employment.max())
        print(employment.sum())

########################  Vectorized operations   #############################
   
    # Arithmetic operations between 2 NumPy arrays
    if False:
        a = np.array([1, 2, 3, 4])
        b = np.array([1, 2, 1, 2])
        
        print(a + b)
        print(a - b)
        print(a * b)
        print(a / b)
        print(a ** b) #pow
        
    # Arithmetic operations between a NumPy array and a single number
    if False:
        a = np.array([1, 2, 3, 4])
        b = 2
        
        print(a + b)
        print(a - b)
        print(a * b)
        print(a / b)
        print(a ** b)
        
    # Logical operations with NumPy arrays
    if False:
        a = np.array([True, True, False, False])
        b = np.array([True, False, True, False])
        
        print(a & b)
        print(a | b)
        print(~a)   # non a 
        
        print(a & True)   #=a
        print(a & False)  # = false
        
        print(a | True)
        print(a | False) 
        
    # Comparison operations between 2 NumPy Arrays
    if False:
        a = np.array([1, 2, 3, 4, 5])
        b = np.array([5, 4, 3, 2, 1])
        
        print(a > b)
        print(a >= b)
        print(a < b)
        print(a <= b)
        print(a == b)
        print(a != b)
        
    # Comparison operations between a NumPy array and a single number
    if False:
        a = np.array([1, 2, 3, 4])
        b = 2
        
        print(a > b)
        print(a >= b)
        print(a < b)
        print(a <= b)
        print(a == b)
        print(a != b)
        
#####################        flags_indexing         ###########################
    
    # Using index arrays
    if False:
        a = np.array([1, 2, 3, 4])
        b = np.array([True, True, False, False])
        
        print(a[b])
        print(a[np.array([True, False, True, False])])
        
    # Creating the index array using vectorized operations
    if False:
        a = np.array([1, 2, 3, 2, 1])
        b = (a >= 2)
        
        print(a[b])
        print(a[a >= 2])
        
    # Creating the index array using vectorized operations on another array
    if False:
        a = np.array([1, 2, 3, 4, 5])
        b = np.array([1, 2, 3, 2, 1])
        
        print(b == 2)
        print(a[b == 2])

################################  pandas    ###################################
    life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                             70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                             67.3,  70.6]

    gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
                  13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
                  27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                  483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
                  3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]
    
    # Life expectancy and gdp data in 2007 for 20 countries
    life_expectancy = pd.Series(life_expectancy_values)
    gdp = pd.Series(gdp_values)
    
        
    # Accessing elements and slicing
    if False :
        print("\n")
        print(life_expectancy)
        print(life_expectancy[0])
        print(gdp[3:6])
        
    # Looping
    if False :
        for country_life_expectancy in life_expectancy:
            print('Examining life expectancy {}'.format(country_life_expectancy))
            
    # Pandas functions
    if False :
        print(life_expectancy.mean())
        print(life_expectancy.std())
        print(gdp.max())
        print(gdp.sum())
    
    # Vectorized operations and index arrays
    if False :
        a = pd.Series([1, 2, 3, 4])
        b = pd.Series([1, 2, 1, 2])
        
        print(a.dtype)
        
        print(a + b)
        print(a * 2)
        print(a >= 3)
        print(a[a >= 3])
        
################## series index ###############################################

    
    countries = [
        'Afghanistan', 'Albania', 'Algeria', 'Angola',
        'Argentina', 'Armenia', 'Australia', 'Austria',
        'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
        'Barbados', 'Belarus', 'Belgium', 'Belize',
        'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
    ]
    
    
    employment_values = [
        55.70000076,  51.40000153,  50.5       ,  75.69999695,
        58.40000153,  40.09999847,  61.5       ,  57.09999847,
        60.90000153,  66.59999847,  60.40000153,  68.09999847,
        66.90000153,  53.40000153,  48.59999847,  56.79999924,
        71.59999847,  58.40000153,  70.40000153,  41.20000076,
    ]
    
    # Employment data in 2007 for 20 countries
    employment_serie = pd.Series(employment_values, index=countries)
    
    def max_employment(employment_serie):

        max_country = employment_serie.idxmax()    
        max_value=employment_serie[max_country]
       
        return (max_country, max_value)

############# vectorized_opertaion done upon indexes ################################
             #while in numpy series we have same static indexing 
             #we can can consider that vectorized operations are done upon the order 
    
    # Addition when indexes are the same
    if False: #same indexing values (order notimportant) 
        s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
        s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
        print (s1 + s2) 
    
    # Indexes have same elements in a different order 
    
    if False :  
        s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
        s2 = pd.Series([10, 20, 30, 40], index=['b', 'd', 'a', 'c'])
        print (s1 + s2)
    
    # Indexes overlap, but do not have exactly the same elements
    if False :  # some indexes in common -> union of indexes --> NaN value for non overlapping indexes 
        s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
        s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
        print( s1 + s2)  # NaN : not a number for elements not having there corresspoding ones upon their index 
    
    # Indexes do not overlap
    if False: # union of indexes --> NaN value for non overlapping indexes 
        s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
        s2 = pd.Series([10, 20, 30, 40], index=['e', 'f', 'g', 'h'])
        print (s1 + s2) 


######################## apply() on series to reverse names     ###################


# Example pandas apply() usage (although this could have been done
# without apply() using vectorized operations)
if False :
    s = pd.Series([1, 2, 3, 4, 5])
    def add_one(x):
        return x + 1
    print( s.apply(add_one))

names = pd.Series([
    'Andre Agassi',
    'Barry Bonds',
    'Christopher Columbus',
    'Daniel Defoe',
    'Emilio Estevez',
    'Fred Flintstone',
    'Greta Garbo',
    'Humbert Humbert',
    'Ivan Ilych',
    'James Joyce',
    'Keira Knightley',
    'Lois Lane',
    'Mike Myers',
    'Nick Nolte',
    'Ozzy Osbourne',
    'Pablo Picasso',
    'Quirinus Quirrell',
    'Rachael Ray',
    'Susan Sarandon',
    'Tina Turner',
    'Ugueth Urbina',
    'Vince Vaughn',
    'Woodrow Wilson',
    'Yoji Yamada',
    'Zinedine Zidane'
])

#print(reverse_names(names))

if __name__ == '__main__' :
    main()

######################plotig in pandas ########################################


# The following code reads all the Gapminder data into Pandas DataFrames. You'll
# learn about DataFrames next lesson.

path = './dataset/'
employment = pd.read_csv(path + 'employment_above_15.csv', index_col='Country')

female_completion = pd.read_csv(path + 'female_completion_rate.csv', index_col='Country')

male_completion = pd.read_csv(path + 'male_completion_rate.csv', index_col='Country')

life_expectancy = pd.read_csv(path + 'life_expectancy.csv', index_col='Country')

gdp = pd.read_csv(path + 'gdp_per_capita.csv', index_col='Country')




print(employment.index.values )


# Create empty Pandas Series with the correct dtype
employment_country = pd.Series(dtype='float64')
female_completion_country = pd.Series(dtype='float64')
male_completion_country = pd.Series(dtype='float64')
life_expectancy_country = pd.Series(dtype='float64')
gdp_country = pd.Series(dtype='float64')

def data_by_country(country) : 
    global employment_country ,female_completion_country , male_completion_country , life_expectancy_country , gdp_country
    employment_country = employment.loc[country]
    female_completion_country = female_completion.loc[country]
    male_completion_country = male_completion.loc[country]
    life_expectancy_country = life_expectancy.loc[country]
    gdp_country = gdp.loc[country]

#choose the country 
country='Zimbabwe'
data_by_country(country)

# Variable names
variable_names = ['employment_country', 'female_completion_country', 'male_completion_country', 'life_expectancy_country', 'gdp_country']

# Titles for the subplots
titles = [
    'Employment Rate Above 15 Over Time',
    'Female Primary Completion Rate Over Time',
    'Male Primary Completion Rate Over Time',
    'Life Expectancy Over Time',
    'GDP Per Capita Over Time'
]

y_labels = [
    'Employment Rate (%)',
    'Completion Rate (%)',
    'Completion Rate (%)',
    'Life Expectancy (Years)',
    'GDP Per Capita (constant 2000 US$)'
]

#create a figure and a set of subplots
fig , axs =plt.subplots(5,1,figsize=(8,15), sharex=True)

#set the x-axis label for the last subplot
axs[-1].set_xlabel('year')

for i , name in enumerate(variable_names)   :
    series=globals()[name]
    axs[i].plot(series.index,series.values,marker='o')
    axs[i].set_title(f'{titles[i]} in {country}')
    axs[i].set_ylabel(y_labels[i])
    axs[i].grid(True)
    

#adjust layout 
plt.tight_layout()
plt.show()












