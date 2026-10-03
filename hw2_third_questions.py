##############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)

data = {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}

# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

def total_registered_cases(data, country):
    count = 0
    if country in data:
        for i in data[country]:
            count += i
    return count

print(total_registered_cases(data, 'France'))


# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#

def total_registered_cases_per_country(data):
    new_dict = {}

    for country in data:
        new_dict[country] = total_registered_cases(data, country)
    return new_dict

print(total_registered_cases_per_country(data))

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(data):
    count = 0
    most_cases_country = ''
    for country, total in total_registered_cases_per_country(data).items():

        if total > count:
            count = total
            most_cases_country = country

    return most_cases_country


print(country_with_most_cases(data))

###############