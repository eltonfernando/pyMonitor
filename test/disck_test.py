from hardware_monitor import Machine


def test_dick():
    pc = Machine()
    disk = pc.disk()
    print(disk)
