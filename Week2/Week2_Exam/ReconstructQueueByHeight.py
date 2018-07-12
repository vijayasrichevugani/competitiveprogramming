def ReconstructQueueByHeight(people):
    people.sort(key=lambda (h, k): (-h, k))

    lists = [[]]
    for p in people:
        index = p[1]

        for i, lis in enumerate(lists):
            if index <= len(lis):
                break
            index -= len(lis)
        lis.insert(index, p)

        if len(lis) * len(lis) > len(people):
            lists.insert(i+1, lis[len(lis)/2:])
            del lis[len(lis)/2:]

    return [p for lis in lists for p in lis]
 
#Testcase:1   
actual = ReconstructQueueByHeight([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
print actual

#Testcase:2
actual = ReconstructQueueByHeight([[12,0], [6,3], [3,4], [9,2], [11,1], [1,5]])
print actual

#Testcase:3
actual = ReconstructQueueByHeight([[2,4], [5,1], [3,3], [1,5], [4,2], [6,0]])
print actual
