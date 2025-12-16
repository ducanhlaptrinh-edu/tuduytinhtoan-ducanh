def set_matrix() : 
    try : 
        n = int(input())
        m = int(input())
    except ValueError : 
        print("Invalid")
        return
    matrix = []

    print(f"Enter {n} rows and {m} columns !")

    for i in range(n) : 
        while True : 
            row_input = list(map(str,input().split()))
            if m == len(row_input) : 
                matrix.append(row_input)
                break
            else : 
                print("Invalid")

    print("\nMatrix : ")

    for i in range(n) : 
        for j in range(m) : 
            print(f"{matrix[i][j]:>4}" , end = "")
        print()


set_matrix()


