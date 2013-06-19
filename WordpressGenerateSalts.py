import sublime, sublime_plugin, urllib.request

# Extends TextCommand so that run() receives a View to modify.
class WordpressGenerateSaltsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for cursor in self.view.sel():
            req = urllib.request.Request('https://api.wordpress.org/secret-key/1.1/salt/')
            response = urllib.request.urlopen(req)
            salts = response.read()
            salts = salts.decode("utf-8")
            self.view.insert(edit, cursor.begin(), salts )
