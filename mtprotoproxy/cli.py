from mtprotoproxy import server


def run():
    server.init_ip_info()
    server.print_tg_info()
    server.main()


if __name__ == '__main__':
    run()
