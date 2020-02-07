import time


class term_color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'


ROBOT_LISTENER_API_VERSION = 3

_x_start_time = {}


def decorate(text):
    indent_level = 6
    box_length = 1

    box_upper_corner = u'\u2554'.encode('utf-8')
    box_horizontal_element = u'\u2550'.encode('utf-8')
    box_vertical_element = u'\u2551'.encode('utf-8')
    box_lower_corner = u'\u255a'.encode('utf-8')

    initial_spacing = " " * indent_level
    line_prefix = "\n" + initial_spacing + box_vertical_element + " "

    return initial_spacing + box_upper_corner + (box_horizontal_element * box_length) \
        + line_prefix \
        + line_prefix.join(text.encode('utf-8').split("\n")) \
        + "\n" + initial_spacing + box_lower_corner + (box_horizontal_element * box_length)


def start_test(data, result):
    print("+++++ Starting test '{}'".format(data.longname))
    _x_start_time[data.longname] = time.time()


def end_test(data, result):
    status = ""
    if result.passed:
        status = term_color.GREEN + 'OK' + term_color.RESET
    else:
        if 'skipped' in result.tags:
            status = term_color.BLUE + 'skipped' + term_color.RESET
        elif 'non_critical' in result.tags:
            status = term_color.YELLOW + 'failed (non critical)' + term_color.RESET
        else:
            status = term_color.RED + 'failed' + term_color.RESET

    duration = time.time() - _x_start_time[data.longname]
    del _x_start_time[data.longname]

    print("+++++ Finished test '{0}' in {1:.2f} seconds with status {2}".format(data.longname, duration, status))

    if not result.passed:
        print(decorate(result.message))
