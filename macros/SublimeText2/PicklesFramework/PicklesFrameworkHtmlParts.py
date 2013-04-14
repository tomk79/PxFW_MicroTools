# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
from xml.sax.saxutils import *
import re


class PicklesFrameworkHtmlPartsParagraphCommand(sublime_plugin.TextCommand):
	def run(self, edit, action=None):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})
		selected_string = re.sub(r'(\r\n|\r|\n)', '<br />'+"\n", selected_string)
		selected_string = '<p>' + "\n" + selected_string + '</p>' + "\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)


class PicklesFrameworkHtmlPartsHeadersCommand(sublime_plugin.TextCommand):
	def run(self, edit, tagName=None):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		if not tagName:
			tagName = 'h2'

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})
		selected_string = re.sub(r'(\r\n|\r|\n)$', '', selected_string)
		selected_string = re.sub(r'(\r\n|\r|\n)', '<br />'+"\n", selected_string)
		selected_string = '<'+tagName+'>' + selected_string + '</'+tagName+'>'+"\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)

class PicklesFrameworkHtmlPartsAnchorsCommand(sublime_plugin.TextCommand):
	def run(self, edit, modName=None):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		if not modName:
			modName = ''
			classSrc = ''
		else:
			classSrc = ' class="'+modName+'"'

		# process string
		fin = '<a href="{$href}"'+classSrc+'>' + selected_string + '</a>'

		# replace selected string
		self.view.replace(edit, selection, fin)


class PicklesFrameworkHtmlPartsSpanWithClassCommand(sublime_plugin.TextCommand):
	def run(self, edit, modName=None):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		if not modName:
			modName = ''
			classSrc = ''
		else:
			classSrc = ' class="'+modName+'"'

		# process string
		fin = '<span'+classSrc+'>' + selected_string + '</span>'

		# replace selected string
		self.view.replace(edit, selection, fin)




class PicklesFrameworkHtmlPartsUlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})
		selected_string = re.sub(r'(\r\n|\r|\n)*$', '', selected_string) # trim
		selected_string = re.sub(r'^(\r\n|\r|\n)*', '', selected_string) # trim
		selected_string = re.sub(r'(\r\n|\r|\n)', '</li>'+"\n"+'	<li>', selected_string)

		fin = ''
		fin += '<ul>'+"\n"

		if not selected_string:
			fin += '	<li>{$string:listItem}</li>'+"\n"
			fin += '	<li>{$string:listItem}</li>'+"\n"
		else:
			fin += '	<li>'+selected_string+'</li>'+"\n"

		fin += '</ul>'+"\n"

		# replace selected string
		self.view.replace(edit, selection, ('%s' % fin) )




class PicklesFrameworkHtmlPartsUlNotesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})
		selected_string = re.sub(r'(\r\n|\r|\n)*$', '', selected_string) # trim
		selected_string = re.sub(r'^(\r\n|\r|\n)*', '', selected_string) # trim
		selected_string = re.sub(r'(\r\n|\r|\n)', '</li>'+"\n"+'	<li class="notes-li">* ', selected_string)

		fin = ''
		fin += '<ul class="notes">'+"\n"

		if not selected_string:
			fin += '	<li class="notes-li">* {$string:listItem}</li>'+"\n"
			fin += '	<li class="notes-li">* {$string:listItem}</li>'+"\n"
		else:
			fin += '	<li class="notes-li">* '+selected_string+'</li>'+"\n"

		fin += '</ul>'+"\n"
		# ↑[UTODO]マルチバイト文字を出力できず、こうなった。本当は、※を入れられるようにしたい。

		# replace selected string
		self.view.replace(edit, selection, ('%s' % fin) )

		# "* " を "※" に置換してください。のメッセージ。
		sublime.message_dialog('[UTODO] We can not output Multibytes strings. You TODO: replace "* " to "kome" in UTF-8.')


