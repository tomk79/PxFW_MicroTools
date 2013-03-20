# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
from xml.sax.saxutils import *
import re


class PicklesFrameworkFuncsHtmlspecialcharsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})

		# replace selected string
		self.view.replace(edit, selection, selected_string)


class PicklesFrameworkFuncsText2htmlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})
		selected_string = re.sub(r'(\r\n|\r|\n)', '<br />'+"\n", selected_string)

		# replace selected string
		self.view.replace(edit, selection, selected_string)



class PicklesFrameworkFuncsString2varCommand(sublime_plugin.TextCommand):
	def run(self, edit, lang=None):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = re.sub(r'(\\)', '\\\\\\\\', selected_string)
		selected_string = re.sub(r'(\')', '\\\'', selected_string)
		if lang == 'php':
			selected_string = re.sub(r'(\r\n|\r|\n)', '\'."\\\\n";'+"\n"+'	$fin .= \'', selected_string)
			selected_string = '	$fin .= \'' + selected_string + '\'."\\n";'+"\n"
		elif lang == 'js':
			selected_string = re.sub(r'(\r\n|\r|\n)', '\'+"\\\\n";'+"\n"+'	fin += \'', selected_string)
			selected_string = '	fin += \'' + selected_string + '\'+"\\n";'+"\n"
		elif lang == 'phython':
			selected_string = re.sub(r'(\r\n|\r|\n)', '\'+"\\\\n"'+"\n"+'	fin += \'', selected_string)
			selected_string = '	fin += \'' + selected_string + '\'+"\\n"'+"\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)





