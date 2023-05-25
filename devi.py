from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish/<cherry>/')
def wish(cherry):
    return f'{cherry} This is Our Second Flask Class'



if __name__=='__main__':
    FAI.run(debug=True,host='127.0.0.1',port=5001)



















