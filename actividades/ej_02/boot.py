def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Conectandose...')
        sta_if.active(True)
        sta_if.connect('Cooperadora Alumnos', '')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())