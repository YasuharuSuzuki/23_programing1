import glob
import sys, os
import io
import neologdn
import subprocess

def try_all(exec_python_path):
    in_path_all = sorted(glob.glob("data/in*.txt"))
    error_count = 0
    for in_path1 in in_path_all:
        out_path1 = in_path1.replace("in","out")
        
        with open(in_path1,"r") as f_in:
            # 標準入力を file に、標準出力を io.StringIO に結びつけてsubprocessで実行する
            proc = subprocess.Popen(['python', exec_python_path], encoding='utf-8', stdin=f_in, stdout=subprocess.PIPE)
            stdout, stderr = proc.communicate()
            stdout_io = io.StringIO(stdout)
        
        with open(out_path1,"r") as f_out:
            all_output = f_out.readlines()

        all_temp = stdout_io.getvalue().split('\n')
        for out_str1 in all_output:
            stdout_str1 = neologdn.normalize(all_temp.pop(0)) # neologdnで正規化してから比較する
            out_str1 = neologdn.normalize(out_str1) # neologdnで正規化してから比較する
            if out_str1 != stdout_str1:
                print(f"Error! temp={stdout_str1}, answer={out_str1}, in_path={in_path1}")
                error_count += 1
            else:
                print(f"OK temp={stdout_str1}, answer={out_str1}")
                pass

    print("AC" if error_count == 0 else "WA")


if __name__ == "__main__":
    try_all(sys.argv[1])
