from google.cloud import storage



client = storage.Client.from_service_account_json("<ServiceAccountsKeyJson>")


class UploadFile:
    def __init__(self, bucketName, fileName):
        self.bucketName = bucketName
        self.fileName = fileName

    def Upload(self):
        try:
            # define bucket
            bucket = client.get_bucket(self.bucketName)
            # upload file
            blob = bucket.blob(self.fileName)
            blob.upload_from_filename(self.fileName)
            return 'Uploaded'
        except Exception as e:
            return  str(e)






