def point_system(point_list):
    
    if len(point_list) > 3:
        for i in range(3):
            if not isinstance(point_list[i], (int, float)):
                return f"Los primeros 3 valores deben ser númericos, el valor '{point_list[i]}' no es númerico"
    
    result_list = []
    
    for i in point_list:
        if isinstance(i, int):
            result_list.append(i)
        elif i == "M":
            score = sum(result_list[-3:])
            result_list.append(score)
        elif i == "2":
            last_score = result_list[-1]
            new_score = last_score ** 2
            result_list.append(new_score)
        elif i == "-":
            result_list = result_list[:-2]
    
    total_score = sum(result_list)
    return total_score
