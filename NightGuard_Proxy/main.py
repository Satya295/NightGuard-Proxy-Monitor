import ssl
import threading
import flask
import requests
from flask_cors import CORS
from email.message import EmailMessage
import smtplib
import time

app = flask.Flask(__name__)
app.config["DEBUG"] = True
global proxy_status_count
proxy_status_count = 0

# Allow cross-origin
CORS(app)
cors = CORS(app, resources={
    r"/": {
        "origins": "*"
    }
})

# global variables
email_sender = "nightguardproxy@gmail.com"
email_password = "pjpqgqimdskwiysc"
email_receiver = ["Vamsieagala@gmail.com", "Vamsieagala2@gmail.com"]
email_subject = "Proxy Monitor Alert [URGENT]"

module_addresses = [
    ["Transaction Engine", "127.0.0.1:5501/keepalive"],
    ["Banking Bank End", "127.0.0.1:5502/keepalive"],
    ["Cash Manager Database", "127.0.0.1:5503/keepalive"]]


@app.route("/proxy_monitor", methods=["GET"])
def check_keep_alive():
    print("***** check_keep_alive is calling *****")
    up_module_name = []
    down_module_name = []
    down_module_address = []
    global proxy_status_count
    proxy_status_description = ""
    timestamp = time.time()
    timestamp = str(timestamp).replace(".", "")

    # if any module addresses are not defined
    if not module_addresses:
        proxy_status = 200
        proxy_status_description = "No modules available"

        obj = {
            "proxy_status": proxy_status,
            "proxy_status_description": proxy_status_description,
            "up_module_name": up_module_name,
            "down_module_name": down_module_name,
            "down_module_address": down_module_address
        }

    # if any module addresses are defined
    else:
        proxy_status = 200
        proxy_status_description = len(module_addresses), " modules available"

        # checking keep alive one by one
        # and waiting for 40 seconds until get a reply
        for module in module_addresses:
            try:
                result = requests.get("http://" + str(module[1]), timeout=40)
                print(result)
                print("Keep alive module: " + module[0] + " success")
                up_module_name.append(module[0])

            except Exception as e:
                proxy_status = 200
                proxy_status_description = module[0] + " keep alive failed"
                down_module_name.append(module[0])
                down_module_address.append(module[1])
                print(e)

        obj = {
            "proxy_status": proxy_status,
            "proxy_status_description": proxy_status_description,
            "up_module_name": up_module_name,
            "down_module_name": down_module_name,
            "down_module_address": down_module_address
        }

        # check whether there are any down modules
        # if the up module count is increased (means: Down module is up and running again)
        if len(up_module_name) > proxy_status_count:
            print("Up Count: ", len(up_module_name))
            print("Status count: ", proxy_status_count)
            print("timestamp: ", timestamp)
            proxy_status_count = len(up_module_name)
            alert_manager(1, up_module_name, down_module_name, timestamp)

        # if the up module count is decreased
        elif len(up_module_name) < proxy_status_count:
            print("Up Count: ", len(up_module_name))
            print("Status count: ", proxy_status_count)
            print("timestamp: ", timestamp)
            proxy_status_count = len(up_module_name)
            alert_manager(2, up_module_name, down_module_name, timestamp)

        # if the up module count is same as before
        else:
            print("Up Count: ", len(up_module_name))
            print("Status count: ", proxy_status_count)
            print("All modules are up and running")

    print(obj)
    return obj


# function to send emails out to stakeholders
def alert_manager(status, up_module_name, down_module_name, timestamp):
    print("***** alert_manager is calling *****")
    print()
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = email_subject + " Ticket ID: " + timestamp

    if status == 1:
        salutation = "Hello User,\n\n"
        content_01 = "The Night Guard Proxy monitor detected that the down module is up & running again. But, We will keep our eye on the modules\n\n"
        content_02 = "Up modules: " + str(up_module_name) + "\n"
        content_03 = "Down modules: " + str(down_module_name) + "\n"
        content_04 = "\n\nThank you\nNight Guard Proxy Service"

    else:
        salutation = "Hello User,\n\n"
        content_01 = "The Night Guard Proxy monitor detected that the below module(s) are DOWN. Please give your attention!\n\n"
        content_02 = "Up modules: " + str(up_module_name) + "\n"
        content_03 = "Down modules: " + str(down_module_name) + "\n"
        content_04 = "\n\nThank you\nNight Guard Proxy Service"

    email_body = salutation + content_01 + content_02 + content_03 + content_04
    em.set_content(email_body)
    context = ssl.create_default_context()

    # sending email one by one to the all users defined
    print("attempting to send emails")
    for user in email_receiver:
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, user, em.as_string())
                print("emails sent to: " + user + " successfully")
        except:
            print("emails sending failed. Please check email address")


# if __name__ == "__main__":
#     check_keep_alive()

app.run(port=5500)
