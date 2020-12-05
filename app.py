import requests
import smtplib

from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}


def checkPrice(url, target):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    title = title[0:34]
    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)
    if price < target:
        return send_mail(title, url)


def send_mail(title, url):
    sender = '...@gmail.com' #SMTP mail
    receiver = '..@hotmail.com' # target mail adress
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, '') # Gmail app password
        subject = title + ' fiyatı düştü '
        body = 'Bu linkten gidebilirsin : ' + url
        mailContent = f"To:{receiver}\nFrom {sender}\nSubject: {subject}\n\n{body}"
        server.sendmail(sender, receiver, mailContent)
        return True
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()
