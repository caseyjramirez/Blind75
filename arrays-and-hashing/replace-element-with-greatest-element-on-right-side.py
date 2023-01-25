def replaceElementWithGreatestElement(arr):
    maxValue = -1

    for i in range(len(arr) - 1, -1, -1):
        placeHolder = arr[i];
        arr[i] = maxValue;
        maxValue = max(maxValue, placeHolder);

    return arr;





if __name__ == '__main__':
    testCase1 = [17,18,5,4,6,1];
    sollution1 = [18,6,6,6,1,-1];
    
    test1 = replaceElementWithGreatestElement(testCase1);

    print(test1)

    if test1 == sollution1:
        print('test 1 pass!');
    else:
        print('fail')

    