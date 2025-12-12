def generate_report(data):
    """
    Accepts a dictionary of employee computed values and returns
    formatted report lines as a single string.
    """
    report = []
    report.append("Employee Tax Report")
    report.append("-------------------------------------")
    report.append("Field                     Details")
    report.append("-------------------------------------")

    for key, value in data.items():
        report.append(f"{key:<25} {value}")

    report.append("-------------------------------------")
    return "\n".join(report)
