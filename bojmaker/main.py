import os, sys, argparse
from bs4 import BeautifulSoup
from urllib.request import urlopen


def file_maker(folder_name, problem_input):
    sol_py_content = '''import sys
    
sys.stdin = open('{}\input.txt'.format(os.path.dirname(os.path.realpath(__file__))))'''

    sol_cpp_content = '''#include <iostream>
using namespace std;

int main(void)
{
   freopen("input.txt", "r", stdin);
   return 0;
}
    
    '''

    sol_java_content = '''package packageName;

import java.io.*;

public class className {
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    }
}
'''
    

    input_text = open('./{}/input.txt'.format(folder_name), 'w')
    input_text.write(problem_input)
    input_text.close()

    # if language == 'py':
    sol_py = open('./{}/sol1.py'.format(folder_name), 'w')
    sol_py.write(sol_py_content)
    sol_py.close()
    
    # elif language == 'cpp':
    sol_cpp = open('./{}/sol1.cpp'.format(folder_name), 'w')
    sol_cpp.write(sol_cpp_content)
    sol_cpp.close()

    # elif language == 'java':
    sol_java = open('./{}/sol1.java'.format(folder_name), 'w')
    sol_java.write(sol_java_content)
    sol_java.close()

def bojmaker(problem_number):
    url = 'https://www.acmicpc.net/problem/'
    html = urlopen('{}{}'.format(url, problem_number))
    bs_object = BeautifulSoup(html, 'html.parser')

    problem_title = bs_object.find('span', id='problem_title').text
    problem_input = bs_object.find('pre', id='sample-input-1').text
    folder_name = str(problem_number) + '_' + problem_title

    try:
        os.mkdir('{}'.format(folder_name))
    except OSError:
        pass


    
    file_maker(folder_name, problem_input)

    print('\n-------------------\n{}\n\nSet up completed\n-------------------\n{}{}\n'.format(folder_name, url, problem_number))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('problem_number', help="Write BOJ problem number")
    # parser.add_argument('--language', help="Input using language")

    args = parser.parse_args()

    problem_number = args.problem_number

    bojmaker(problem_number)

    # if args.py:
    #     bojmaker(problem_number, 'py')
    # elif args.cpp:
    #     bojmaker(problem_number, 'cpp')
    # elif args.java:
    #     bojmaker(problem_number, 'java')


if __name__ == "__main__":
    main()
