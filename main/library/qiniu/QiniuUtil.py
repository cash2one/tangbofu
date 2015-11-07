# -*- coding: utf-8 -*-
from qiniu import Auth
from tangbofu.settings import *

class QiniuUtil:

    def __init__(self):
        pass

    @staticmethod
    def token(key):
        q = Auth(QINIU_AK, QINIU_SK)
        policy =  {
            'callbackUrl': '/qiniu_callback',
            'callbackBody': 'key=$(key)',
        };
        token = q.upload_token(QINIU_BUCKET_NAME, key, 7200, policy)
        return token