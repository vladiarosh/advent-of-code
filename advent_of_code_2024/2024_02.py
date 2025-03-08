from utils import get_input_path


def main():
    file_path = get_input_path(__file__, '2024_02_input.txt')
    file = open(file_path)
    lines = file.readlines()
    file.close()
    lines = [line.rstrip().split() for line in lines]
    lines = [[int(num) for num in line] for line in lines]
    safe_reports, unsafe_reports = collect_safe_and_unsafe_reports(lines)

    # Part one result
    print('Number of safe reports is', len(safe_reports))

    saved_reports = []
    for report in unsafe_reports:
        report_save_attempt = dampen_problem(report)
        if report_save_attempt is not None:
            saved_reports.append(report_save_attempt)

    new_result = len(safe_reports) + len(saved_reports)

    # Part two result
    print('After dampen module the result is', new_result)


def collect_safe_and_unsafe_reports(unfiltered_report):
    good_reports = []
    bad_reports = []
    for line in unfiltered_report:
        uni_direction_state, no_out_of_bound_difference = check_report_safety(line)
        if uni_direction_state and no_out_of_bound_difference is True:
            good_reports.append(line)
        else:
            bad_reports.append(line)
    return good_reports, bad_reports


def check_report_safety(report):
    single_direction = True
    nothing_out_of_bounds = True
    ascending_counter = 0
    descending_counter = 0
    out_of_bounds_counter = 0

    for index, number in enumerate(report):
        if index != 0:
            difference = report[index] - report[index - 1]
            if report[index] > report[index - 1]:
                ascending_counter += 1
                if difference < 1 or difference > 3:
                    out_of_bounds_counter += 1
            if report[index] < report[index - 1]:
                descending_counter += 1
                if abs(difference) < 1 or abs(difference) > 3:
                    out_of_bounds_counter += 1
            if difference == 0:
                out_of_bounds_counter += 1

        if ascending_counter > 0 and descending_counter > 0:
            single_direction = False
        if out_of_bounds_counter > 0:
            nothing_out_of_bounds = False
    return single_direction, nothing_out_of_bounds


def dampen_problem(unsafe_report):
    for index in range(len(unsafe_report)):
        temp_report = unsafe_report[:index] + unsafe_report[index + 1:]
        single_direction, nothing_out_of_bounds = check_report_safety(temp_report)
        if single_direction and nothing_out_of_bounds:
            return temp_report
    return None


if __name__ == "__main__":
    main()





