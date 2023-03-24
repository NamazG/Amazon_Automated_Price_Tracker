from bs4 import BeautifulSoup
import requests
import smtplib
import os

# ------------------------- Web Scraping Amazon for Price of an Item ------------------

headers = {
    "User-Agent":
        os.environ.get("USER-AGENT"),
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get("https://www.amazon.ca/Samsung-32-Inch-Monitor-Streaming-LS32BM500ENXGO/dp/B09YN2G35W/ref=pd_rhf_d_dp_s_pd_sbs_rvi_sccl_2_10/132-5107081-3058702?pd_rd_w=9NODo&content-id=amzn1.sym.c4b12d63-26ee-451b-a00e-167063525dc5&pf_rd_p=c4b12d63-26ee-451b-a00e-167063525dc5&pf_rd_r=G8F7W9RD16PJYMR5PJHW&pd_rd_wg=r8jKC&pd_rd_r=230316c7-94df-432e-8915-89c34a009ea5&pd_rd_i=B09YN2G35W&psc=1",
                        headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")
price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])

# ------------------------- Comparing Price and Sending Discount Price via Email ------------------------------

if price <= 300:
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs="zscorpio@bk.ru",
                            msg=f"Subject: Discount on the Item!\n\nThe price is now ${price}. Hurry up and buy it!")