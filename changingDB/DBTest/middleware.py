def my_middleware(get_response):



    def m(request):
        print('m is called')


        response = get_response(request)



        print('m is going to return responce ')
        return response

        

    
    print('my middleware is going to end ')
    return m
