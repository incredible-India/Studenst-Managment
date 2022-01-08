class verification:
    def __init__(self,get_response):
        self.get_response = get_response

    
    def __call__(self,request):
        fname = request.session.get('fname',None)
        essn = request.session.get('essn',None)
        log = request.session.get('log',None)

        if fname == None or essn == None or log == None:
            request.isverified = False
        else:
            request.isverified = True
            request.fname = fname
            request.essn = essn
            request.log = log
        
        response = self.get_response(request)    
        return response