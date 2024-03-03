class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and (len(name) >= 3) and not hasattr(self, "name"):
            self._name = name
        # else:
        #     raise Exception
    
    # QUESTION: why does the above not work if i uncomment out the exception?
    # Also, why does the below not need to include the len(name) >= 3 to pass the more than 3 characters validation?

    # @name.setter
    # def name(self, name):
    #     if isinstance(name, str) and not hasattr(self, "name"):
    #         self._name = name
    #     else:
    #         raise Exception
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    # the solution files shows: return max(set(visitors), key = visitors.count)
    # not sure which why they would do that
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max((visitors), key = visitors.count)
    
    @classmethod
    def most_visited(cls):
        return max(cls.all, key = lambda park: park.total_visits())


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        # NOTE: type(self).all.append(self) is identical to below
        Trip.all.append(self)


    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and (len(start_date) >= 7):
            self._start_date = start_date
        # else:
        #     raise Exception
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and (len(end_date) >= 7):
            self._end_date = end_date
        # else:
        #     raise Exception
    
    @property
    def visitor(self):
        return self._visitor
    
    # NOTE: because all the classes are in one file, i do not need to import the Visitor class here
    # If they were separate files, we would need to import:
    # from Visitor import Visitor 
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception

class Visitor:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name (self, name):
        if isinstance(name, str) and  (1 < len(name) < 15):
            self._name = name
        # else:
        #     raise Exception
            
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        pass