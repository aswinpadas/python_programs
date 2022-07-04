""" 
Hacker Rank Nested List : 
Qun : Given the names and grades for each student in a class of N students, store them in 
a nested list and print the name(s) of any student(s) having the second lowest grade.
"""
if __name__ == '__main__':
    student_result = []
    for x in range(int(input())):
        name = input()
        score = float(input())
        student_result.append([name, score])
    new_list = [[j, k] for j, k in sorted(
        student_result, key=lambda student_result: student_result[1])
                if k != min(student_result,
                            key=lambda student_result: student_result[1])[1]]
    new_list = [
        j for j, k in sorted(new_list, key=lambda new_list: new_list[1])
        if k == min(new_list, key=lambda new_list: new_list[1])[1]
    ]
    for i in sorted(new_list):
        print(i)
