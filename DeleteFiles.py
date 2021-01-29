from google.cloud import storage


client = storage.Client.from_service_account_json("<ServiceAccountsKeyJson>")


class DeleteFile:
    def __init__(self, bucketName, fileName):
        self.bucketName = bucketName
        self.fileName = fileName

    def Delete(self):
        try:
            # define bucket
            bucket = client.get_bucket(self.bucketName)

            filename = list(bucket.list_blobs(prefix=''))
            # search file
            for name in filename:
                if self.fileName in name.name:
                    #delete file
                    bucket.delete_blob(name.name)


            return 'Deleted'
        except Exception as e:
            return  str(e)






