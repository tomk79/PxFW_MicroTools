import sublime
import sublime_plugin
from xml.sax.saxutils import *


class PxCommand(sublime_plugin.TextCommand):
	#  view.run_command('px')
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})
		selected_string = '<div class="unit">'+"\n"+'	<div class="code"><textarea readonly="readonly">' + selected_string + '</textarea></div>'+"\n"+'</div>'

		# replace selected string
		self.view.replace(edit, selection, selected_string)


