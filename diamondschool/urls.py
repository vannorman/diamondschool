from django.conf.urls import *

import diamondschool.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'diamondschool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', diamondschool.views.home),
	url(r'^blog/$', diamondschool.views.blog_base), 
	url(r'^base/$', diamondschool.views.simple_page('base.html')), 
	url(r'^resume/$', diamondschool.views.simple_page('resume.html')), 
	url(r'^portfolio/$', diamondschool.views.simple_page('portfolio.html')), 
	url(r'^address/$', diamondschool.views.simple_page('address.html')), 
	url(r'^blog/(.*)/$', diamondschool.views.blog), 
	url(r'^.well-known/acme-challenge/p_LTkY9QHhcECb6Lv1UZWYQ6rawjuQLnUAdBdZZE9kk', diamondschool.views.file_a),
	url(r'^.well-known/acme-challenge/v9b5S4UbuLtvh_PwuhqjfOUnVfiulJSmFCYkNHtD6mA', diamondschool.views.file_b),


	url(r'^messages/whatyouwant$', diamondschool.views.simple_page('messages/isthiswhatyouwant.html')), 




]
