import datetime, pytz, random

admin_timestamp = '2022-09-22 09:41:17'

admin_timestamp_object = datetime.datetime.strptime(admin_timestamp, '%Y-%m-%d %H:%M:%S')
                     
given_timezone = pytz.timezone('Asia/Singapore')
                     
admin_timestamp_object_with_timezone = given_timezone.localize(admin_timestamp_object)
                                    
seed = int(admin_timestamp_object_with_timezone.timestamp())
                     
random.seed(seed)
                     
admin_token = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16))
                     
print(admin_token)
