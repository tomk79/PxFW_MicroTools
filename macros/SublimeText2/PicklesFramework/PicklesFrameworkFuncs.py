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
		fin += '<?php $px->theme()->send_content( ob_get_clean(), \'head\' ); ?>'+"\n"
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


class PicklesFrameworkFuncsStandardFormUiCommand(sublime_plugin.TextCommand):
	def run(self, edit, tagName):
		# getting selected string
		selection = self.view.sel()[0]
		selected_string = self.view.substr(selection)
		selected_string = re.sub(r'(\r\n|\r|\n)', '', selected_string)

		if selected_string == '':
			selected_string = '{$form_name}'

		# process string
		fin = ''

		fin += '	/**'+"\n"
		fin += '	 * '+selected_string+''+"\n"
		fin += '	 */'+"\n"
		fin += '	private function start_'+selected_string+'(){'+"\n"
		fin += '		$error = $this->check_'+selected_string+'_check();'+"\n"
		fin += '		if( $this->px->req()->get_param(\'mode\') == \'thanks\' ){'+"\n"
		fin += '			return	$this->page_'+selected_string+'_thanks();'+"\n"
		fin += '		}elseif( $this->px->req()->get_param(\'mode\') == \'confirm\' && !count( $error ) ){'+"\n"
		fin += '			return	$this->page_'+selected_string+'_confirm();'+"\n"
		fin += '		}elseif( $this->px->req()->get_param(\'mode\') == \'execute\' && !count( $error ) ){'+"\n"
		fin += '			return	$this->execute_'+selected_string+'_execute();'+"\n"
		fin += '		}elseif( !strlen( $this->px->req()->get_param(\'mode\') ) ){'+"\n"
		fin += '			$error = array();'+"\n"
		fin += ''+"\n"
		fin += '			// $this->px->req()->set_param( \'input_value\' , $this->cmd[1] );'+"\n"
		fin += '		}'+"\n"
		fin += '		return	$this->page_'+selected_string+'_input( $error );'+"\n"
		fin += '	}'+"\n"
		fin += '	/**'+"\n"
		fin += '	 * '+selected_string+'：入力'+"\n"
		fin += '	 */'+"\n"
		fin += '	private function page_'+selected_string+'_input( $error ){'+"\n"
		fin += '		$RTN = \'\'."\\n";'+"\n"
		fin += ''+"\n"
		fin += '		$RTN .= \'<p>\'."\\n";'+"\n"
		fin += '		$RTN .= \'	必要な情報を入力して、「確認する」ボタンをクリックしてください。<span class="must">必須</span>印の項目は必ず入力してください。<br />\'."\\n";'+"\n"
		fin += '		$RTN .= \'</p>\'."\\n";'+"\n"
		fin += '		if( is_array( $error ) && count( $error ) ){'+"\n"
		fin += '			$RTN .= \'<p class="error">\'."\\n";'+"\n"
		fin += '			$RTN .= \'	入力エラーを検出しました。画面の指示に従って修正してください。<br />\'."\\n";'+"\n"
		fin += '			$RTN .= \'</p>\'."\\n";'+"\n"
		fin += '		}'+"\n"
		fin += '		$RTN .= \'<form action="\'.t::h( \'?\' ).\'" method="post" class="inline">\'."\\n";'+"\n"
		fin += '		$RTN .= \'<table style="width:100%;" class="form_elements">\'."\\n";'+"\n"
		fin += '		$RTN .= \'	<tr>\'."\\n";'+"\n"
		fin += '		$RTN .= \'		<th style="width:30%;"><div>input_value <span class="must">必須</span></div></th>\'."\\n";'+"\n"
		fin += '		$RTN .= \'		<td style="width:70%;">\'."\\n";'+"\n"
		fin += '		$RTN .= \'			<div><input type="text" name="input_value" value="\'.t::h( $this->px->req()->get_param(\'input_value\') ).\'" style="width:80%;" /></div>\'."\\n";'+"\n"
		fin += '		if( strlen( $error[\'input_value\'] ) ){'+"\n"
		fin += '			$RTN .= \'			<div class="error">\'.$error[\'input_value\'].\'</div>\'."\\n";'+"\n"
		fin += '		}'+"\n"
		fin += '		$RTN .= \'		</td>\'."\\n";'+"\n"
		fin += '		$RTN .= \'	</tr>\'."\\n";'+"\n"
		fin += ''+"\n"
		fin += '		$RTN .= \'</table>\'."\\n";'+"\n"
		fin += '		$RTN .= \'	<div class="center"><input type="submit" value="確認する" /></div>\'."\\n";'+"\n"
		fin += '		$RTN .= \'	<input type="hidden" name="mode" value="confirm" />\'."\\n";'+"\n"
		fin += '		$RTN .= \'</form>\'."\\n";'+"\n"
		fin += '		return	$RTN;'+"\n"
		fin += '	}'+"\n"
		fin += '	/**'+"\n"
		fin += '	 * '+selected_string+'：確認'+"\n"
		fin += '	 */'+"\n"
		fin += '	private function page_'+selected_string+'_confirm(){'+"\n"
		fin += '		$RTN = \'\'."\\n";'+"\n"
		fin += '		$HIDDEN = \'\'."\\n";'+"\n"
		fin += ''+"\n"
		fin += '		$RTN .= \'<p>\'."\\n";'+"\n"
		fin += '		$RTN .= \'	入力した内容を確認してください。<br />\'."\\n";'+"\n"
		fin += '		$RTN .= \'</p>\'."\\n";'+"\n"
		fin += ''+"\n"
		fin += '		$RTN .= \'<table style="width:100%;" class="form_elements">\'."\\n";'+"\n"
		fin += '		$RTN .= \'	<tr>\'."\\n";'+"\n"
		fin += '		$RTN .= \'		<th style="width:30%;"><div>input_value</div></th>\'."\\n";'+"\n"
		fin += '		$RTN .= \'		<td style="width:70%;">\'."\\n";'+"\n"
		fin += '		$RTN .= \'			<div>\'.t::h( $this->px->req()->get_param(\'input_value\') ).\'</div>\'."\\n";'+"\n"
		fin += '		$HIDDEN .= \'<input type="hidden" name="input_value" value="\'.t::h( $this->px->req()->get_param(\'input_value\') ).\'" />\';'+"\n"
		fin += '		$RTN .= \'		</td>\'."\\n";'+"\n"
		fin += '		$RTN .= \'	</tr>\'."\\n";'+"\n"
		fin += '		$RTN .= \'</table>\'."\\n";'+"\n"
		fin += ''+"\n"
		fin += '		$RTN .= \'<div class="unit">\'."\\n";'+"\n"
		fin += '		$RTN .= \'<div class="center">\'."\\n";'+"\n"
		fin += '		$RTN .= \'<form action="\'.t::h( \'?\' ).\'" method="post" class="inline">\'."\\n";'+"\n"
		fin += '		$RTN .= \'	<input type="hidden" name="mode" value="execute" />\'."\\n";'+"\n"
		fin += '		$RTN .= $HIDDEN;'+"\n"
		fin += '		$RTN .= \'	\'.\'\'."\\n";'+"\n"
		fin += '		$RTN .= \'	<input type="submit" value="送信する" />\'."\\n";'+"\n"
		fin += '		$RTN .= \'</form>\'."\\n";'+"\n"
		fin += '		$RTN .= \'<form action="\'.t::h( \'?\' ).\'" method="post" class="inline">\'."\\n";'+"\n"
		fin += '		$RTN .= \'	<input type="hidden" name="mode" value="input" />\'."\\n";'+"\n"
		fin += '		$RTN .= $HIDDEN;'+"\n"
		fin += '		$RTN .= \'	\'.\'\'."\\n";'+"\n"
		fin += '		$RTN .= \'	<input type="submit" value="訂正する" />\'."\\n";'+"\n"
		fin += '		$RTN .= \'</form>\'."\\n";'+"\n"
		fin += '		$RTN .= \'</div>\'."\\n";'+"\n"
		fin += '		$RTN .= \'</div>\'."\\n";'+"\n"
		fin += '		$RTN .= \'<hr />\'."\\n";'+"\n"
		fin += '		$RTN .= \'<div class="unit">\'."\\n";'+"\n"
		fin += '		$RTN .= \'<form action="\'.t::h( \'?\' ).\'" method="post" class="inline">\'."\\n";'+"\n"
		fin += '		$RTN .= \'	<div class="center"><input type="submit" value="キャンセル" /></div>\'."\\n";'+"\n"
		fin += '		$RTN .= \'</form>\'."\\n";'+"\n"
		fin += '		$RTN .= \'</div>\'."\\n";'+"\n"
		fin += '		return	$RTN;'+"\n"
		fin += '	}'+"\n"
		fin += '	/**'+"\n"
		fin += '	 * '+selected_string+'：チェック'+"\n"
		fin += '	 */'+"\n"
		fin += '	private function check_'+selected_string+'_check(){'+"\n"
		fin += '		$RTN = array();'+"\n"
		fin += '		if( !strlen( $this->px->req()->get_param(\'input_value\') ) ){'+"\n"
		fin += '			$RTN[\'input_value\'] = \'input_valueは必須項目です。\';'+"\n"
		fin += '		}elseif( preg_match( \'/\\r\\n|\\r|\\n/\' , $this->px->req()->get_param(\'input_value\') ) ){'+"\n"
		fin += '			$RTN[\'input_value\'] = \'input_valueに改行を含めることはできません。\';'+"\n"
		fin += '		}elseif( strlen( $this->px->req()->get_param(\'input_value\') ) > 256 ){'+"\n"
		fin += '			$RTN[\'input_value\'] = \'input_valueが長すぎます。\';'+"\n"
		fin += '		}'+"\n"
		fin += ''+"\n"
		fin += '		return	$RTN;'+"\n"
		fin += '	}'+"\n"
		fin += '	/**'+"\n"
		fin += '	 * '+selected_string+'：実行'+"\n"
		fin += '	 */'+"\n"
		fin += '	private function execute_'+selected_string+'_execute(){'+"\n"
		fin += ''+"\n"
		fin += '		// [UTODO] ここに実行する処理を記述します。'+"\n"
		fin += ''+"\n"
		fin += '		return $this->px->redirect( \'?mode=thanks\' );'+"\n"
		fin += '	}'+"\n"
		fin += '	/**'+"\n"
		fin += '	 * '+selected_string+'：完了'+"\n"
		fin += '	 */'+"\n"
		fin += '	private function page_'+selected_string+'_thanks(){'+"\n"
		fin += '		$RTN = \'\'."\\n";'+"\n"
		fin += '		$RTN .= \'<p>完了しました。</p>\'."\\n";'+"\n"
		fin += '		$RTN .= \'<form action="\'.t::h( \'?\' ).\'" method="post" class="inline">\'."\\n";'+"\n"
		fin += '		$RTN .= \'	<p><input type="submit" value="戻る" /></p>\'."\\n";'+"\n"
		fin += '		$RTN .= \'</form>\'."\\n";'+"\n"
		fin += '		return	$RTN;'+"\n"
		fin += '	}'+"\n"
		fin += ''+"\n"

		# replace selected string
		self.view.replace(edit, selection, fin)
