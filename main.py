

import DownloadFiles
import UploadFiles
import DeleteFiles


if __name__ == '__main__':

    #download file
    objectDow = DownloadFiles.DownloadFile("<bucketName>", "<filename>")
    result = objectDow.Download()
    print(result)

    #upload file
    objectUp = UploadFiles.UploadFile("<bucketName>", "<filename>")
    result = objectUp.Upload()
    print(result)

    #delete file
    objectDel = DeleteFiles.DeleteFile("<bucketName>", "<filename>")
    result = objectUp.Delete()
    print(result)



