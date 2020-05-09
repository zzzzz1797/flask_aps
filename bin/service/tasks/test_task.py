def sum_task(num1: int, num2: int):
    return num1 + num2


def multi_task(num1: int, num2: int):
    return num1 * num2


sum_task.description = "求和任务，两个参数，比如(1,3)"
multi_task.description = "求积任务，两个参数，比如(4,5)"


if __name__ == '__main__':
    from apscheduler.util import ref_to_obj
    res = ref_to_obj("tasks:test_task.multi_task")
    print(res)