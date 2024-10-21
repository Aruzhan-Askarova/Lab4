from datetime import datetime

date1 = datetime(2024, 10, 1, 12, 0, 0)
date2 = datetime(2024, 10, 5, 14, 30, 0)

difference_in_seconds = (date2 - date1).total_seconds()
print(difference_in_seconds)
