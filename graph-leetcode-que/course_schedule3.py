import numpy as np
import heapq as hq

def main():
    try:
        courses_count = utility_function()
        print(f"Courses count: {courses_count}")
    except Exception as e:
        print(f"Message: {e}")

def utility_function():
    try:
        courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
        courses.sort(key = lambda row : row[1])

        total_time = 0
        prev_max_duration = 0
        courseList = []
        for course in courses:
            duration, deadline = course
            hq.heappush(courseList, -duration)
            total_time += duration
            if not total_time <= deadline:
                prev_max_duration = -hq.heappop(courseList)
                total_time -= prev_max_duration
            
        return len(courseList)

    except Exception as e:
        raise e

if __name__ == "__main__":
    main()