class PicklesFrameworkHtmlPartsUlNomarkCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})
		selected_string = re.sub(r'(\r\n|\r|\n)*$', '', selected_string) # trim
		selected_string = re.sub(r'^(\r\n|\r|\n)*', '', selected_string) # trim
		selected_string = re.sub(r'(\r\n|\r|\n)', '</li>'+"\n"+'	<li class="nomark-li">* ', selected_string)

		fin = ''
		fin += '<ul class="nomark">'+"\n"

		if not selected_string:
			fin += '	<li class="nomark-li">{$string:listItem}</li>'+"\n"
			fin += '	<li class="nomark-li">{$string:listItem}</li>'+"\n"
		else:
			fin += '	<li class="nomark-li">'+selected_string+'</li>'+"\n"

		fin += '</ul>'+"\n"

		# replace selected string
		self.view.replace(edit, selection, ('%s' % fin) )





class PicklesFrameworkHtmlPartsDlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})

		fin = ''
		fin += '<dl>'+"\n"
		fin += '	<dt>{$string}</dt>'+"\n"

		if not selected_string:
			fin += '		<dd>{$string}</dd>'+"\n"
		else:
			fin += '		<dd>'+selected_string+'</dd>'+"\n"

		fin += '	<dt>{$string}</dt>'+"\n"
		fin += '		<dd>{$string}</dd>'+"\n"
		fin += '	<dt>{$string}</dt>'+"\n"
		fin += '		<dd>{$string}</dd>'+"\n"
		fin += '</dl>'+"\n"

		# replace selected string
		self.view.replace(edit, selection, ('%s' % fin) )




class PicklesFrameworkHtmlPartsDlNotesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})

		fin = ''
		fin += '<dl class="notes">'+"\n"
		fin += '	<dt class="notes-dt">{$strong}</dt>'+"\n"

		if not selected_string:
			fin += '		<dd class="notes-dd">{$strong}</dd>'+"\n"
		else:
			fin += '		<dd class="notes-dd">'+selected_string+'</dd>'+"\n"

		fin += '	<dt class="notes-dt">{$strong}</dt>'+"\n"
		fin += '		<dd class="notes-dd">{$strong}</dd>'+"\n"
		fin += '	<dt class="notes-dt">{$strong}</dt>'+"\n"
		fin += '		<dd class="notes-dd">{$strong}</dd>'+"\n"
		fin += '</dl>'+"\n"

		# replace selected string
		self.view.replace(edit, selection, ('%s' % fin) )





class PicklesFrameworkHtmlPartsDateListCommand(sublime_plugin.TextCommand):
	# view.run_command('pickles_framework_html_parts_date_list')
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="date_list">'+"\n"
		fin += '	<table>'+"\n"
		fin += '		<thead>'+"\n"
		fin += '			<tr>'+"\n"
		fin += '				<th>{$text:headerOfDate}</th>'+"\n"
		fin += '				<th class="date_list-flag">{$text:headerOfFlags}</th>'+"\n"
		fin += '				<th>{$text:headerOfContents}</th>'+"\n"
		fin += '			</tr>'+"\n"
		fin += '		</thead>'+"\n"
		fin += '		<tbody>'+"\n"
		fin += '			<tr>'+"\n"
		fin += '				<th>{$text:date}</th>'+"\n"
		fin += '				<td class="date_list-flag">{$html:flags}</td>'+"\n"
		fin += '				<td><a href="{$href}">{$text:linkLabel}</a></td>'+"\n"
		fin += '			</tr>'+"\n"
		fin += '		</tbody>'+"\n"
		fin += '	</table>'+"\n"
		fin += '</div><!-- /.date_list -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)






class PicklesFrameworkHtmlPartsImgrepCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = ''
		selected_string += '<?php ob_start(); ?>'+"\n"
		selected_string += '<style type="text/css">'+"\n"
		selected_string += '	.cont_{$string:yourClassName}{'+"\n"
		selected_string += '		width:{$string:yourImageWidth};'+"\n"
		selected_string += '		height:{$string:yourImageHeight};'+"\n"
		selected_string += '	}'+"\n"
		selected_string += '	.cont_sample .imgrep-panel{'+"\n"
		selected_string += '		background-image:url("{$string:yourImagePath}");'+"\n"
		selected_string += '	}'+"\n"
		selected_string += '</style>'+"\n"
		selected_string += '<?php $px->theme()->send_content( ob_get_clean(), \'head\' ); ?>'+"\n"
		selected_string += '<a href="{$string:href}" class="imgrep cont_{$string:yourClassName}">{$string:linklabel}<span class="imgrep-panel"></span></a>'+"\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)


