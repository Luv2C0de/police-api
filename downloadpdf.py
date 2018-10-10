import urllib.request


def download_file():

    links = []

    for i in range(1, 30):
        if(i < 10):
            links.append(f'http://www.tipsoftonline.com/Push/uploads/572/090{i}18NM.pdf')
        else:
            links.append(f'http://www.tipsoftonline.com/Push/uploads/572/09{i}18NM.pdf')

    i = 1

    for link in links:
        try:
            urllib.request.urlretrieve(link, f'test{i}.pdf')
        except Exception as e:
            pass

        i += 1

    #     # file = open("document.pdf", 'wb')
    #     # file.write(response.read())
    #     # file.close()
    #     # print("Completed")


if __name__ == "__main__":
    download_file()
