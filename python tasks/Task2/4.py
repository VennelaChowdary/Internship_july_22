n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
X = list(student_marks[query_name])    
per = sum(X)/len(X);
print("%.2f" %per)