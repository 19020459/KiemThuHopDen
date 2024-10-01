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
        (1, -1, -10, "Invalid"),
        (2, -2, 30, "Invalid"),
        (3, -3, 100, "Invalid"),
        (4, -4, 150, "Invalid"),
        (5, -5, 350, "Invalid"),
        (6, 0, -20, "Invalid"),
        (7, 0, 25, "Invalid"),
        (8, 0.5, 100, 55000),
        (9, 0.5, 300, 55000),
        (10, 0.5, 350, "Invalid"),
        (11, 1, -30, "Invalid"),
        (12, 1, 50, 45000),
        (13, 1, 80, 45000),
        (14, 2, 250, 65000),
        (15, 2, 400, "Invalid"),
        (16, 5, -40, "Invalid"),
        (17, 5, 45, 35000),
        (18, 5, 100, 75000),
        (19, 50, 300, 75000),
        (20, 50, 500, "Invalid"),
        (21, 51, -50, "Invalid"),
        (22, 51, 50, "Invalid"),
        (23, 60, 90, "Invalid"),
        (24, 70, 300, "Invalid"),
        (25, 80, 400, "Invalid"),
    ]

    print(f"{'Test Case':<10} {'KL':<10} {'KC':<10} {'Expected Output':<20} {'Actual Output':<20} {'Result':<10}")

    for case in test_cases:
        case_id, weight, distance, expected_output = case
        actual_output, *_ = calculate_shipping_cost(weight, distance)
        actual_output = "Invalid" if actual_output is None else actual_output

        # So sánh kết quả
        result = "Passed" if actual_output == expected_output else "Failed"

        # In ra kết quả
        print(f"{case_id:<10} {weight:<10} {distance:<10} {expected_output:<20} {actual_output:<20} {result:<10}")


if __name__ == "__main__":
    run_test_cases()
