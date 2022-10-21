from src.jobs import read


def get_unique_job_types(path):
    datas = read(path)
    conj = set()
    for data in datas:
        if data['job_type'] != '':
            conj.add(data['job_type'])
    return conj


def filter_by_job_type(jobs, job_type):
    _list = []
    for job in jobs:
        if job['job_type'] == job_type:
            _list.append(job)
    return _list


def get_unique_industries(path):
    datas = read(path)
    conj = set()
    for data in datas:
        if data['industry'] != '':
            conj.add(data['industry'])
    return conj


def filter_by_industry(jobs, industry):
    _list = []
    for job in jobs:
        if job['industry'] == industry:
            _list.append(job)
    return _list


def get_max_salary(path):
    datas = read(path)
    values = set()
    for job in datas:
        if job['max_salary'] != '' and job['max_salary'].isdigit():
            values.add(int(job['max_salary']))
    return max(values)


def get_min_salary(path):
    datas = read(path)
    values = set()
    for job in datas:
        if job['min_salary'] != '' and job['min_salary'].isdigit():
            values.add(int(job['min_salary']))
    return min(values)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
