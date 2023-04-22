import os
import requests
from requests.auth import HTTPDigestAuth
from datetime import datetime
import time
import schedule
import dropbox
from dropbox.exceptions import AuthError

def refreshDropboxToken(access_token, refresh_token, app_key, app_secret):

    try:
        dbx = dropbox.Dropbox(oauth2_access_token=access_token,
                              oauth2_refresh_token=refresh_token,
                              app_key=app_key, app_secret=app_secret)

        access_token = dbx.check_and_refresh_access_token()
        if access_token != 'None':
            new_access_token = access_token
            print("Received new access token:")
            print(new_access_token)
            return new_access_token
        else:
            print("Existing token still valid")
            print(access_token)
            return access_token

    except AuthError as e:
        print("Error getting new access token")
        return -1


def UploadImg(file_from, file_to, access_token,refresh_token, app_key,app_secret):

    print(file_from)

    # API v2
    try:
        dbx = dropbox.Dropbox(oauth2_access_token=access_token,
                              oauth2_refresh_token=refresh_token,
                              app_key=app_key, app_secret=app_secret)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
        print("Upload complete")
        try:
            os.remove(file_from)
            print("Successfully deleted uploaded file from local drive")
        except:
            print("Failed to delete uploaded file from local drive")
    except:
        print("Failed to upload")

def HikGetImage(fileName, url, username, password):

    try:
        response = requests.get(url, auth=HTTPDigestAuth(username, password))

        with open(fileName + '.jpg', 'wb') as f:
            f.write(response.content)

        print("Acquired image: " + fileName + ".jpg")

    except:
        print("Failed to acquire image")

def main():
    def job():
        url = 'http://<IP_CAM_URL>:<PORT>/ISAPI/Streaming/channels/101/picture'
        username = '<USERNAME>' #!!REQUIRED!!
        password = '<PASSWORD>' #!!REQUIRED!!


        app_key = '<DROPBOX_APP_KEY>' #!!REQUIRED!!
        app_secret = '<DROPBOX_APP_SECRETKEY>' #!!REQUIRED!!
        access_token = '<DROPBOX_ACCESSTOKEN>'
        refresh_token = '<DROPBOX_REFRESH_TOKEN>' #!!REQUIRED!!

        # get timestamp to use for filename
        dt_string = datetime.now().strftime("%d_%m_%Y_%H.%M.%S")
        # Acquire image from IP camera
        HikGetImage(dt_string, url, username, password)
        # Update Dropbox access token if required
        access_token = refreshDropboxToken(access_token, refresh_token, app_key, app_secret)
        # Assign file names
        file_from = dt_string + '.jpg'
        file_to = '/images/' + file_from
        # Upload to dropbox
        UploadImg(file_from, file_to, access_token, refresh_token, app_key, app_secret)
        # UploadImg(dt_string + '.jpg', access_token)
        time.sleep(1)

    print("<INIT>")

    schedule.every().day.at("10:00").do(job)
    schedule.every().day.at("12:00").do(job)
    schedule.every().day.at("14:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
