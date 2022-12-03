"""
Adapted from
https://www.educative.io/edpresso/how-to-send-emails-using-python?fbclid=IwAR2kQYpvPac8t273HnLjpEYoIY2K3_AW9y-5ewEtzeq8M_5_r4Yf6r3wAs0
and
https://stackoverflow.com/questions/920910/sending-multipart-html-emails-which-contain-embedded-images?fbclid=IwAR1fHC4KYyV3rMSiD1GdcDcBmLiAyNIoA3lH-iR2c6lTa4g9NacTRoMOjqk
"""
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


with open('email_login.json') as f:
    LOGIN = json.load(f)


def send_email(receiver, message):
    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = 'Mère Noël \U0001f936'
    msgRoot['To'] = receiver
    msgRoot['Subject'] = (
        "\U0001f384 \u2744\uFE0F \u26C4 "
        "Secret santa avenue de Saint-Mandé \u26C4 \u2744\uFE0F \U0001f384")

    msgText = MIMEText(message, 'html')
    msgRoot.attach(msgText)

    with open('maman_noel.jpg', 'rb') as f:
        msgImage = MIMEImage(f.read())

    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    email = smtplib.SMTP('smtp.gmail.com', 587)
    email.starttls()
    email.login(LOGIN['email'], LOGIN['password'])
    email.sendmail(LOGIN['email'], receiver, msgRoot.as_string())
    email.quit()
    return


if __name__ == '__main__':
    with open("participants.json") as f:
        PARTCIPANTS = json.load(f)

    for name, email in PARTCIPANTS.items():
        with open(f"packages/{name}.txt") as f:
            message = f.read().format(giver=name)
        send_email(email, message)
