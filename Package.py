import copy
from Style import Style

class Package:
    def __init__(self, ID, address, city, state, zip, deadline, weight_kilos, phase):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight_kilos = weight_kilos
        self.phase = phase
        self.delivery_time = None
        self.assigned_truck = Style.set_style("Assigned truck: TBD", Style.YELLOW)

    def __str__(self):
        # Format delivery_time to display only the time part and set the color to CYAN
        delivery_time_str = self.delivery_time.strftime('%H:%M:%S') if self.delivery_time else 'TBD'
        delivery_time_str = "\nTime delivered: " + delivery_time_str
        delivery_time_str = Style.set_style(delivery_time_str, Style.CYAN)

        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip,
                                                       self.deadline, self.weight_kilos, self.phase, delivery_time_str, self.assigned_truck)
    
    def clone(self): 
        # Create a deep copy of the Package instance
        return copy.deepcopy(self)