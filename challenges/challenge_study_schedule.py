def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    # Requisito 1

    if type(target_time or permanence_period) != int:
        return None

    total_present_students = 0

    for entrance_time, exit_time in permanence_period:
        if type(entrance_time) != int or type(exit_time) != int:
            return None

        if entrance_time <= target_time <= exit_time:
            total_present_students += 1

    return total_present_students
