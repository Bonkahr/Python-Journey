required_list = ['python', 'linux', 'github']

candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'c++', 'github'},
    'ekani': {'html', 'css', 'javascript', 'linux', 'python'},
    'daniel': {'pascal', 'java', 'ruby', 'python', 'linux', 'github'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl',
              'github'},
}

interviewees = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_list):  # tests for superset
    if skills > set(required_list):     # tests for proper set
        interviewees.add(candidate)

print(interviewees)
