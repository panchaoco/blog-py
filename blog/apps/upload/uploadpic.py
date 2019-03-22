# -*- coding: utf-8 -*-
__author__ = 'panchao'

import io
import uuid

import qiniu
from PIL import Image
from django.conf import settings

q = qiniu.Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)


def upload(img):
  _img = img.read()
  size = len(_img) / (1024 * 1024)  # 上传图片的大小 M单位

  image = Image.open(io.BytesIO(_img))

  key = str(uuid.uuid1()).replace('-', '')

  name = 'upfile.{0}'.format(image.format)  # 获取图片后缀（图片格式）

  if size > 1:
    # 压缩
    x, y = image.size
    im = image.resize((int(x / 1.73), int(y / 1.73)), Image.ANTIALIAS)  # 等比例压缩 1.73 倍
  else:
    # 不压缩
    im = image

  im.save('./media/' + name)  # 在根目录有个media文件
  path = './media/' + name

  token = q.upload_token(settings.QINIU_BUCKET_NAME, key, 3600, )

  qiniu.put_file(token, key, path)
  url = 'http://por9999si.bkt.clouddn.com/{}'.format(key)
  return url
