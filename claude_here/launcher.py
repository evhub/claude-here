#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x82db63c1

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

import os  #1 (line in Coconut source)
import urllib  #2 (line in Coconut source)
import webbrowser  #3 (line in Coconut source)

from claude_here.debugger import ALL_DEBUG_CONTEXT  #5 (line in Coconut source)


# META PROMPT:
# The task is for Claude to act as an assistant in debugging Python code. The application will automatically collect information about the currently running environment and send that to Claude to help debug upon encountering an exception or breakpoint. The information available is:
# * The raw source code of the file(s) being debugged.
# * A list of debug contexts, each containing information about a particular called breakpoint or caught exception. The contained information is: the filename, the function being called, the line on which the error occurred, and one of:
#     - The traceback if it's from an exception.
#     - The locals and globals if it's from a breakpoint.

PREAMBLE = """Your task is to analyze the provided source code, breakpoint contexts, and/or unhandled exceptions to identify issues and provide helpful debugging suggestions. You are being called by the `claude_here` debugging library, which the user is using to ask you for debugging help; any cases where you see `import claude_here` or `breakpoint()` are the user asking you for help.

Here's the information you'll be working with:"""  #17 (line in Coconut source)

POSTAMBLE = """Carefully examine the source code, breakpoint contexts, and/or unhandled exceptions provided above. Your goal is to identify the root cause of any errors or issues and suggest solutions to fix them. Follow these steps:

1. Analyze the source code:
   - Look for syntax errors, logical errors, or potential issues in the code structure.
   - Pay attention to common Python pitfalls.

2. Examine the breakpoint contexts and/or unhandled exceptions provided:
   - For each context, note the filename, function, and code context where the error occurred or breakpoint was reached.
   - If it's an exception, carefully review the traceback to understand the error type and message.
   - If it's a breakpoint, analyze the local and global variables to identify any unexpected values or states.

3. Identify the root cause:
   - Cross-reference the provided context with the source code to pinpoint the exact location of the issue.
   - Determine if the error is caused by the code itself or if it's related to external factors (e.g., missing dependencies, environment issues).

4. Develop debugging suggestions:
   - Propose clear and concise solutions to fix any identified issues.
   - If applicable, suggest alternative approaches or best practices to improve the code.
   - Provide explanations for your suggestions to help the user understand the reasoning behind them.
   - If there is anything you're not sure you understand from the provided context, you can ask the user for more information, but you should still give your best attempt at debugging given only the context provided.

5. Present your findings and suggestions:
   - Summarize the identified issues and their locations in the code.
   - List your debugging suggestions in a clear and organized manner.
   - If relevant, include small code snippets to illustrate your suggestions.
   - Format your response using Markdown.

Remember to be thorough in your analysis, clear in your explanations, and helpful in your suggestions. Your goal is to assist the user in resolving their Python code issues effectively."""  #46 (line in Coconut source)


