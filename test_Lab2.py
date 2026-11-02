import Lab2
def test_find_min_max():
    inputlist = [21,23,25,27,29,31,33]
    expected = [21,33]
    result = Lab2.find_min_max(inputlist)
    assert(result == expected)

def test_calc_average():
    inputlist = [21,23,25,27,29,31,33]
    expected = 27
    result = Lab2.calc_average(inputlist)
    assert(result == expected)

def test_find_medium():
    inputlist = [[21,23,25,27,29,31,33],[21,23,25,27,29,31,34,33]]
    expected = [27,28]
    for index,element in enumerate(inputlist):
        result = Lab2.calc_median_temperature(inputlist[index])
        assert(result == expected[index])