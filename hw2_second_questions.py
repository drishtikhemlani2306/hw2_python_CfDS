
############################################
#
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#



#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

cvs = [
    {'user': 'john', 'jobs': ['analyst', 'engineer']},
    {'user': 'jane', 'jobs': ['finance', 'engineer']}
]

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

has_experience_as(cvs, 'analyst')

#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_counts(cvs):
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

print(job_counts(cvs))

#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.

def most_popular_job(cvs):
    counts = job_counts(cvs)
    best = (None, 0)
    for each_job in counts.items():
        if each_job[1] >= best[1]:
            best = each_job
    return best

print(most_popular_job(cvs))
