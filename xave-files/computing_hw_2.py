import pandas as pd
def tripled(x):
    """QUESTION 1 Take an input and return it multiplied by 3"""
    return(x *3)

def subtract(a, b):
    """QUESTION 2 Takes 2 inputs and returns the difference of first minus the second"""
    return(a-b)

def dictionary_maker(list_as_tuple):
    """QUESTION 3 Turn a list of two tuples and turns into dictionary where first value is key"""
    list_as_d = {}
    for key, value in list_as_tuple:
        list_as_d[key] = value
    return list_as_d

def has_experience_as (cvs, job_test):
    """QUESTION 4 return a list of strings representing the usernames of every user 
    that has worked as job_title"""
    experienced_group = []
    for cv in cvs:
        for jobs in cv["jobs"]:
            if jobs == job_test:
                experienced_group.append(cv["user"])
                break
    return experienced_group

def job_counts(cvs):
    """QUESTION 5 returns a dictionary where the keys are the job titles and the values
       are the number of users that have done that job."""
    counts_dict = {}
    for cv in cvs:
        seen = []
        for jobs in cv['jobs']:
            if jobs in seen:
                continue
            else:
                seen.append(jobs)
        for each_job in seen:
                if each_job in counts_dict:
                    counts_dict[each_job] += 1
                else:    
                    counts_dict[each_job] = 1
    return counts_dict

def most_popular_job(cvs):
    """QUESTION 6 Return tuple w/ most popular job and count of it
    UNSURE WHAT TO DO IN CASE OF TIE"""
    counts = job_counts(cvs)
    best = (None, 0)
    for each_job in counts.items():
        if each_job[1] >= best[1]:
            best = each_job
    return best

def total_registered_cases(records, target):
    for country in records:
        if target == country:
            return sum(records[country])

def total_registered_cases_per_country(records):
     new_d = {}
     for country in records:
        new_d[country] = total_registered_cases(records, country)
     return new_d

def country_with_most_cases(records):
    best_country = None
    best_total = 0
    record_summed_per_country = total_registered_cases_per_country(records)
    for country in records:
        if record_summed_per_country[country] > best_total:
            best_country = country
            best_total = record_summed_per_country[country]
    return best_country

"""QUESTION 10"""
df = pd.read_csv("covid.csv")

threshold = [500, 1000, 5000]

for number in threshold:

    print(f'The countries which have more than {number} active cases.')

    filtered_df = df[df['Active'] > number].copy()

    print(filtered_df['Country'])

    filtered_df['Ratio'] = filtered_df['Deaths'] / filtered_df['Confirmed']

    print(f"Average Deaths/Confirmed cases: {filtered_df['Ratio'].mean()}")


