# -*- coding:cp949 -*-
from http.client import HTTPSConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

conn = None
client_id = "J0xlzLY_mwqXVGY7OBho"
client_secret = "8NphEmVq6H"

# ���̹� OpenAPI ���� ���� information
server = "openapi.naver.com"

# smtp ����
host = "smtp.gmail.com"  # Gmail SMTP ���� �ּ�.
port = "587"


def userURIBuilder(uri, **user):
    str = uri + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str


def connectOpenAPIServer():
    global conn, server
    conn = HTTPSConnection(server)
    conn.set_debuglevel(1)


def getBookDataFromISBN(isbn):
    global server, conn, client_ID, client_secret
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilder("/v1/search/book_adv.xml", display="1", start="1", d_isbn=isbn)
    conn.request("GET", uri, None, {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        print("Book data downloading complete!")
        return extractBookData(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    # Book ������Ʈ�� �����ɴϴ�.
    itemElements = tree.iter("item")  # return list type
    # itemElements = tree.getiterator("item")  # return list type
    print(itemElements)
    for item in itemElements:
        isbn = item.find("isbn")
        strTitle = item.find("title")
        print(strTitle)
        if len(strTitle.text) > 0:
            return {"ISBN": isbn.text, "title": strTitle.text}


def sendMain(name, m_info, email, location, height):
    global host, port
    title = name
    senderAddr = 'leejungkeuen@gmail.com'
    recipientAddr = email
    passwd = 'nsrq nopj ghxo zqxi'

    html = f"""
    <html>
    <body>
        <h2>{name} ����</h2>
        <p><strong>�� �̸�:</strong> {name}</p>
        <p><strong>����:</strong> {location}</p>
        <p><strong>�ع߰�:</strong> {height} M</p>
        <p><strong>�� ����:</strong> {m_info}</p>
    </body>
    </html>
    """

    import mysmtplib
    # MIMEMultipart�� MIME�� �����մϴ�.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container�� �����մϴ�.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    MountainPart = MIMEText(html, 'html', _charset='UTF-8')

    # �޼����� ������ MIME ������ ÷���մϴ�.
    msg.attach(MountainPart)

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # �α��� �մϴ�.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")

