#! /usr/bin/env python
#coding=utf-8

from handlers import admin, home, upload, exception, mail

homeurls = [

   #前台
   (r"/",home.Home),
   (r"/projects/([0-9]+)",home.ListProjects),
   (r"/articles/([0-9]+)",home.ListArticles),
   (r"/members",home.ListMembers),
   (r"/about",home.ShowAbout),
   (r"/contact",home.ShowContact),
   (r"/upload/?",upload.FileUpload),
   (r"/projects/p/([0-9]+)",home.ShowProjects),
   (r"/articles/a/([0-9]+)",home.ShowArticles),
   (r"/members/m/([0-9]+)",home.ShowMyPage),
   #(r"/type/([0-9a-zA-Z]*)",home.ShowAbout),

   (r"/members/m/([0-9]+)/write",home.EditArticle),
   (r"/members/m/([0-9]+)/profile",home.EditProfile),
   #(r"/members/m/([0-9]+)/setting/",admin.EditProfile),

   #后台
   (r"/signin",admin.Signin),
   (r"/signup",admin.Signup),
   (r"/signout",admin.Signout),
   (r"/admin",admin.AdminHome),
   (r"/admin/editpage",admin.EditPage),
   (r"/admin/limits",admin.EditLimits),
   (r"/admin/reports",admin.ListReports),
   (r"/admin/slide",admin.SlideOption),
   (r"/admin/link",admin.LinkOption),
   (r"/admin/meetinfo",admin.MeetinfoOption),
   (r"/admin/changechecked",admin.ChangeChecked),

   (r"/admin/mail",mail.MailSending),




   (r".*", exception.ErrorHandler)
]
