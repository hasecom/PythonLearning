#viewの親クラス (viewの共通部分を描画します。)
class View:
    obj = ""
    en = "<div class='app'>"
    ex = "</div>"
    def enter(self):
        return self.en
    def exit(self):
        return self.ex