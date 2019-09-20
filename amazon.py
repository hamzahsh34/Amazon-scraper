import requests
from bs4 import BeautifulSoup
import smtplib


def convert(string: str) -> float:
    CAD = []
    for i in string.split():
        try:
            CAD.append(float(i))
        except:
            pass
    return CAD[0]


def email():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Google apps password
    password = "secretsecret"
    server.login("hamzaleafs@gmail.com", password)
    subject = "Price fell"
    body = "Check amazon: https: // www.amazon.ca/dp/B0749ZSPN7?ref_ = nav_em_T1_0_4_7_1__k_ods_ha_rr"
    message = f"Subject: {subject}\n\n{body}"

    server.sendmail("hamzaleafs@gmail.com",
                    "hamzahshahid0@gmail.com", message)

    server.quit()


# Any amazon URL works
URL = "https://www.amazon.ca/dp/B0749ZSPN7?ref_=nav_em_T1_0_4_7_1__k_ods_ha_rr"

# Google your user agent
root = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

if __name__ == "__main__":

    web = requests.get(URL, headers=root)

    scrape1 = BeautifulSoup(web.content, "html.parser")
    scrape2 = BeautifulSoup(scrape1.prettify(), "html.parser")

    title = scrape2.find(id="productTitle").get_text()
    price = scrape2.find(id="priceblock_ourprice").get_text()
    new_price = convert(price)

    # Current price
    if new_price < 99.99:
        email()
