#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x9cc94f9e

# Compiled with Coconut version 3.1.1-post_dev2

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.1-post_dev2', '', True)
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:  # type: ignore
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):  # type: ignore
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")  # type: ignore
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():  # type: ignore
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):  # type: ignore
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)  # type: ignore
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):  # type: ignore
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and str('__coconut_cache__') in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != str('__coconut_cache__'):
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

import inspect  #1 (line in Coconut source)
import traceback  #2 (line in Coconut source)
try:  #3 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #3 (line in Coconut source)
except _coconut.NameError:  #3 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #3 (line in Coconut source)
sys = _coconut_sys  #3 (line in Coconut source)
if sys.version_info >= (3,):  #3 (line in Coconut source)
    import builtins  #3 (line in Coconut source)
else:  #3 (line in Coconut source)
    import __builtin__ as builtins  #3 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #3 (line in Coconut source)
    sys = _coconut_sys_0  #3 (line in Coconut source)
from collections import defaultdict  #4 (line in Coconut source)


ALL_DEBUG_CONTEXT = defaultdict(list)  #7 (line in Coconut source)


class DebugContext(_coconut.typing.NamedTuple("DebugContext", [("name", 'str'), ("frame_info", '_coconut.typing.Any'), ("source_lines", '_coconut.typing.Sequence[str]'), ("extra_info", 'dict[str, str]')]), _coconut.object):  #10 (line in Coconut source)
    """Collection of information gathered about a debug event."""  #16 (line in Coconut source)
    __slots__ = ()  #17 (line in Coconut source)
    _coconut_is_data = True  #17 (line in Coconut source)
    __match_args__ = ('name', 'frame_info', 'source_lines', 'extra_info')  #17 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #17 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #17 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #17 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #17 (line in Coconut source)
    def __eq__(self, other):  #17 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #17 (line in Coconut source)
    def __hash__(self):  #17 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #17 (line in Coconut source)
    def __init__(self, *args, **kwargs):  #17 (line in Coconut source)
        ALL_DEBUG_CONTEXT[self.filename].append(self)  #18 (line in Coconut source)

    @property  #19 (line in Coconut source)
    def filename(self):  #20 (line in Coconut source)
        return self.frame_info.filename  #20 (line in Coconut source)

    @property  #21 (line in Coconut source)
    def lineno(self):  #22 (line in Coconut source)
        return self.frame_info.lineno  #22 (line in Coconut source)

    @property  #23 (line in Coconut source)
    def function(self):  #24 (line in Coconut source)
        return self.frame_info.function  #24 (line in Coconut source)

    @property  #25 (line in Coconut source)
    def context_lines(self):  #26 (line in Coconut source)
        return self.frame_info.code_context  #26 (line in Coconut source)

    @property  #27 (line in Coconut source)
    def context_index(self):  #28 (line in Coconut source)
        return self.frame_info.index  #28 (line in Coconut source)

    @property  #29 (line in Coconut source)
    def raw_source(self):  #30 (line in Coconut source)
        return "\n".join(self.source_lines)  #30 (line in Coconut source)



_coconut_call_set_names(DebugContext)  #33 (line in Coconut source)
IGNORED_VARS = set(dir(builtins)) | _coconut.set(("claude_here",))  #33 (line in Coconut source)


def format_vars(vardict):  #36 (line in Coconut source)
    return (repr)(_coconut.dict(((name), (val)) for name, val in vardict.items() if not name.startswith("__") and name not in IGNORED_VARS))  #36 (line in Coconut source)



def collect_stack_info(stack_level=1):  #42 (line in Coconut source)
    """Collect information about the callee site for sending to Claude."""  #43 (line in Coconut source)
    cur_frame = inspect.currentframe()  #44 (line in Coconut source)
    outer_frame = reduce(lambda frame, _: frame.f_back, range(stack_level), cur_frame)  #45 (line in Coconut source)

    frame_info = inspect.getframeinfo(outer_frame)  #51 (line in Coconut source)
    try:  #52 (line in Coconut source)
        source_lines, source_lineno = inspect.getsourcelines(outer_frame)  #53 (line in Coconut source)
    except OSError:  #54 (line in Coconut source)
        source_lines = []  #55 (line in Coconut source)

    return DebugContext(name="breakpoint", frame_info=frame_info, source_lines=source_lines, extra_info=_coconut.dict((("locals", format_vars(outer_frame.f_locals)), ("globals", format_vars(outer_frame.f_globals)))))  #57 (line in Coconut source)



def filter_traceback(orig_tb):  #68 (line in Coconut source)
    """Filter out traceback frames from claude_here."""  #69 (line in Coconut source)
    new_tb_top = orig_tb  #70 (line in Coconut source)
    while new_tb_top is not None and new_tb_top.tb_frame.f_globals.get("__package__") == "claude_here":  #71 (line in Coconut source)
# print({k:v for k,v in new_tb_top.tb_frame.f_globals.items() if k.startswith("__")})
        new_tb_top = new_tb_top.tb_next  #73 (line in Coconut source)

    if new_tb_top is not None:  #75 (line in Coconut source)
        tb_cursor_plus_1 = new_tb_top  #76 (line in Coconut source)
        tb_cursor = tb_cursor_plus_1.tb_next  #77 (line in Coconut source)
        while tb_cursor is not None:  #78 (line in Coconut source)
            tb_cursor_minus_1 = tb_cursor.tb_next  #79 (line in Coconut source)
# print({k:v for k,v in tb_cursor.tb_frame.f_globals.items() if k.startswith("__")})
            if tb_cursor.tb_frame.f_globals.get("__package__") == "claude_here":  #81 (line in Coconut source)
                tb_cursor_plus_1.tb_next = tb_cursor_minus_1  #82 (line in Coconut source)
                tb_cursor_plus_1, tb_cursor = (tb_cursor_plus_1, tb_cursor_minus_1)  #83 (line in Coconut source)
            else:  #87 (line in Coconut source)
                tb_cursor_plus_1, tb_cursor = (tb_cursor, tb_cursor_minus_1)  #88 (line in Coconut source)

    return new_tb_top  #93 (line in Coconut source)



def collect_exc_info(exc_type, exc_val, exc_tb):  #96 (line in Coconut source)
    """Collect information about the given exception for sending to Claude."""  #97 (line in Coconut source)
    filtered_tb = filter_traceback(exc_tb)  #98 (line in Coconut source)

    frame_info = inspect.getframeinfo(filtered_tb.tb_frame)  #100 (line in Coconut source)
    source_lines, source_lineno = inspect.getsourcelines(filtered_tb)  #101 (line in Coconut source)
    pretty_tb = ("\n".join)(traceback.format_exception(exc_type, exc_val, filtered_tb))  #102 (line in Coconut source)

    return DebugContext(name="exception", frame_info=frame_info, source_lines=source_lines, extra_info=_coconut.dict((("traceback", pretty_tb),)))  #104 (line in Coconut source)
