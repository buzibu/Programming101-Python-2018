def group(arr):
    result = []
    current_group = [arr[0]]

    for item in arr[1:]:
        if current_group[-1] == item:
            current_group.append(item)
        else:
            result.append(current_group)
            current_group = [item]

    result.append(current_group)
    return result


def max_consecutive(items):
    return max([len(g) for g in group(items)])


def gas_stations(distance, tank_size, stations):
    result = []
    fuel = tank_size
    prev_station = 0
    stations.append(distance)

    for station in stations:
        dist_to_next_station = station - prev_station
        if fuel > dist_to_next_station:
            prev_station = station
            fuel = fuel - dist_to_next_station
        else:
            result.append(prev_station)
            prev_station = station
            fuel = tank_size - dist_to_next_station

    return result
