# claude-here

_debug Python with [claude.ai](https://claude.ai/new)_

## usage

Just
```bash
pip install claude-here
```
then
```python
import claude_here
```
and any uncaught exceptions will automatically launch a new conversation in [claude.ai](https://claude.ai/new) pre-filled with information for Claude to help you debug the error.

To debug something that isn't causing an exception, just add
```python
breakpoint()
```
where you want to debug and it will automatically launch Claude with info about the current locals to help you debug.

### nice things

Some extra features to note:
* If a `breakpoint` is hit multiple times, or an uncaught exception is raised after hitting a `breakpoint`, the information sent to Claude will be cumulative.
* If `claude_here` detects that [`webbrowser`](https://docs.python.org/3/library/webbrowser.html) will use a text-based browser by default, it will instead print an [OSC-8-compliant](https://github.com/Alhadis/OSC8-Adoption/) hyperlink to the terminal for you to open using a graphical browser. This is especially useful if you are debugging a remote machine.

### `breakpoint`

`breakpoint` additionally supports some optional arguments:
- `base_debugger` determines the debugger to call in addition to launching Claude. Defaults to [`pdb.set_trace`](https://docs.python.org/3/library/pdb.html). Setting to `None` will set up a simple prompt to ask you when you're ready to continue execution.
- `just_gather_info=True` will gather information to send to Claude later (on an uncaught exception or `breakpoint` without `just_gather_info=True`) without actually launching Claude or the `base_debugger`.

### environment variables

`claude_here` supports some additional configuration via environment variables:
- `CLAUDE_HERE_PROJECT_ID` can be set to a [Claude Projects](https://claude.ai/projects) UUID (`https://claude.ai/project/<this-part-here-is-the-uuid>`) to launch your debugging conversations in.
- `CLAUDE_HERE_MAX_CONTEXT_ITEMS` can be set to an integer that will determine the maximum number of prior `breakpoint` contexts that will be sent to Claude.
