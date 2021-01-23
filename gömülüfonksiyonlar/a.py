n = int(input())
liste = []
for i in range(n):
    liste1 = input().split()
    liste += [liste1]
point_list = [0] * n
for i in range(n):
    point = 0
    for j in range(len(liste[i])):
        if liste[i][j] != '0':
            point += 1
    point_list[i] += point
    for j in range(1, n):
        try:
            index = liste[i].index(str(j))
            point_list[index] += n-j
        except ValueError:
            break
        except IndexError:
            break
point_list_sorted = sorted(point_list, reverse=True)
for x in range(3):
    try:
        index = point_list.index(point_list_sorted[x])
        point_list[index] = '0'
        print(index + 1)
    except IndexError:
        break