class PicklesFrameworkHtmlPartsTableDefCommand(sublime_plugin.TextCommand):
	# view.run_command('pickles_framework_html_parts_table_def')
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = ''
		selected_string += '<table class="def" style="width:100%;">'+"\n"
		selected_string += '	<thead>'+"\n"
		selected_string += '		<tr>'+"\n"
		selected_string += '			<th>{$string}</th>'+"\n"
		selected_string += '			<td>{$string}</td>'+"\n"
		selected_string += '			<td>{$string}</td>'+"\n"
		selected_string += '		</tr>'+"\n"
		selected_string += '	</thead>'+"\n"
		selected_string += '	<tfoot>'+"\n"
		selected_string += '		<tr>'+"\n"
		selected_string += '			<th>{$string}</th>'+"\n"
		selected_string += '			<td>{$string}</td>'+"\n"
		selected_string += '			<td>{$string}</td>'+"\n"
		selected_string += '		</tr>'+"\n"
		selected_string += '	</tfoot>'+"\n"
		selected_string += '	<tbody>'+"\n"
		selected_string += '		<tr>'+"\n"
		selected_string += '			<th>{$string}</th>'+"\n"
		selected_string += '			<td>{$string}</td>'+"\n"
		selected_string += '			<td>{$string}</td>'+"\n"
		selected_string += '		</tr>'+"\n"
		selected_string += '		<tr>'+"\n"
		selected_string += '			<th>{$string}</th>'+"\n"
		selected_string += '			<td>{$string}</td>'+"\n"
		selected_string += '			<td>{$string}</td>'+"\n"
		selected_string += '		</tr>'+"\n"
		selected_string += '	</tbody>'+"\n"
		selected_string += '</table><!-- /table.def -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)



class PicklesFrameworkHtmlPartsAuralCommand(sublime_plugin.TextCommand):
	# view.run_command('pickles_framework_html_parts_aural')
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="aural">'+"\n"
		fin += selected_string+"\n"
		fin += '</div><!-- /.aural -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)




class PicklesFrameworkHtmlPartsCode1Command(sublime_plugin.TextCommand):
	# view.run_command('pickles_framework_html_parts_code1')
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})
		selected_string = '<div class="unit">'+"\n"+'	<div class="code"><textarea readonly="readonly">' + selected_string + '</textarea></div>'+"\n"+'</div>'+"\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)


class PicklesFrameworkHtmlPartsCode2Command(sublime_plugin.TextCommand):
	# view.run_command('pickles_framework_html_parts_code2')
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = escape(selected_string,{'"':'&quot;'})
		selected_string = '<div class="unit">'+"\n"+'	<div class="code"><pre><code>' + selected_string + '</code></pre></div>'+"\n"+'</div>'+"\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)



class PicklesFrameworkHtmlPartsTopicBoxCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="topic_box">'+"\n"
		fin += '	<p class="topic_box-heading">{$text}</p>'+"\n"

		if selected_string:
			fin += selected_string+"\n"
		else:
			fin += '	<p>{$text}</p>'+"\n"
			fin += '	{$partsModules}'+"\n"

		fin += '</div><!-- /.topic_box -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)



class PicklesFrameworkHtmlPartsAsideBoxCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="aside_box">'+"\n"
		fin += '	<p class="aside_box-heading">{$text}</p>'+"\n"

		if selected_string:
			fin += selected_string+"\n"
		else:
			fin += '	<p>{$text}</p>'+"\n"
			fin += '	{$partsModules}'+"\n"

		fin += '</div><!-- /.aside_box -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)



class PicklesFrameworkHtmlPartsAttentionBoxCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="attention_box">'+"\n"
		fin += '	<p class="attention_box-heading">{$text}</p>'+"\n"

		if selected_string:
			fin += selected_string+"\n"
		else:
			fin += '	<p>{$text}</p>'+"\n"
			fin += '	{$partsModules}'+"\n"

		fin += '</div><!-- /.attention_box -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)





