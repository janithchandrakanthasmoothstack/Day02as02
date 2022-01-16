from setuptools.glob import glob

productList = [['order_num','author','qty','pri'],
                   ['34587', 'Learning Python,Mark Lutz', 4, 40.95],
                   ['98762', 'Programming Python, Mark Lutz', 5, 56.80],
                   ['77226', 'Head First Python, Paul Barry', 3, 32.95],
                   ['88112', 'Einführung in Python3, Bernd Klein', 3, 24.99]]
global orderTotal
orderTotal = 0
def sumVal(input):
    if isinstance(input[3], str):
        return   (input[0],input[3],input[2],'sum')
    else:
        lineSum = (lambda x: int(input[3])*int(input[2]))(input)
        global orderTotal
        orderTotal = orderTotal + lineSum
        return   (input[0],input[3],input[2],orderTotal)

def updatePrice(input):
    if isinstance(input[3], str):
        return (input[0], input[3], input[2], 'sum')
    else:
        lineSum = (lambda x: (int(input[3])+0.1) * int(input[2]))(input)
        global orderTotal
        orderTotal = orderTotal + lineSum
        return (input[0], input[3], input[2], orderTotal)


sumData = list(map(sumVal,productList))

if orderTotal > (orderTotal*100):
    print(f'Total : {orderTotal:.2f}')
    for x in sumData :
     print(f'{x[0]}   {x[1]}    {x[2]}    {x[3]}')
else:
    subTotal = orderTotal;
    orderTotal = 0
sumData = list(map(updatePrice,productList))
for x in sumData:
    print(f'{x[0]}   {x[1]}    {x[2]}    {x[3]}')
print(f'Cost  : $ {(subTotal):.2f}/=')
print(f'surge : $ {(orderTotal-subTotal):.2f}/=')
print(f'Total : ${orderTotal:.2f}/=')