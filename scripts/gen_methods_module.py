import argparse
import yaml
from collections import namedtuple

Param = namedtuple('Param', [
    'name',
    'default'
])

Method = namedtuple('Method', [
    'func_name',
    'meth_name',
    'params'
])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--methods_yaml_fn',   '-y', default='data/methods.yaml')
    parser.add_argument('--methods_module_fn', '-m', default='src/lastfmget/methods.py')
    args = parser.parse_args()

    with open(args.methods_yaml_fn, 'r') as f:
        methodsyaml = yaml.safe_load(f)

    methods = get_methods_list(methodsyaml)
    lines   = write_methods_module_lines(methods)

    with open(args.methods_module_fn, 'w') as f:
        f.writelines('\n'.join(lines))

def get_methods_list(methodsyaml):
    methods = []

    paramdefaults    = methodsyaml['param_defaults']
    methodcategories = methodsyaml['categories']

    for category, categorydata in methodcategories.items():
        categoryparams  = categorydata['common_params']
        categorymethods = categorydata['methods']

        for method in categorymethods:
            functionname = f'{category}_{method["function"]}'
            methodname   = f'{category}.{method["method"]}'

            paramnames = categoryparams + method['params']
            params = [ Param(name, paramdefaults[name]) for name in paramnames ]

            methods.append(Method(functionname, methodname, params))

    return methods
            
def write_methods_module_lines(methods):
    lines = []
    lines.append('from .core import __get_response')
    lines.append('')

    for method in methods:
        argstring = ''
        for i, param in enumerate(method.params):
            argstring += param.name
            if param.default is not None:
                argstring += f'={param.default}'
            if i < len(method.params) - 1:
                argstring += ', '

        lines.append(f'def {method.func_name}({argstring}):')
        lines.append(f'    """ {method.meth_name} """')
        lines.append('')
        lines.append('    payload = {')

        params = [(wrap_str('method'), wrap_str(method.meth_name))]
        params += [ (wrap_str(param.name), param.name) for param in method.params ]
        alignwidth = max(len(param[0]) + 1 for param in params)

        for i, param in enumerate(params):
            lines.append(f'        {param[0]:<{alignwidth}}: {param[1]}{"," if i < len(params)-1 else ""}')

        lines.append('    }')
        lines.append('    return __get_response(payload)')
        lines.append('')
    
    return lines

def wrap_str(s):
    return "'" + s + "'"

if __name__ == '__main__':
    main()
