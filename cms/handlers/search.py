#! /usr/bin/env python
#coding:utf-8

from handlers.admin import SignValidateBase, ArticleListObject
import tornado.web
'''
class ListSearch(SignValidateBase):
    def get(self):
        self.pagination = Pagination()
        targetpage = int(self.get_argument('page', default='1'))
        keyword = self.get_argument('keyword', default='')
        articlelist = []
        for article in self.session.query(Article):
            if keyword in article.atitle or keyword in article.acontent:
                article.insert(0, articlelist)

        articlelist = [ArticleListObject(article) for article in articlelist]

        articlelist, self.pagination = genertePagination()
'''
