from django.core.files.storage import default_storage
from django.shortcuts import render, redirect

from django.views import generic
from .forms import VoiceMapping, PlotForm

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Person

import sys
import io
import matplotlib.pyplot as plt
import numpy as np
import os
import wave

UPLOAD_DIR = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1]) + '/media/'  # アップロードしたファイルを保存するディレクトリ

# アップロードされたファイルのハンドル
def handle_uploaded_file(f):
    path = os.path.join(UPLOAD_DIR, f.name)
    print("handle_uploaded_file: ", path)
    file_name = default_storage.save(f.name, f)
    print(file_name)
    # for chunk in f.chunks():
    #     print(chunk)
    wf = wave.open(path, "r")
    # with open(path, 'wb+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)

class IndexView(generic.TemplateView):
    template_name = "index.html"
    model = Person
    person1 = model.objects.get(id=1)
    person2 = model.objects.get(id=2)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        context["person1"] = self.person1
        context["person2"] = self.person2
        return context

    # try:
    #     person1 = Person.objects.get(id=1)
    #     person2 = Person.objects.get(id=2)
    # except person1.DoesNotExist:
    #     person1 = None
    #     person2 = None


class VoiceMappingView(generic.FormView):
    form_class = VoiceMapping
    template_name = 'voice_mapping.html'
    # success_url = reverse_lazy('vmap:img_plot')
    model = Person
    person1 = model.objects.get(id=1)
    person2 = model.objects.get(id=2)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        context["person1"] = self.person1
        context["person2"] = self.person2
        return context

    def form_valid(self, form):
        handle_uploaded_file(self.request.FILES['file'])
        # return redirect('monitor:upload_complete')  # アップロード完了画面にリダイレクト
        return super().form_invalid(form)

class PlotView(generic.FormView):
    form_class = PlotForm
    template_name = 'plot.html'

# グラフ作成
def setPlt(pk):
    # 折れ線グラフを出力
    # TODO: 本当はpkを基にしてモデルからデータを取得する。
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([20, 90, 50, 30, 100, 80, 10, 60, 40, 70])
    plt.plot(x, y)


# svgへの変換
def pltToSvg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s


def get_svg(request, pk):
    setPlt(pk)  # create the plot
    svg = pltToSvg()  # convert plot to SVG
    plt.cla()  # clean up plt so it can be re-used
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response


#png画像形式に変換数関数
def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s


# html表示view
def analysis_screen(request):
    return render(request, 'analysis.html')

#画像埋め込み用view
def img_plot(request):
    # matplotを使って作図する
    template_name = 'plot.html'
    x = [1, 5, 9]
    y = [4, 6, 8]
    print("x: ", x)
    ax = plt.subplot()
    ax.scatter(x, y)
    png = plt2png()
    plt.cla()
    print("x2: ", x)
    response = HttpResponse(png, content_type='media/')
    return response