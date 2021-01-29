from google.cloud import storage


client = storage.Client.from_service_account_json("<ServiceAccountsKeyJson>")


class DownloadFile:
    def __init__(self, bucketName, fileName):
        self.bucketName = bucketName
        self.fileName = fileName

    def Download(self):
        try:
            # define bucket
            bucket = client.get_bucket(self.bucketName)

            filename = list(bucket.list_blobs(prefix=''))
            # search file
            for name in filename:
                if self.fileName in name.name:
                    #download file
                    blob = bucket.get_blob(name.name)
                    blob.download_to_filename(str(name.name))


            return str(name.name)
        except Exception as e:
            return  str(e)






