import contextlib
import io
import re


def extract_function_name(text):
    """Find a function definition and return its name.

    text: String

    returns: String or None
    """
    pattern = r"def\s+(\w+)\s*\("
    match = re.search(pattern, text)
    if match:
        func_name = match.group(1)
        return func_name
    else:
        return None


# as funções que definem comandos mágicos de célula só são definidas
# se estivermos rodando no Jupyter.

try:
    from IPython.core.magic import register_cell_magic
    from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring

    @register_cell_magic
    def add_method_to(args, cell):

        # obtém o nome da função definida nesta célula
        func_name = extract_function_name(cell)
        if func_name is None:
            return f"This cell doesn't define any new functions."

        # obtém a classe à qual vamos adicioná-la
        namespace = get_ipython().user_ns
        class_name = args
        cls = namespace.get(class_name, None)
        if cls is None:
            return f"Class '{class_name}' not found."

        # guarda a versão antiga da função, se ela já estava definida
        old_func = namespace.get(func_name, None)
        if old_func is not None:
            del namespace[func_name]

        # Executa a célula para definir a função
        get_ipython().run_cell(cell)

        # obtém a função recém-definida
        new_func = namespace.get(func_name, None)
        if new_func is None:
            return f"This cell didn't define {func_name}."

        # adiciona a função à classe e a remove do namespace
        setattr(cls, func_name, new_func)
        del namespace[func_name]

        # restaura a função antiga no namespace
        if old_func is not None:
            namespace[func_name] = old_func

    @register_cell_magic
    def expect_error(line, cell):
        try:
            get_ipython().run_cell(cell)
        except Exception as e:
            get_ipython().run_cell("%tb")

    @magic_arguments()
    @argument("exception", help="Type of exception to catch")
    @register_cell_magic
    def expect(line, cell):
        args = parse_argstring(expect, line)
        exception = eval(args.exception)
        try:
            get_ipython().run_cell(cell)
        except exception as e:
            get_ipython().run_cell("%tb")

    def traceback(mode):
        """Set the traceback mode.

        mode: string
        """
        with contextlib.redirect_stdout(io.StringIO()):
            get_ipython().run_cell(f"%xmode {mode}")

    traceback("Minimal")
except (ImportError, NameError):
    print("Warning: IPython is not available, cell magic not defined.")
