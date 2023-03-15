def get_max():
    grades = [9.6, 9.2, 9.7]
    max_grades = max(grades)
    min_grades = min(grades)
    output = f"Max: {max_grades}, Min: {min_grades}"
    return output


print(get_max())