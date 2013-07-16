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

class PicklesFrameworkFuncsInsertAutoindexCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]

		# process string
		fin = '<?php print( $px->theme()->autoindex() ); ?>'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)


class PicklesFrameworkFuncsInsertSendContentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += "\n"
		fin += '<?php ob_start(); ?>'+"\n"
		fin += "\n"
		fin += selected_string +"\n"
		fin += "\n"
		fin += '<?php print( $px->theme()->send_content( ob_get_clean(), \'head\' ) ); ?>'+"\n"
		fin += "\n"

		# replace selected string
		self.view.replace(edit, selection, fin)



class PicklesFrameworkFuncsWrapInlineTagCommand(sublime_plugin.TextCommand):
	def run(self, edit, tagName):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = '<'+tagName+'>' + selected_string + '</'+tagName+'>'

		# replace selected string
		self.view.replace(edit, selection, selected_string)



class PicklesFrameworkFuncsWrapBlockTagCommand(sublime_plugin.TextCommand):
	def run(self, edit, tagName):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)
		selected_string = re.sub(r'(\r\n|\r|\n)$', '', selected_string)

		# process string
		selected_string = '<'+tagName+'>' + "\n" + selected_string + "\n" + '</'+tagName+'>' + "\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)