@_coconut_mark_as_match  #49 (line in Coconut source)
def assemble_prompt(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #49 (line in Coconut source)
    """Assemble a concrete prompt from the given structured prompt data."""  #50 (line in Coconut source)

    _coconut_match_check_0 = False  #51 (line in Coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #51 (line in Coconut source)
    if _coconut_match_first_arg is not _coconut_sentinel:  #51 (line in Coconut source)
        _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #51 (line in Coconut source)
    _coconut_match_kwargs_store = _coconut_match_kwargs  #51 (line in Coconut source)
    if not _coconut_match_check_0:  #51 (line in Coconut source)
        _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #51 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "content" in _coconut_match_kwargs)) == 1):  #51 (line in Coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("content")  #51 (line in Coconut source)
            _coconut_match_temp_1 = _coconut.getattr(str, "_coconut_is_data", False) or _coconut.isinstance(str, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in str)  # type: ignore  #51 (line in Coconut source)
            if not _coconut_match_kwargs:  #51 (line in Coconut source)
                _coconut_match_check_0 = True  #51 (line in Coconut source)
        if _coconut_match_check_0:  #51 (line in Coconut source)
            _coconut_match_check_0 = False  #51 (line in Coconut source)
            if not _coconut_match_check_0:  #51 (line in Coconut source)
                _coconut_match_set_name_content = _coconut_sentinel  #51 (line in Coconut source)
                if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_temp_0, str)) and (_coconut.len(_coconut_match_temp_0) >= 1):  #51 (line in Coconut source)
                    _coconut_match_set_name_content = _coconut_match_temp_0[0]  #51 (line in Coconut source)
                    _coconut_match_temp_2 = _coconut.len(_coconut_match_temp_0) <= _coconut.max(1, _coconut.len(_coconut_match_temp_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_0, "_coconut_data_defaults", {}) and _coconut_match_temp_0[i] == _coconut.getattr(_coconut_match_temp_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_0.__match_args__))) if _coconut.hasattr(_coconut_match_temp_0, "__match_args__") else _coconut.len(_coconut_match_temp_0) == 1  # type: ignore  #51 (line in Coconut source)
                    if _coconut_match_temp_2:  #51 (line in Coconut source)
                        _coconut_match_check_0 = True  #51 (line in Coconut source)
                if _coconut_match_check_0:  #51 (line in Coconut source)
                    if _coconut_match_set_name_content is not _coconut_sentinel:  #51 (line in Coconut source)
                        content = _coconut_match_set_name_content  #51 (line in Coconut source)

            if not _coconut_match_check_0:  #51 (line in Coconut source)
                if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_temp_0, str)):  #51 (line in Coconut source)
                    _coconut_match_check_0 = True  #51 (line in Coconut source)
                if _coconut_match_check_0:  #51 (line in Coconut source)
                    _coconut_match_check_0 = False  #51 (line in Coconut source)
                    if not _coconut_match_check_0:  #51 (line in Coconut source)
                        _coconut_match_set_name_content = _coconut_sentinel  #51 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_0) in _coconut_self_match_types:  #51 (line in Coconut source)
                            _coconut_match_set_name_content = _coconut_match_temp_0  #51 (line in Coconut source)
                            _coconut_match_check_0 = True  #51 (line in Coconut source)
                        if _coconut_match_check_0:  #51 (line in Coconut source)
                            if _coconut_match_set_name_content is not _coconut_sentinel:  #51 (line in Coconut source)
                                content = _coconut_match_set_name_content  #51 (line in Coconut source)

                    if not _coconut_match_check_0:  #51 (line in Coconut source)
                        _coconut_match_set_name_content = _coconut_sentinel  #51 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_0) in _coconut_self_match_types:  #51 (line in Coconut source)
                            _coconut_match_temp_3 = _coconut.getattr(str, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #51 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_3, _coconut.tuple):  #51 (line in Coconut source)
                                raise _coconut.TypeError("str.__match_args__ must be a tuple")  #51 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_3) < 1:  #51 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'str' only supports %s)" % (_coconut.len(_coconut_match_temp_3),))  #51 (line in Coconut source)
                            _coconut_match_temp_4 = _coconut.getattr(_coconut_match_temp_0, _coconut_match_temp_3[0], _coconut_sentinel)  #51 (line in Coconut source)
                            if _coconut_match_temp_4 is not _coconut_sentinel:  #51 (line in Coconut source)
                                _coconut_match_set_name_content = _coconut_match_temp_4  #51 (line in Coconut source)
                                _coconut_match_check_0 = True  #51 (line in Coconut source)
                        if _coconut_match_check_0:  #51 (line in Coconut source)
                            if _coconut_match_set_name_content is not _coconut_sentinel:  #51 (line in Coconut source)
                                content = _coconut_match_set_name_content  #51 (line in Coconut source)





        if _coconut_match_check_0:  #51 (line in Coconut source)

                return content  #51 (line in Coconut source)

    if not _coconut_match_check_0:  #52 (line in Coconut source)
        _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #52 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "objs" in _coconut_match_kwargs)) == 1):  #52 (line in Coconut source)
            _coconut_match_temp_5 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("objs")  #52 (line in Coconut source)
            _coconut_match_temp_6 = _coconut.getattr(list, "_coconut_is_data", False) or _coconut.isinstance(list, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in list)  # type: ignore  #52 (line in Coconut source)
            if not _coconut_match_kwargs:  #52 (line in Coconut source)
                _coconut_match_check_0 = True  #52 (line in Coconut source)
        if _coconut_match_check_0:  #52 (line in Coconut source)
            _coconut_match_check_0 = False  #52 (line in Coconut source)
            if not _coconut_match_check_0:  #52 (line in Coconut source)
                _coconut_match_set_name_objs = _coconut_sentinel  #52 (line in Coconut source)
                if (_coconut_match_temp_6) and (_coconut.isinstance(_coconut_match_temp_5, list)) and (_coconut.len(_coconut_match_temp_5) >= 1):  #52 (line in Coconut source)
                    _coconut_match_set_name_objs = _coconut_match_temp_5[0]  #52 (line in Coconut source)
                    _coconut_match_temp_7 = _coconut.len(_coconut_match_temp_5) <= _coconut.max(1, _coconut.len(_coconut_match_temp_5.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_5, "_coconut_data_defaults", {}) and _coconut_match_temp_5[i] == _coconut.getattr(_coconut_match_temp_5, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_5.__match_args__))) if _coconut.hasattr(_coconut_match_temp_5, "__match_args__") else _coconut.len(_coconut_match_temp_5) == 1  # type: ignore  #52 (line in Coconut source)
                    if _coconut_match_temp_7:  #52 (line in Coconut source)
                        _coconut_match_check_0 = True  #52 (line in Coconut source)
                if _coconut_match_check_0:  #52 (line in Coconut source)
                    if _coconut_match_set_name_objs is not _coconut_sentinel:  #52 (line in Coconut source)
                        objs = _coconut_match_set_name_objs  #52 (line in Coconut source)

            if not _coconut_match_check_0:  #52 (line in Coconut source)
                if (not _coconut_match_temp_6) and (_coconut.isinstance(_coconut_match_temp_5, list)):  #52 (line in Coconut source)
                    _coconut_match_check_0 = True  #52 (line in Coconut source)
                if _coconut_match_check_0:  #52 (line in Coconut source)
                    _coconut_match_check_0 = False  #52 (line in Coconut source)
                    if not _coconut_match_check_0:  #52 (line in Coconut source)
                        _coconut_match_set_name_objs = _coconut_sentinel  #52 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_5) in _coconut_self_match_types:  #52 (line in Coconut source)
                            _coconut_match_set_name_objs = _coconut_match_temp_5  #52 (line in Coconut source)
                            _coconut_match_check_0 = True  #52 (line in Coconut source)
                        if _coconut_match_check_0:  #52 (line in Coconut source)
                            if _coconut_match_set_name_objs is not _coconut_sentinel:  #52 (line in Coconut source)
                                objs = _coconut_match_set_name_objs  #52 (line in Coconut source)

                    if not _coconut_match_check_0:  #52 (line in Coconut source)
                        _coconut_match_set_name_objs = _coconut_sentinel  #52 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_5) in _coconut_self_match_types:  #52 (line in Coconut source)
                            _coconut_match_temp_8 = _coconut.getattr(list, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #52 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_8, _coconut.tuple):  #52 (line in Coconut source)
                                raise _coconut.TypeError("list.__match_args__ must be a tuple")  #52 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_8) < 1:  #52 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'list' only supports %s)" % (_coconut.len(_coconut_match_temp_8),))  #52 (line in Coconut source)
                            _coconut_match_temp_9 = _coconut.getattr(_coconut_match_temp_5, _coconut_match_temp_8[0], _coconut_sentinel)  #52 (line in Coconut source)
                            if _coconut_match_temp_9 is not _coconut_sentinel:  #52 (line in Coconut source)
                                _coconut_match_set_name_objs = _coconut_match_temp_9  #52 (line in Coconut source)
                                _coconut_match_check_0 = True  #52 (line in Coconut source)
                        if _coconut_match_check_0:  #52 (line in Coconut source)
                            if _coconut_match_set_name_objs is not _coconut_sentinel:  #52 (line in Coconut source)
                                objs = _coconut_match_set_name_objs  #52 (line in Coconut source)





        if _coconut_match_check_0:  #52 (line in Coconut source)

                return ("\n\n".join)((map)(assemble_prompt, objs))  #52 (line in Coconut source)

    if not _coconut_match_check_0:  #53 (line in Coconut source)
        _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #53 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "tags" in _coconut_match_kwargs)) == 1):  #53 (line in Coconut source)
            _coconut_match_temp_10 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("tags")  #53 (line in Coconut source)
            _coconut_match_temp_11 = _coconut.getattr(dict, "_coconut_is_data", False) or _coconut.isinstance(dict, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in dict)  # type: ignore  #53 (line in Coconut source)
            if not _coconut_match_kwargs:  #53 (line in Coconut source)
                _coconut_match_check_0 = True  #53 (line in Coconut source)
        if _coconut_match_check_0:  #53 (line in Coconut source)
            _coconut_match_check_0 = False  #53 (line in Coconut source)
            if not _coconut_match_check_0:  #53 (line in Coconut source)
                _coconut_match_set_name_tags = _coconut_sentinel  #53 (line in Coconut source)
                if (_coconut_match_temp_11) and (_coconut.isinstance(_coconut_match_temp_10, dict)) and (_coconut.len(_coconut_match_temp_10) >= 1):  #53 (line in Coconut source)
                    _coconut_match_set_name_tags = _coconut_match_temp_10[0]  #53 (line in Coconut source)
                    _coconut_match_temp_12 = _coconut.len(_coconut_match_temp_10) <= _coconut.max(1, _coconut.len(_coconut_match_temp_10.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_10, "_coconut_data_defaults", {}) and _coconut_match_temp_10[i] == _coconut.getattr(_coconut_match_temp_10, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_10.__match_args__))) if _coconut.hasattr(_coconut_match_temp_10, "__match_args__") else _coconut.len(_coconut_match_temp_10) == 1  # type: ignore  #53 (line in Coconut source)
                    if _coconut_match_temp_12:  #53 (line in Coconut source)
                        _coconut_match_check_0 = True  #53 (line in Coconut source)
                if _coconut_match_check_0:  #53 (line in Coconut source)
                    if _coconut_match_set_name_tags is not _coconut_sentinel:  #53 (line in Coconut source)
                        tags = _coconut_match_set_name_tags  #53 (line in Coconut source)

            if not _coconut_match_check_0:  #53 (line in Coconut source)
                if (not _coconut_match_temp_11) and (_coconut.isinstance(_coconut_match_temp_10, dict)):  #53 (line in Coconut source)
                    _coconut_match_check_0 = True  #53 (line in Coconut source)
                if _coconut_match_check_0:  #53 (line in Coconut source)
                    _coconut_match_check_0 = False  #53 (line in Coconut source)
                    if not _coconut_match_check_0:  #53 (line in Coconut source)
                        _coconut_match_set_name_tags = _coconut_sentinel  #53 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_10) in _coconut_self_match_types:  #53 (line in Coconut source)
                            _coconut_match_set_name_tags = _coconut_match_temp_10  #53 (line in Coconut source)
                            _coconut_match_check_0 = True  #53 (line in Coconut source)
                        if _coconut_match_check_0:  #53 (line in Coconut source)
                            if _coconut_match_set_name_tags is not _coconut_sentinel:  #53 (line in Coconut source)
                                tags = _coconut_match_set_name_tags  #53 (line in Coconut source)

                    if not _coconut_match_check_0:  #53 (line in Coconut source)
                        _coconut_match_set_name_tags = _coconut_sentinel  #53 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_10) in _coconut_self_match_types:  #53 (line in Coconut source)
                            _coconut_match_temp_13 = _coconut.getattr(dict, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #53 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_13, _coconut.tuple):  #53 (line in Coconut source)
                                raise _coconut.TypeError("dict.__match_args__ must be a tuple")  #53 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_13) < 1:  #53 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'dict' only supports %s)" % (_coconut.len(_coconut_match_temp_13),))  #53 (line in Coconut source)
                            _coconut_match_temp_14 = _coconut.getattr(_coconut_match_temp_10, _coconut_match_temp_13[0], _coconut_sentinel)  #53 (line in Coconut source)
                            if _coconut_match_temp_14 is not _coconut_sentinel:  #53 (line in Coconut source)
                                _coconut_match_set_name_tags = _coconut_match_temp_14  #53 (line in Coconut source)
                                _coconut_match_check_0 = True  #53 (line in Coconut source)
                        if _coconut_match_check_0:  #53 (line in Coconut source)
                            if _coconut_match_set_name_tags is not _coconut_sentinel:  #53 (line in Coconut source)
                                tags = _coconut_match_set_name_tags  #53 (line in Coconut source)





        if _coconut_match_check_0:  #53 (line in Coconut source)

                return (assemble_prompt)((list)(tags.items()))  #53 (line in Coconut source)

    if not _coconut_match_check_0:  #54 (line in Coconut source)
        _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #54 (line in Coconut source)
        _coconut_match_set_name_tag = _coconut_sentinel  #54 (line in Coconut source)
        _coconut_match_set_name_content = _coconut_sentinel  #54 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 1:  #54 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 2):  #54 (line in Coconut source)
                _coconut_match_set_name_tag = _coconut_match_args[0][0]  #54 (line in Coconut source)
                _coconut_match_set_name_content = _coconut_match_args[0][1]  #54 (line in Coconut source)
                if not _coconut_match_kwargs:  #54 (line in Coconut source)
                    _coconut_match_check_0 = True  #54 (line in Coconut source)
        if _coconut_match_check_0:  #54 (line in Coconut source)
            if _coconut_match_set_name_tag is not _coconut_sentinel:  #54 (line in Coconut source)
                tag = _coconut_match_set_name_tag  #54 (line in Coconut source)
            if _coconut_match_set_name_content is not _coconut_sentinel:  #54 (line in Coconut source)
                content = _coconut_match_set_name_content  #54 (line in Coconut source)

        if _coconut_match_check_0:  #54 (line in Coconut source)

                return "<{_coconut_format_0}>\n{_coconut_format_1}\n</{_coconut_format_2}>".format(_coconut_format_0=(tag), _coconut_format_1=(assemble_prompt(content)), _coconut_format_2=(tag))  #54 (line in Coconut source)



    if not _coconut_match_check_0:  #57 (line in Coconut source)
        raise _coconut_FunctionMatchError('case def assemble_prompt:', _coconut_match_args)  #57 (line in Coconut source)

def generate_prompt(all_debug_context, max_context_items):  #57 (line in Coconut source)
    """Generate a full prompt for Claude using the given debug context."""  #58 (line in Coconut source)
    prompt_cmpts = [PREAMBLE,]  #59 (line in Coconut source)

    for filepath, debug_contexts in all_debug_context.items():  #61 (line in Coconut source)
        filename = os.path.basename(filepath)  #62 (line in Coconut source)
        file_prompt_cmpts = [_coconut.dict((("source_code", (("".join)(_coconut_iter_getitem(((filter)(ident, (map)(_coconut.operator.attrgetter("source_lines"), debug_contexts))), (0))))),)),]  #63 (line in Coconut source)
        for ctx in _coconut_iter_getitem(debug_contexts, _coconut.slice(-max_context_items, None)):  #72 (line in Coconut source)
            info_dict = _coconut.dict((("executing_function", ctx.function), ("executing_code", ("".join)(ctx.context_lines))))  #73 (line in Coconut source)
            info_dict |= ctx.extra_info  #77 (line in Coconut source)
            file_prompt_cmpts += [_coconut.dict(((ctx.name, info_dict),)),]  #78 (line in Coconut source)
        prompt_cmpts += [_coconut.dict(((filename, file_prompt_cmpts),)),]  #79 (line in Coconut source)

    prompt_cmpts += [POSTAMBLE,]  #81 (line in Coconut source)
    return assemble_prompt(prompt_cmpts)  #82 (line in Coconut source)



def launch_claude(max_context_items=5):  #85 (line in Coconut source)
    """Launch claude.ai with all the collected debug context."""  #86 (line in Coconut source)
    prompt = generate_prompt(ALL_DEBUG_CONTEXT, max_context_items=max_context_items)  #87 (line in Coconut source)
    encoded_prompt = urllib.parse.quote_plus(prompt)  #88 (line in Coconut source)
    webbrowser.open("https://claude.ai/new?q={_coconut_format_0}".format(_coconut_format_0=(encoded_prompt)))  #89 (line in Coconut source)
