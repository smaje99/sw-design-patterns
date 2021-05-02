from proxy import ProxyInternet


def main():
    internet = ProxyInternet()
    try:
        internet.connect_to('udemy.com')
        internet.connect_to('facebook.com')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
