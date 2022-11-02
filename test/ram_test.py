from hardware_monitor import Machine


def test_ram():
    pc = Machine()
    ram = pc.ram()
    print(ram)