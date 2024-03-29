from calchas_sympy.evaluator import evaluate
from unittest import TestCase

class TestEvaluation(TestCase):

    def procedure(self, testCases, debug=False):
        for test in testCases:
            if len(test)==2:
                (expr, res) = test
            else:
                (expr, res, debug) = test
            if debug:
                print(expr)
            strOutput, latexOutput = evaluate(expr, debug)
            self.assertEqual(latexOutput, res)

    def testNumeric(self):
        testCases = [('2/4', '\\frac{1}{2}'),
                     ('4/2', '2'),
                     ('Sqrt[4]', '2'),
                     ('2^42', '4398046511104'),
                     ('sqrt(4)', '2'),
                     ('sqrt((42)**(pi))', '42^{\\frac{\\pi}{2}}'),
                     ('10!', '3628800'),
                    ]
        self.procedure(testCases)

    def testSimplify(self):
        testCases = [('sqrt(x)**2', 'x'),
                     ('Sqrt[x]^2', 'x'),
                     ('x-x', '0'),
                     ('sin(x)**2+cos(x)**2', '1'),
                     ('(n+1)!/n!', 'n + 1'),
                    ]
        self.procedure(testCases)

    def testSympyLanguage(self):
        testCases = [('diff(x**2,x)', '2 x'),
                     ('2*integrate(exp(-x**2/2), (x,(-oo,oo)))', '2 \\sqrt{2} \\sqrt{\\pi}'),
                     ('summation(1/n**2, (n,(1,oo)))', '\\frac{\\pi^{2}}{6}'),
                     ('(n+1)*n!-(n+1)!', '0'),
                     ('N(GoldenRatio,100)', '1.618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137'),
                     ('N(EulerGamma,100)', '0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495'),
                     ('Pow(1024,1/2)', '32'),
                     ('Abs(1)', '1'),
                     ('floor(-Pi)', '-4'),
                     ('ceiling(-Pi)', '-3'),
                     ('floor(Pi)', '3'),
                     ('ceiling(Pi)', '4'),
                     ('(a/(b+1)/c)+1/(d+1)', '\\frac{a \\left(d + 1\\right) + c \\left(b + 1\\right)}{c \\left(b + 1\\right) \\left(d + 1\\right)}'),
                     ('diff(erf(x),x)','\\frac{2}{\\sqrt{\\pi}} e^{- x^{2}}'),
                    ]
        self.procedure(testCases)

    def testMathematicaLanguage(self):
        testCases = [('Integrate[Exp[-x^2/2], {x, -Infinity, Infinity}]', '\\sqrt{2} \\sqrt{\\pi}'),
                     ('Sum[1/i^6, {i, 1, Infinity}]', '\\frac{\\pi^{6}}{945}'),
                     ('Sum[j/i^6, {i, 1, Infinity}, {j, 0 ,m}]', '\\frac{\\pi^{6} m}{1890} \\left(m + 1\\right)'),
                     ('Integrate[1/(x^3 + 1), x]', '\\frac{1}{3} \\log{\\left (x + 1 \\right )} - \\frac{1}{6} \\log{\\left (x^{2} - x + 1 \\right )} + \\frac{\\sqrt{3}}{3} \\operatorname{atan}{\\left (\\frac{\\sqrt{3}}{3} \\left(2 x - 1\\right) \\right )}'),
                     ('Integrate[1/(x^3 + 1), {x, 0, 1}]', '\\frac{1}{3} \\log{\\left (2 \\right )} + \\frac{\\sqrt{3} \\pi}{9}'),
                     ('Integrate[Sin[x*y], {x, 0, 1}, {y, 0, x}]', '- \\frac{1}{2} \\operatorname{Ci}{\\left (1 \\right )} + \\frac{\\gamma}{2}'),
                     ('D[x^2,x]', '2 x'),
                     ('D[x^3,x,x]', '6 x'),
                     ('D[x^4, {x,2}]', '12 x^{2}'),
                     ('D[x^4*Cos[y^4], {x,2}, {y,3}]', '96 x^{2} y \\left(8 y^{8} \\sin{\\left (y^{4} \\right )} - 18 y^{4} \\cos{\\left (y^{4} \\right )} - 3 \\sin{\\left (y^{4} \\right )}\\right)'),
                     ('D[x^4*Cos[y]^z, {x,2}, y, {z,3}]', '- 12 x^{2} \\left(z \\log{\\left (\\cos{\\left (y \\right )} \\right )} + 3\\right) \\log^{2}{\\left (\\cos{\\left (y \\right )} \\right )} \\sin{\\left (y \\right )} \\cos^{z - 1}{\\left (y \\right )}'),
                     ('Sin\'[x]', '\\cos{\\left (x \\right )}'),
                     ('N[Pi]', '3.14159265358979'),
                     ('N[Sqrt[2], 100]', '1.414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641573'),
                     ('N[GoldenRatio,100]', '1.618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137'),
                     ('N[EulerGamma,100]', '0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495'),
                     ('N[Power[1024, 0.5]]', '32.0'),
                     ('Log[Exp[x^n]]', '\\log{\\left (e^{x^{n}} \\right )}'),
                     ('Log10[Exp[x^n]]', '\\frac{\\log{\\left (e^{x^{n}} \\right )}}{\\log{\\left (10 \\right )}}'),
                     ('Log10[1000]', '3'),
                     ('Factorial[10]', '3628800'),
                     ('N[Factorial[3.1]/Factorial[2.1]]', '3.1'),
                     ('Abs[1]', '1'),
                     ('Abs[-1]', '1'),
                     ('Abs[x]', '\\left|{x}\\right|'),
                     ('Abs[-Pi]', '\\pi'),
                     ('Floor[-Pi]', '-4'),
                     ('Ceiling[-Pi]', '-3'),
                     ('Floor[Pi]', '3'),
                     ('Ceiling[Pi]', '4'),
                     ('Limit[Sin[x]/x, x->0]', '1'),
                     ('Limit[(1+x/n)^n, n->Infinity]', 'e^{x}'),
                     ('Limit[Sum[1/i, {i, 1, n}]- Log[n], n->Infinity]', '\\gamma'),
                     ('Solve[x^2==1, x]', '\\left [ -1, \\quad 1\\right ]'),
                     ('Expand[(x+1)*(x-1)]', 'x^{2} - 1'),
                     ('Factor[x^2+x]', 'x \\left(x + 1\\right)'),
                     ('Prime[5]', '11'),
                     ('PrimeQ[5]', '\\mathrm{True}'),
                     ('N[1- Sum[Binomial[10,k] * 0.2^k *0.8^(10-k), {k, 0, 3}]]', '0.1208738816'),
                     ]
        self.procedure(testCases)

    def testCalchas(self):
        testCases = [('3^3', '27'),
                     ('4**4', '256'),
                     ('12%5', '2'),
                     ('Numeric(Pi)', '3.14159265358979'),
                     ('eval(Sqrt(2), 100)', '1.414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641573'),
                     ('approx(GoldenRatio,100)', '1.618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137'),
                     ('evalf(EulerGamma,100)', '0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495'),
                     ('power(32,2)', '1024'),
                     ('Pow(1024,1/2)', '32'),
                     ('Power(1024,1/2)', '32'),
                     ('sqrt(64)', '8'),
                     ('root(27,3)', '3'),
                     ('N(Power(1024, 0.5))', '32.0'),
                     ('Log10(Exp(x**n))', '\\frac{\\log{\\left (e^{x^{n}} \\right )}}{\\log{\\left (10 \\right )}}'),
                     ('Log10(1000)', '3'),
                     ('Lg(1000)', '3'),
                     ('ln(exp(1))', '1'),
                     ('Log(1000,10)', '3'),
                     ('log(1024,2)', '10'),
                     ('lb(1024)', '10'),
                     ('Factorial(10)', '3628800'),
                     ('Gamma(3/2)', '\\frac{\\sqrt{\\pi}}{2}'),
                     ('N(Factorial(3.1)/Fact(2.1))', '3.1'),
                     ('Abs(1)', '1'),
                     ('Abs(-1)', '1'),
                     ('Abs(x)', '\\left|{x}\\right|'),
                     ('Ceiling(-Pi)', '-3'),
                     ('Floor(-Pi)', '-4'),
                     ('ceil(-Pi)', '-3'),
                     ('Floor(Pi)', '3'),
                     ('ceil(pi)', '4'),
                     ('sgn(0)', '0'),
                     ('Signum(-gamma)', '-1'),
                     ('sig(Phi)', '1'),
                     ('Sign(-e)', '-1'),
                     ('sin(pi/3)', '\\frac{\\sqrt{3}}{2}'),
                     ('cos(pi/3)', '\\frac{1}{2}'),
                     ('tan(pi/3)', '\\sqrt{3}'),
                     ('arcsin(1/2)', '\\frac{\\pi}{6}'),
                     ('acos(1/2)', '\\frac{\\pi}{3}'),
                     ('aTan(1)', '\\frac{\\pi}{4}'),
                     ('C(6,4)', '15'),
                     ('C(6,-1)', '0'),
                     ('C(6,6)', '1'),
                     ('C(6,7)', '0'),
                     ('C(-1,4)', '\\mathrm{NaN}'),
                     ('C(-1,-2)', '\\mathrm{NaN}'),
                     ('C(-2,-1)', '\\mathrm{NaN}'),
                     ('C(-2.5,-1.5)', '0'),
                     ('N(C(1.3,3.7))', '0.0284312028601124'),
                     ('N(C(3.7,1.3))', '4.43659695748368'),
                     ('gcd(6,4)', '2'),
                     ('lcm(n,m)hcf(n,m)', 'm n'),
                     ('Diff(x^4*Cos(y)^z, {x,2}, y, {z,3})', '- 12 x^{2} \\left(z \\log{\\left (\\cos{\\left (y \\right )} \\right )} + 3\\right) \\log^{2}{\\left (\\cos{\\left (y \\right )} \\right )} \\sin{\\left (y \\right )} \\cos^{z - 1}{\\left (y \\right )}'),
                     ('diff(x**2 y^3,x)', '2 x y^{3}'),
                     ('derivate(x**2 y^3,x)', '2 x y^{3}'),
                     ('derivative(x**2 y^3,x)', '2 x y^{3}'),
                     ('integral(Exp(-x^2/2), x, -infinity, oo)', '\\sqrt{2} \\sqrt{\\pi}'),
                     ('integral(Exp(-x**2/2), x, -infinity, oo)', '\\sqrt{2} \\sqrt{\\pi}'),
                     ('sum(1/i^6, i, 1, Infty)', '\\frac{\\pi^{6}}{945}'),
                     ('int(1/(x^3 + 1), x)', '\\frac{1}{3} \\log{\\left (x + 1 \\right )} - \\frac{1}{6} \\log{\\left (x^{2} - x + 1 \\right )} + \\frac{\\sqrt{3}}{3} \\operatorname{atan}{\\left (\\frac{\\sqrt{3}}{3} \\left(2 x - 1\\right) \\right )}'),
                     ('Integrate(1/(x^3 + 1), x, 0, 1)', '\\frac{1}{3} \\log{\\left (2 \\right )} + \\frac{\\sqrt{3} \\pi}{9}'),
                     ('solve(ch(x)=y,x)', '\\left [ \\log{\\left (y - \\sqrt{y^{2} - 1} \\right )}, \\quad \\log{\\left (y + \\sqrt{y^{2} - 1} \\right )}\\right ]'),
                     ('solve(sinh(x)==y,x)', '\\left [ \\log{\\left (y - \\sqrt{y^{2} + 1} \\right )}, \\quad \\log{\\left (y + \\sqrt{y^{2} + 1} \\right )}\\right ]'),
                     ('lim(sin(x)/x, x, 0)', '1'),
                     ('limit(tan(x), x, Pi/2)', '-\\infty'),
                     ('LimitR(tan(x), x, Pi/2)', '-\\infty'),
                     ('Liml(tan(x), x, 1/2*Pi)', '\\infty'),
                     ('sin(x)^2+cos(x)^2=1', '\\mathrm{True}'),
                     ('3=4', '\\mathrm{False}'),
                     ('2=2', '\\mathrm{True}'),
                     ('x=y', 'x = y'),
                     ('2f(x)b', '2 b f{\\left (x \\right )}'),
                     ("sin'''(x)","- \\cos{\\left (x \\right )}"),
                     ("log''(x)","- \\frac{1}{x^{2}}"),
                     ("abs'(x)","\\frac{1}{\\left|{x}\\right|} \\left(\\Re{x} \\frac{d}{d x} \\Re{x} + \\Im{x} \\frac{d}{d x} \\Im{x}\\right)"),
                     ("sqrt'(x)","\\frac{1}{2 \\sqrt{x}}"),
                     ('isprime(5)','\mathrm{True}'),
                     ('prime(5)','11'),
                     ('x & x & x | x & y','x'),
                     ('satisfiable(x & x & x | x & y)','\\left \\{ x : \\mathrm{True}, \\quad y : \\mathrm{True}\\right \\}'),
                     ('satisfiable(x & ~y)','\\left \\{ x : \\mathrm{True}, \\quad y : \\mathrm{False}\\right \\}'),
                     ('satisfiable(x & ~x)','\\mathrm{False}'),
                     ('satisfiable(x | ~x)','\\left \\{ x : \\mathrm{False}\\right \\}'),
                     ('D(erf(x),x)','\\frac{2}{\\sqrt{\\pi}} e^{- x^{2}}'),
                     ('D(cos)','\\left( x_{0} \\mapsto - \\sin{\\left (x_{0} \\right )} \\right)'),
                     ('integrate(cos)','\\left( x_{0} \\mapsto \\sin{\\left (x_{0} \\right )} \\right)'),
                     ('D(2*cos)','\\left( x_{0} \\mapsto - 2 \\sin{\\left (x_{0} \\right )} \\right)'),
                     ('D(cos + sin)','\\left( x_{0} \\mapsto - \\sin{\\left (x_{0} \\right )} + \\cos{\\left (x_{0} \\right )} \\right)'),
                     ('D(D(cos))','\\left( x_{0} \\mapsto - \\cos{\\left (x_{0} \\right )} \\right)'),
                    ]
        self.procedure(testCases)

    def testLatex(self):
        testCases = [("\\sqrt{9}", "3"),
                     ("\\frac{42}{1337}", "\\frac{6}{191}"),
                     ("\\sqrt[3]{27}", "3"),
                     ("\\sum_{i=1}^\\infty (1/i^{2})", "\\frac{\\pi^{2}}{6}"),
                     ("\\sum_{i=1}^\\infty (1/Pow(i,2))", "\\frac{\\pi^{2}}{6}"),
                     ("\\binom{6}{4}", "15"),
                     ("\\sqrt{x^2}", "\\sqrt{x^{2}}"),
                     ("2\\times(1+3)", "8"),
                    ]
        self.procedure(testCases)

