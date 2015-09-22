def generate_splices(knot_sqs,degree):
    lst = []
    for i in range(len(knot_sqs) - degree +1):
        lst.append(knot_sqs[i:degree+i])
    return lst
def Greville_abscissae(lst):
    xs,ys = zip(*lst)
    return  (sum(xs)/len(xs),sum(ys)/len(ys))



knot_sqs=[(x,x+1) for x in range(10)]
degree = 4
splices = generate_splices(knot_sqs,degree)
control_points = map(Greville_abscissae,splices)


print(control_points)

#print(zip(lst[0],lst[1],lst[2]))

