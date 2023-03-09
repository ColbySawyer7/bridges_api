from classes.vm import VM 
from classes.port import Port
from classes.vc import VC

def main():
    # Create VMs
    vm1 = VM('vm1', vcpus=10, vmem=1024, ports=[Port('eno1','ethernet'),Port('eno2','ethernet')])
    vm2 = VM('vm2', vcpus=12, vmem=2048, ports=[Port('enops3','ethernet'),Port('eno2','ethernet')])

    # Create VC
    vc1 = VC(src=vm1, dest=vm2)

    # Create VMs
    vm3 = VM('vm3', vcpus=10, vmem=1024, ports=[Port('eno1','ethernet'),Port('eno2','ethernet')])
    vm4 = VM('vm4', vcpus=12, vmem=2048, ports=[Port('enops3','ethernet'),Port('eno2','ethernet')])

    # Create VC
    vc2 = VC(src=vm3, dest=vm4)

    objects =[vm1, vm2, vc1, vm3, vm4, vc2]
    for obj in objects:
        # Reserve 
        try:
            obj.reserve()
        except Exception as e:
            print(f'Error when reserving {obj.name}: {e}')

        # Provision
        try:
            obj.provision()
        except Exception as e:
            print(f'Error when provisioning {obj.name}: {e}')

        # Release
        try:
            obj.release()
        except Exception as e:
            print(f'Error when releasing {obj.name}: {e}')

        # Terminate
        try:
            obj.terminate()
        except Exception as e:
            print(f'Error when terminating {obj.name}: {e}')

