def main():
    try:
        transpose_matrix()
    except Exception as e:
        print(f"Message: {e}")


def transpose_matrix():
    try:
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        rows = len(matrix)
        cols = len(matrix[0])
        t_matrix = [[0]*cols for _ in range(rows) ]
        for i in range(rows):
            for j in range(cols):
                t_matrix[i][j] = matrix[j][i]
    
        print(t_matrix)
    except Exception as e:
        raise e



if __name__ == "__main__":
    main()