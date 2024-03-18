from django.test import SimpleTestCase
from django.urls import reverse,resolve
from blog.views import home,about,contact,dashboard,signup,ulogin,ulogout,add_post,update,deleted,details

class test_urls(SimpleTestCase):
    def testhome(self):
        url=reverse('home')
        self.assertEqual(resolve(url).func,home)

    def testabout(self):
        url=reverse("about")
        self.assertEqual(resolve(url).func,about)

    def testcontact(self):
        url=reverse("contact")
        self.assertEqual(resolve(url).func,contact)
    
    def testdashboard(self):
        url=reverse("dashboard")
        self.assertEqual(resolve(url).func,dashboard)

    def testsign(self):
        url=reverse("signup")
        self.assertEqual(resolve(url).func,signup)
    
    def testlogin(self):
        url=reverse("login")
        self.assertEqual(resolve(url).func,ulogin)
    
    def testlogout(self):
        url=reverse("logout")
        self.assertEqual(resolve(url).func,ulogout)
    
    def testaddpost(self):
        url=reverse("addpost")
        self.assertEqual(resolve(url).func,add_post)
    def testupdate(self):
        url=reverse("update",args=[12345])
        self.assertEqual(resolve(url).func,update)
    
    def testdelete(self):
        url=reverse("delete",args=[123456])
        self.assertEqual(resolve(url).func,deleted)
    def testdetails(self):
        url=reverse("detail",args=[1234])
        self.assertEqual(resolve(url).func,details)