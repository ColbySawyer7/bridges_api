#from classes.atomic import Atomic

class VM():
    def __init__(self, name,  vcpu, vmem, ports, obj='atomic'):
        self.name = name
        self.obj = obj
        self.vcpu = vcpu
        self.vmem = vmem
        self.ports = ports

        def reserve():
            # do work here
            return False
        
        def provision():
            # do work here 
            return False
        
        def release():
            # do work here 
            return False
        
        def terminate():
            # do work here 
            return False