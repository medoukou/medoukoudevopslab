class FilterModule(object):
    def filters(self):
        return {
            'format_cisco_interface_list': self.format_cisco_interface_list
        }

    def format_cisco_interface_list(self, interfaces):
        formatted_list = []
        start_range = None
        last_interface = None

        for interface in interfaces:
            if start_range is None:
                start_range = interface
            elif last_interface is not None and int(interface.split('/')[-1]) != int(last_interface.split('/')[-1]) + 1:
                formatted_list.append(f"{start_range}-{last_interface}")
                start_range = interface

            last_interface = interface

        formatted_list.append(f"{start_range}-{last_interface}")
        return ', '.join(formatted_list)
