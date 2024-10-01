def calculate_shipping_cost(weight, distance):
    # Kiểm tra đầu vào hợp lệ
    if weight <= 0 or distance <= 0:
        return None, "Invalid"

    # Tính phí dựa trên khối lượng
    if weight <= 1:
        weight_cost = 10000  # 10,000 VNĐ
    elif weight < 5:
        weight_cost = 20000  # 20,000 VNĐ
    elif weight <= 50:
        weight_cost = 30000  # 30,000 VNĐ
    else:
        return None, "Invalid"

    # Tính phí dựa trên khoảng cách
    if distance <= 50:
        distance_cost = 5000  # 5,000 VNĐ
    elif distance <= 100:
        distance_cost = 25000  # 25,000 VNĐ
    elif distance <= 300:
        distance_cost = 45000  # 45,000 VNĐ
    else:
        return None, "Invalid"

    # Tính tổng phí gửi hàng
    total_cost = weight_cost + distance_cost
    return total_cost, weight_cost, distance_cost

def run_test_cases():
    test_cases = [
        (25, -1, "Invalid"),                        # Test case 1
        (25, 0, "Invalid"),                         # Test case 2
        (25, 1, 35000),                             # Test case 3
        (25, 299, 75000),                           # Test case 4
        (25, 300, 75000),                           # Test case 5
        (25, 301, "Invalid"),                       # Test case 6
        (-1, 150, "Invalid"),                       # Test case 7
        (0, 150, "Invalid"),                        # Test case 8
        (1, 150, 65000),                            # Test case 9
        (49, 150, 75000),                           # Test case 10
        (50, 150, 75000),                           # Test case 11
        (51, 150, "Invalid"),                       # Test case 12
        (25, 150, 75000),                           # Test case 13
    ]

    print(f"{'Test Case':<10} {'Expected Output':<20} {'Actual Output':<20} {'Result':<10}")

    for i, (weight, distance, expected_output) in enumerate(test_cases, start=1):
        result = calculate_shipping_cost(weight, distance)
        
        # Xử lý khi kết quả là Invalid
        if result[0] is None:
            actual_output = "Invalid"
        else:
            actual_output = result[0]  # Lấy tổng phí gửi hàng (total_cost)
        
        # So sánh với kết quả mong đợi
        if actual_output == expected_output:
            result_status = "Passed"
        else:
            result_status = f"Failed"
        
        # In kết quả cho mỗi test case
        print(f"{i:<10} {expected_output:<20} {actual_output:<20} {result_status:<10}")

# Chạy các test case
run_test_cases()
