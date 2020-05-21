if __name__ == '__main__':
    N = int(input())
    student2marks = {}
    for i in range(N):
        student, *marks = input().split()
        student2marks[student] = list(map(float, marks))
    
    marks = student2marks[input()]
    print("{0:.2f}".format(sum(marks) / len(marks)))
