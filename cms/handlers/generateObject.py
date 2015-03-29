#! /usr/bin/env python
#coding=utf-8

class ArticleListObject(object):
    def __init__(self, article):
        self.id = article.aid
        self.title = article.atitle
        self.subcontent = article.acontent[:300]
        self.content = article.acontent
        self.type = article.atype.typename
        self.typelink = ''
        self.pubtime = article.apubtime.ctime()[:16]
        self.chgtime = article.achgtime.ctime()[:16]
        self.user = article.auser.username
        self.useravatar = article.auser.uavatar
        self.userlink = '/members/m/' + str(article.auser.uid)

class PageListObject(object):
    def __init__(self, page):
        self.pid = page.pid
        self.ptitle = page.ptitle
        self.pcontent = page.pcontent
        self.ppubtime = page.ppubtime.ctime()[:16]
        self.pchgtime = page.pchgtime.ctime()[:16]
        self.ppic = page.ppic

class MeetinfoObject(object):
    def __init__(self, meetinfo):
        self.mid = meetinfo.mid
        self.mtitle = meetinfo.mtitle
        self.mcontent = meetinfo.mcontent
        self.mcettime = meetinfo.mcettime.ctime()[:16]
