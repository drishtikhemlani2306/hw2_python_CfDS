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

CV=[{'user': 'john', 'jobs': ['analyst', 'engineer', 'software', 'engineer']},
    {'user': 'jane', 'jobs': ['finance', 'software', 'engineer']}]

def has_experience_as(CV, job_title):
    for cv in CV:
        if job_title in cv['jobs']:
            print(cv['user'])
    return CV, job_title

has_experience_as(CV, "finance")

# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_count(CV):
    counts={}
    for cv in CV:
        for job in cv['jobs']:
            if job in counts:
                 counts[job]+=1
            else:
                counts[job]=1
    return counts

print(job_count(CV))

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

def most_popular_job(CV):
    counts=job_count(CV)

    most_popular=""
    highest_count=0

    for job, count in counts.items():
        if count > highest_count:
            most_popular=job
            highest_count=count
    return (most_popular, highest_count)

print("The most popular job in the list are: ", most_popular_job(CV))
