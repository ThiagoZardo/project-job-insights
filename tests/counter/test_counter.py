from src.counter import count_ocurrences


def test_counter():
    response_python = count_ocurrences('src/jobs.csv', 'Python')
    response_javascript = count_ocurrences('src/jobs.csv', 'Javascript')
    assert response_python == 1639
    assert response_javascript == 122
