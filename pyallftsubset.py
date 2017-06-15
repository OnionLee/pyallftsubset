import sys
import os
import subprocess

def get_arg(arg_name, default, req=False):
    for i in range(0, len(sys.argv)):
        if sys.argv[i] == arg_name:
            if i + 1 < len(sys.argv):
                return sys.argv[i + 1]
            else:
                print('pyallftsubset.py --subset_path [required] --input_path [optional] --output_path [optional]')
                exit()

    if req:
        print('pyallftsubset.py --subset_path [required] --input_path [optional] --output_path [optional]')
        exit()
    else:
        return default
    
input_path = get_arg('--input_path', './')
output_path = get_arg('--output_path', './')
subset = get_arg('--subset_path', '', True)

if not os.path.isfile(subset):
    print('subset file not found - ' + subset)
    exit()

stdout = subprocess.getoutput('pip install -r requirements.txt')
print(stdout)
    
for root, dirs, files in os.walk(input_path):
    for file in files:
        if file.endswith('.otf') or file.endswith('.ttf'):
            cmd = 'pyftsubset {0} --output-file={1} --text-file={2}'.format(input_path + file, output_path + 'subset_' +file, subset)
            print(cmd)
            stdout = subprocess.getoutput(cmd)
            print(stdout)

print('done.')
