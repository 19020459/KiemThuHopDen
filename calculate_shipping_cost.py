def calculate_shipping_cost(weight, distance):
    # Kiểm tra đầu vào hợp lệ
    if weight <= 0 or distance <= 0:
        return None, "Weight and distance must be greater than or equal to 0."

    # Tính phí dựa trên khối lượng
    if weight <= 1:
        weight_cost = 10000  # 10,000 VNĐ
    elif weight < 5:
        weight_cost = 20000  # 20,000 VNĐ
    elif weight <= 50:
        weight_cost = 30000  # 30,000 VNĐ
    else:
        return None, "Weight exceeds the allowed limit (50kg)."

    # Tính phí dựa trên khoảng cách
    if distance <= 50:
        distance_cost = 5000  # 5,000 VNĐ
    elif distance <= 100:
        distance_cost = 25000  # 25,000 VNĐ
    elif distance <= 300:
        distance_cost = 45000  # 45,000 VNĐ
    else:
        return None, "Distance exceeds the allowed limit (300km)."

    # Tính tổng phí gửi hàng
    total_cost = weight_cost + distance_cost
    return total_cost, weight_cost, distance_cost


def main():
    # Nhập vào khối lượng
    weight = float(input("Enter weight (kg): "))

    # Nhập vào khoảng cách
    distance = float(input("Enter distance (km): "))

    # Tính phí gửi hàng
    shipping_cost, weight_cost, distance_cost = calculate_shipping_cost(weight, distance)

    # Kiểm tra lỗi
    if shipping_cost is None:
        print(weight_cost)  # In ra thông báo lỗi
    else:
        # Đầu ra
        print(f"Shipping cost: {weight_cost} VNĐ (weight) + {distance_cost} VNĐ (distance) = {shipping_cost} VNĐ")


if __name__ == "__main__":
    main()