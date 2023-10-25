class SalaryException(Exception):
    def __init__(self,args):
        self.msg = args

class UpdateSalaryException(Exception):
    def __init__(self,args):
        self.msg = args

class SerialNoException(Exception):
    def __init__(self,args):
        self.msg = args

class OptionException(Exception):
    def __init__(self,args):
        self.msg = args