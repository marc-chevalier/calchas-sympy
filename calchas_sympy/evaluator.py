from sympy import latex
from sympy.parsing.sympy_parser import stringify_expr, eval_expr, standard_transformations
from calchas_datamodel import AbstractExpression
from .translator import Translator

PREEXEC = """from sympy import *"""


class SympyEvaluator:
    def __init__(self):
        self.outputRawString = None
        self.outputLatex = None
        self.output_calchas = None

    def evaluate(self, input_calchas: AbstractExpression):
        builder = Translator(input_calchas)
        output_sympy = builder.to_sympy_tree()
        self.output_calchas =
        self.outputRawString, self.outputLatex = str(output_sympy), latex(output_sympy)


def eval_input(input_tree):
    namespace = {}
    exec(PREEXEC, {}, namespace)

    def plot(f=None, **kwargs):
        pass
    namespace.update({
        'plot': plot,  # prevent textplot from printing stuff
        'help': lambda f: f
    })

    transformations = list(standard_transformations)
    parsed = stringify_expr(input_tree, {}, namespace, transformations)
    try:
        evaluated = eval_expr(parsed, {}, namespace)
    except SyntaxError:
        raise
    except Exception as e:
        raise ValueError(str(e))

    return str(evaluated), latex(evaluated)
