# Custom filter plugin: range_interfaces.py

def range_interfaces(interfaces):
    ranges = []
    start = None
    end = None

    def format_interface(interface):
        parts = interface.split("/")
        if len(parts) == 3:
            return "Gi{}/{}/{}".format(parts[0], parts[1], parts[2])
        else:
            return interface

    sorted_interfaces = sorted(interfaces, key=format_interface)

    for interface in sorted_interfaces:
        if start is None:
            start = interface
            end = interface
        elif format_interface(interface) == format_interface(end + 1):
            end = interface
        else:
            if start == end:
                ranges.append(format_interface(start))
            else:
                ranges.append("{}-{}".format(format_interface(start), format_interface(end)))
            start = interface
            end = interface

    if start is not None:
        if start == end:
            ranges.append(format_interface(start))
        else:
            ranges.append("{}-{}".format(format_interface(start), format_interface(end)))

    return ', '.join(ranges)


interfaces = [
    "Gi1/0/1",
    "Gi1/0/2",
    "Gi1/0/3",
    "Gi1/0/4",
    "Gi1/0/5",
    "Gi1/0/6",
    "Gi1/0/7",
    "Gi1/0/8",
    "Gi1/0/9",
    "Gi1/0/10",
    "Gi1/0/12",
    "Gi2/0/1",
    "Gi2/0/2",
    "Gi2/0/3",
    "Gi2/0/4",
    "Gi2/0/5",
    "Gi2/0/6",
    "Gi2/0/7",
    "Gi2/0/8",
    "Gi2/0/9",
    "Gi2/0/10"
]

resultat = range_interfaces (interfaces)
print(resultat)
