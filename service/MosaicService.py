from function.Mosaic import *

class Mosaic:
    
    def image():
        # s3에서 데이터 가져오기
        Mosaic.bring_file_from_aws_s3()
        # 기능 수행
        
        # s3에 데이터 저장하기
        Mosaic.store_file_at_aws_s3()
        
        return
    
    def video():
        # s3에서 데이터 가져오기
        Mosaic.bring_file_from_aws_s3()
        # 기능 수행
        
        # s3에 데이터 저장하기
        Mosaic.store_file_at_aws_s3()
        
        return