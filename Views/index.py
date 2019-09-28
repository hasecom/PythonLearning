from Views import view
# __init__:親クラスの共通部分を合体させます。
# _exit   :親クラスの共通部分を合体させます。
# view    :描画されるHTMLを返します。
# content :HTMLの細かい描画を行います。

class Index(view.View):
    def __init__(self):
        self.obj += super().enter()

    def _exit(self):
        self.obj += super().exit()

    def view(self,obj):
        self.obj += "{0}".format(obj)
        self._exit()
        return self.obj

