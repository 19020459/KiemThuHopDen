def expected_output(weight, distance):
    # Tính đầu ra mong đợi
    if weight <= 0 or distance <= 0:
        return "Invalid"

    # Tính phí dựa trên khối lượng
    if weight < 1:
        weight_cost = 10000  # 10,000 VNĐ
    elif weight < 5:
        weight_cost = 20000  # 20,000 VNĐ
    elif weight <= 50:
        weight_cost = 30000  # 30,000 VNĐ
    else:
        return "Invalid"

    # Tính phí dựa trên khoảng cách
    if distance < 50:
        distance_cost = 5000  # 5,000 VNĐ
    elif distance < 100:
        distance_cost = 25000  # 25,000 VNĐ
    elif distance <= 300:
        distance_cost = 45000  # 45,000 VNĐ
    else:
        return "Invalid"

    # Tính tổng phí gửi hàng
    total_cost = weight_cost + distance_cost
    return total_cost

def calculate_expected_outputs():
    test_cases = [
        (-1, -10),   # Test case 1
        (-2, 30),    # Test case 2
        (-3, 100),   # Test case 3
        (-4, 150),   # Test case 4
        (-5, 350),   # Test case 5
        (0, -20),    # Test case 6
        (0, 25),     # Test case 7
        (0.5, 100),  # Test case 8
        (0.5, 300),  # Test case 9
        (0.5, 350),  # Test case 10
        (1, -30),    # Test case 11
        (1, 50),     # Test case 12
        (1, 80),     # Test case 13
        (2, 250),    # Test case 14
        (2, 400),    # Test case 15
        (5, -40),    # Test case 16
        (5, 45),     # Test case 17
        (5, 100),    # Test case 18
        (50, 300),   # Test case 19
        (50, 500),   # Test case 20
        (51, -50),   # Test case 21
        (51, 50),    # Test case 22
        (60, 90),    # Test case 23
        (70, 300),   # Test case 24
        (80, 400),   # Test case 25
    ]

    print(f"{'Test Case':<10} {'KL':<10} {'KC':<10} {'Expected Output':<20}")
    for i, (weight, distance) in enumerate(test_cases, start=1):
        expected = expected_output(weight, distance)
        print(f"{i:<10} {weight:<10} {distance:<10} {expected:<20}")

if __name__ == "__main__":
    calculate_expected_outputs()
