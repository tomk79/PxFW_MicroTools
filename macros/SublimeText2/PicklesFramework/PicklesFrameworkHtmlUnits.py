# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
from xml.sax.saxutils import *


class PicklesFrameworkHtmlUnitsUnitCommand(sublime_plugin.TextCommand):
	#  view.run_command('pickles_framework_html_units_unit')
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="unit">'+"\n"
		if selected_string:
			fin += selected_string+"\n"
		else:
			fin += '	{$partsModules}'+"\n"
		fin += '</div><!-- /.unit -->'+"\n"
		fin += ''+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)




class PicklesFrameworkHtmlUnitsColsCol2Command(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = ''
		selected_string += '<div class="cols unit">'+"\n"
		selected_string += '	<div class="cols-col cols-1of2"><div class="cols-pad">'+"\n"
		selected_string += '		{$partsModules}'+"\n"
		selected_string += '	</div></div>'+"\n"
		selected_string += '	<div class="cols-col cols-1of2 cols-last"><div class="cols-pad">'+"\n"
		selected_string += '		{$partsModules}'+"\n"
		selected_string += '	</div></div>'+"\n"
		selected_string += '</div><!-- / .cols -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)



class PicklesFrameworkHtmlUnitsColsCol3Command(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = ''
		selected_string += '<div class="cols unit">'+"\n"
		selected_string += '	<div class="cols-col cols-1of3"><div class="cols-pad">'+"\n"
		selected_string += '		{$partsModules}'+"\n"
		selected_string += '	</div></div>'+"\n"
		selected_string += '	<div class="cols-col cols-1of3"><div class="cols-pad">'+"\n"
		selected_string += '		{$partsModules}'+"\n"
		selected_string += '	</div></div>'+"\n"
		selected_string += '	<div class="cols-col cols-1of3 cols-last"><div class="cols-pad">'+"\n"
		selected_string += '		{$partsModules}'+"\n"
		selected_string += '	</div></div>'+"\n"
		selected_string += '</div><!-- / .cols -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)


class PicklesFrameworkHtmlUnitsColsCol4Command(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		selected_string = ''
		selected_string += '<div class="cols unit">'+"\n"
		selected_string += '	<div class="cols-col cols-1of4"><div class="cols-pad">'+"\n"
		selected_string += '		{$partsModules}'+"\n"
		selected_string += '	</div></div>'+"\n"
		selected_string += '	<div class="cols-col cols-1of4"><div class="cols-pad">'+"\n"
		selected_string += '		{$partsModules}'+"\n"
		selected_string += '	</div></div>'+"\n"
		selected_string += '	<div class="cols-col cols-1of4"><div class="cols-pad">'+"\n"
		selected_string += '		{$partsModules}'+"\n"
		selected_string += '	</div></div>'+"\n"
		selected_string += '	<div class="cols-col cols-1of4 cols-last"><div class="cols-pad">'+"\n"
		selected_string += '		{$partsModules}'+"\n"
		selected_string += '	</div></div>'+"\n"
		selected_string += '</div><!-- / .cols -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)



class PicklesFrameworkHtmlUnitsFloatMediaCommand(sublime_plugin.TextCommand):
	def run(self, edit, lr=None, width=None):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		if not lr:
			lr = "r"
		if not width:
			lr = "1of2"

		# process string
		selected_string = ''
		selected_string += '<div class="unit float_media">'+"\n"
		selected_string += '	<div class="float_media-'+lr+width+'">'+"\n"
		selected_string += '		<div class="float_media-image"><img src="{$imagePath}" alt="" /></div>'+"\n"
		selected_string += '		<p class="float_media-caption">{$text:captionText}</p>'+"\n"
		selected_string += '	</div>'+"\n"
		selected_string += '	<div class="float_media-body">'+"\n"
		selected_string += '		{$partsModules}'+"\n"
		selected_string += '	</div>'+"\n"
		selected_string += '</div><!-- /.float_media -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, selected_string)





class PicklesFrameworkHtmlUnitsThumbListCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="unit thumb_list">'+"\n"
		fin += '	<ul>'+"\n"
		fin += '		<li><div class="thumb_list-pad"><a href="{$href}"><img src="{$imagePath}" alt="" /><span class="thumb_list-caption">{$text:ThumbnailLabel}</span></a></div></li>'+"\n"
		fin += '		<li><div class="thumb_list-pad"><a href="{$href}"><img src="{$imagePath}" alt="" /><span class="thumb_list-caption">{$text:ThumbnailLabel}</span></a></div></li>'+"\n"
		fin += '		<li><div class="thumb_list-pad"><a href="{$href}"><img src="{$imagePath}" alt="" /><span class="thumb_list-caption">{$text:ThumbnailLabel}</span></a></div></li>'+"\n"
		fin += '		<li><div class="thumb_list-pad"><a href="{$href}"><img src="{$imagePath}" alt="" /><span class="thumb_list-caption">{$text:ThumbnailLabel}</span></a></div></li>'+"\n"
		fin += '		<li><div class="thumb_list-pad"><a href="{$href}"><img src="{$imagePath}" alt="" /><span class="thumb_list-caption">{$text:ThumbnailLabel}</span></a></div></li>'+"\n"
		fin += '		<li><div class="thumb_list-pad"><a href="{$href}"><img src="{$imagePath}" alt="" /><span class="thumb_list-caption">{$text:ThumbnailLabel}</span></a></div></li>'+"\n"
		fin += '		<li><div class="thumb_list-pad"><img src="{$imagePath}" alt="" /><span class="thumb_list-caption">{$text:ThumbnailLabel}</span></div></li>'+"\n"
		fin += '	</ul>'+"\n"
		fin += '</div><!-- /.thumb_list -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)



class PicklesFrameworkHtmlUnitsPagerCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="unit pager">'+"\n"
		fin += '	<ul>'+"\n"
		fin += '		<li class="pager-first"><span>&lt;&lt;first</span></li>'+"\n"
		fin += '		<li class="pager-prev"><span>&lt;prev</span></li>'+"\n"
		fin += '		<li><span class="current">1</span></li>'+"\n"
		fin += '		<li><a href="#">2</a></li>'+"\n"
		fin += '		<li><a href="#">3</a></li>'+"\n"
		fin += '		<li><a href="#">4</a></li>'+"\n"
		fin += '		<li><a href="#">5</a></li>'+"\n"
		fin += '		<li><a href="#">6</a></li>'+"\n"
		fin += '		<li><a href="#">7</a></li>'+"\n"
		fin += '		<li class="pager-next"><a href="#">next&gt;</a></li>'+"\n"
		fin += '		<li class="pager-last"><a href="#">last&gt;&gt;</a></li>'+"\n"
		fin += '	</ul>'+"\n"
		fin += '</div><!-- /.pager -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)


class PicklesFrameworkHtmlUnitsForm_buttonsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="unit form_buttons">'+"\n"
		fin += '	<ul>'+"\n"
		fin += '		<li class="form_buttons-submit"><input type="submit" name="" value="{$string:submitButtonLabel}" /></li>'+"\n"
		fin += '	</ul>'+"\n"
		fin += '</div><!-- /.form_buttons -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)




class PicklesFrameworkHtmlUnitsForm_buttonsOkCancelCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="unit form_buttons">'+"\n"
		fin += '	<ul>'+"\n"
		fin += '		<li class="form_buttons-submit"><input type="submit" name="" value="{$string:submitButtonLabel}" /></li>'+"\n"
		fin += '		<li class="form_buttons-revise"><input type="submit" name="" value="{$string:reviseButtonLabel}" /></li>'+"\n"
		fin += '	</ul>'+"\n"
		fin += '</div><!-- /.form_buttons -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)




class PicklesFrameworkHtmlUnitsForm_buttonsCancelCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="unit form_buttons">'+"\n"
		fin += '	<ul>'+"\n"
		fin += '		<li class="form_buttons-cancel"><input type="submit" name="" value="{$string:cancelButtonLabel}" /></li>'+"\n"
		fin += '	</ul>'+"\n"
		fin += '</div><!-- /.form_buttons -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)




class PicklesFrameworkHtmlUnitsForm_error_boxCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)

		# process string
		fin = ''
		fin += '<div class="unit form_error_box">'+"\n"
		fin += '	<p>{$string:text}</p>'+"\n"
		fin += '	<ul>'+"\n"
		fin += '		<li><a href="#{$string:anchorId}">{$string:text}</a></li>'+"\n"
		fin += '		<li>{$string:text}</li>'+"\n"
		fin += '	</ul>'+"\n"
		fin += '</div><!-- /.form_error_box -->'+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)




