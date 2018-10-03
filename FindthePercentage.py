if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        a,b,c=map(float,line)
        x=str(round(((a+b+c)/3),2))
        a=x.split(".")
        a[1]=a[1].ljust(2,'0')
        x=float(".".join(a))
        student_marks[name] =x 
    query_name = input()
    print("%.2f" %student_marks[query_name])