import Lab2_devOps_python.bmi as BMI

def test_calculate_bmi():
    input_data = [
    [70, 1.75],   # BMI 22.86
    [50, 1.60],   # BMI 19.53
    [90, 1.80],   # BMI 27.78
    [45, 1.70],   # BMI 15.57
    [100, 1.65],  # BMI 36.73
]
    expected_data = [0, 0, 1, -1, 1]

    result_data = [BMI.calculate_bmi(el[1],el[0]) for el in input_data]

    assert(result_data == expected_data)
