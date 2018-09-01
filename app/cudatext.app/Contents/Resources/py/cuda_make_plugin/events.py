EVENTS = [
    'on_caret',
    'on_change',
    'on_change_slow',
    'on_click',
    'on_click_dbl',
    'on_click_gap',
    'on_click_gutter',
    'on_close',
    'on_close_pre',
    'on_complete',
    'on_console',
    'on_console_nav',
    'on_console_print',
    'on_exit',
    'on_focus',
    'on_func_hint',
    'on_goto_def',
    'on_hotspot',
    'on_insert',
    'on_key',
    'on_key_up',
    'on_lexer',
    'on_macro',
    'on_mouse_stop',
    'on_open',
    'on_open_none',
    'on_open_pre',
    'on_output_nav',
    'on_paste',
    'on_save',
    'on_save_pre',
    'on_scroll',
    'on_snippet',
    'on_start',
    'on_state',
    'on_tab_change',
    'on_tab_move',
    'on_tab_switch',
  ]

EVENTS_ADD_PARAMS = {
  'on_key': 'key, state',
  'on_key_up': 'key, state',
  'on_insert': 'text',
  'on_click': 'state',
  'on_click_dbl': 'state',
  'on_click_gap': 'state, nline, ntag, size_x, size_y, pos_x, pos_y',
  'on_click_gutter': 'state, nline, nband',
  'on_console': 'text',
  'on_console_nav': 'text',
  'on_console_print': 'text',
  'on_hotspot': 'entered, hotspot_index',
  'on_output_nav': 'text, tag',
  'on_macro': 'text',
  'on_mouse_stop': 'x, y',
  'on_open_pre': 'filename',
  'on_paste': 'keep_caret, select_then',
  'on_snippet': 'snippet_id, snippet_text',
  'on_state': 'state',
  'on_tab_switch': 'next, state',
  }
