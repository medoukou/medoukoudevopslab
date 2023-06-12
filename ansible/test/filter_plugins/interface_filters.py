class FilterModule(object):
    def filters(self):
        return {
            'convert_to_interface_ranges': self.convert_to_interface_ranges
        }

    def convert_to_interface_ranges(self, interfaces):
        ranges = []
        current_range = []
        prev_interface = None

        for interface in sorted(interfaces):
            if prev_interface and not self.is_successor(prev_interface, interface):
                self.append_range(ranges, current_range)
                current_range = []

            current_range.append(interface)
            prev_interface = interface

        self.append_range(ranges, current_range)
        return ranges

    def is_successor(self, interface1, interface2):
        interface1_parts = interface1.split('/')
        interface2_parts = interface2.split('/')

        if len(interface1_parts) != len(interface2_parts):
            return False

        for i in range(len(interface1_parts)):
            if interface1_parts[i] != interface2_parts[i]:
                return False

        return int(interface2_parts[-1]) - int(interface1_parts[-1]) == 1

    def append_range(self, ranges, current_range):
        if current_range:
            if len(current_range) == 1:
                ranges.append(current_range[0])
            else:
                ranges.append(f"{current_range[0]}-{current_range[-1]}")


