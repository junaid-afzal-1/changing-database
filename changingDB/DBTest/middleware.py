from django.http import request
import logging
logging.basicConfig(level=logging.INFO,filename='my loggr.log')

def my_middleware(get_response):


    l = logging.getLogger()
    request_count = 0
    request_count += 1

    



    def m(request):
        
        #print('m is called')

        l.info(str(request.path + '  ' + str(request.content_params) + '   '+ str(request.path_info)))
        l.info(str(request.META.get('REMOTE_ADDR')))
        l.info('request count ' + str(request_count))


        f = open('views_record.txt',mode='a')
        f.write(str(request.path + '  ' + str(request.content_params) + '   '+ str(request.path_info)))
        f.write('\n')
        print(request.path)

        f.write('ip is:\n')
        f.write(str(request.META.get('REMOTE_ADDR')))


        response = get_response(request)



        #print('m is going to return responce ')
        return response

        

    
    #print('my middleware is going to end ')

    #f.close()
    return m
