from django.views.generic import View, TemplateView
from django.http import HttpResponse , JsonResponse

class PostList1(View):

    def get(self, request):
        name = '건일'
        html =self.get_template_string().format(name="23살")
        return HttpResponse(html)


    def get_template_string(self):
        return """
                <h1>장건이 짱 멋쟁이</h1>
                <p>{name}<p>
                <p>여러분의 파이썬  & 장고 페이스메이커가 되어드리겠습니다.<p>
              """
post_list1 = PostList1.as_view()



class PostList2(TemplateView):
    template_name = 'dojo/post_list.html'


    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '24살'
        return context
post_list2 = PostList2.as_view()





class PostList3(object):
    pass


class excel_download(object):
    pass
