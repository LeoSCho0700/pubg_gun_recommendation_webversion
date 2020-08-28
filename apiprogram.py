from flask import Flask
from flask_restx import Resource, Api
import pymysql
from flask_cors import CORS
from flask_restx import reqparse, abort, Api, Resource

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)



@api.route('/guns/<map>/<distance>/<situations>/<ammo>')
class map(Resource):
    def get(self,map,distance,situations,ammo):
        returnlist=[]
        conn = pymysql.connect(host='localhost', user='root', password='KimYJ1004!', db='user', charset='utf8')
        curs = conn.cursor()

        n = """SELECT * FROM user.PUBG WHERE gun_"""+map+"""=1 and gun_ammunition='"""+ammo+"""' and gun_hashtag like '%%"""+situations+"""%%' and gun_hashtag like '%%"""
        n = """SELECT * FROM user.PUBG WHERE gun_%s=1 and gun_ammunition='%s' and gun_hashtag like '%%%s%%' and gun_hashtag like '%%%s%%'""" % (map,ammo,situations,distance)
        print(n)

        curs.execute(n)
        rows=curs.fetchall()
        for i in rows:
            returnlist.append({'name': i[0], 'ammunition': i[1], 'type': i[2], 'information': i[-1]})

        return returnlist





if __name__ == '__main__':
    # app = Flask(__name__)
    app.run(debug=True)
