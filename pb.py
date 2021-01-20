import http.client

token = str(input("Masukkan Token: "))
cookie = str(input("Masukkan Cookie: "))
conn = http.client.HTTPSConnection("topup.pointblank.id")
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  '__RequestVerificationToken': token,
  'Content-Type': 'application/json; charset=UTF-8',
  'Cookie': cookie
}
with open("pb.txt", "r") as file:
    for i in file:
        payload = '{"couponno":"%s"}'%(i)
        conn.request("POST", "/Coupon/Register", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))