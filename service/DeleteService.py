from function.DeleteProcess import *

class Delete:
    
    def image():
        # s3에서 데이터 가져오기
        Delete.bring_file_from_aws_s3()
        # 기능 수행
        
        # s3에 데이터 저장하기
        Delete.store_file_at_aws_s3()
        
        return
    
    def video():
        # s3에서 데이터 가져오기
        Delete.bring_file_from_aws_s3()
        # 기능 수행
        
        # s3에 데이터 저장하기
        Delete.store_file_at_aws_s3()
        
        return