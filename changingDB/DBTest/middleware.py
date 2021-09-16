from django.http import request


def my_middleware(get_response):


    


    def m(request):
        print('m is called')
        f = open('views_record.txt',mode='a')
        f.write(str(request.path + '  ' + str(request.content_params) + '   '+ str(request.path_info)))
        f.write('\n')
        print(request.path)


        response = get_response(request)



        print('m is going to return responce ')
        return response

        

    
    print('my middleware is going to end ')

    #f.close()
    return m
