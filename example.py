#!/usr/bin/env python
# coding:utf-8
# Author: veelion@ebuinfo.com

from sanic import Sanic
from sanic import response
from sanicdb import SanicDB

app = Sanic('demo')
db = SanicDB('localhost', 'the_db', 'the_user', 'the_password', sanic=app)


@app.route('/')
async def index(request):
    sql = 'select * from test where id=1'
    data = await app.db.query(sql)
    return response.json(data)


if __name__ == '__main__':
    app.run()
