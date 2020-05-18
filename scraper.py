import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://gtracing.com/collections/gtracing-music-series/products/music-series-gt890mf-red'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
}

def check_avail():
    page = requests.get(URL, headers = headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')

    btn = soup.find('button', {
        'class': 'shopify-payment-button__button'
    })

    btn_attrs = btn.__dict__['attrs']

    btn_disabled = ('disabled' in btn_attrs and btn_attrs['disabled'] != 'disabled') or 'disabled' not in btn_attrs

    if btn_disabled:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Your source email address goes here.', 'Your email password or mail app password goes here.')

    subject = 'Chair is available!'
    
    body = 'Check the GTRacing link - https://gtracing.com/collections/gtracing-music-series/products/music-series-gt890mf-red'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'Source email address goes here.',
        'Destination email address goes here.',
        msg
    )

    print('Hey, email has been sent!')

    server.quit()

while True:
    check_avail()
    time.sleep(60 * 30)