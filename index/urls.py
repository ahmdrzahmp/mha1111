from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index_url, name='index_url'),
    path('Speaker/', views.index_detail, name='index_detail'),
    path('', views.index, name='index_index'),
    path('schedule/', views.schedule, name='index_schedule'),
    path('tabbed-layout/', views.tabbed_layout, name='inedx_layout'),
    path('404-page/', views.error_page, name='index_404'),
    path('pricing-table/', views.pricing_table, name='index_pricing'),
    path('coming-soon/', views.coming_soon, name='index_coming'),
    path('content-us/', views.content_us, name='index_content'),
    path('about-us/', views.about_us, name='index_about'),
    path('blog/', views.blog, name='index_blog'),
    path('blog-page-2/', views.blog_page2, name='index_blog_page2'),
    path('cart/', views.cart, name='index_cart'),
    path('checkout/', views.checkout, name='index_checkout'),
    path('shop/', views.shop, name='index_shop'),
]