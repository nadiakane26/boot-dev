def count_marketers(job_titles):
    return sum(1 for title in job_titles if "marketer" in title.lower())

