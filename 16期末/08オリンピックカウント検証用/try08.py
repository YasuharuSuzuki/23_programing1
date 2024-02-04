import glob
import sys, os
import io
import neologdn
import subprocess
import lzma
import json
from collections import Counter

# XZで圧縮されたJSONファイル名
xz_filename = 'data/answer.json.xz'

def try_all(exec_python_path):

    # XZ圧縮されたファイルを開き、内容を読み込む
    with lzma.open(xz_filename, 'rb') as file_in:
        json_str = file_in.read().decode('utf-8')

    # JSON文字列を辞書に変換
    json_data = json.loads(json_str)

    answer_count = len(json_data.keys())
    error_count = 0
    for answer_key1 in json_data.keys():
        input_string = '\n'.join(json_data[answer_key1][0])
        all_output = json_data[answer_key1][1]
        
        # 標準入力を file に、標準出力を io.StringIO に結びつけてsubprocessで実行する
        proc = subprocess.Popen(['python', exec_python_path], encoding='utf-8', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate(input_string)
        stdout_io = io.StringIO(stdout)
        
        all_temp = stdout_io.getvalue().split('\n')
        for out_str1 in all_output:
            stdout_str1 = neologdn.normalize(all_temp.pop(0)) # neologdnで正規化してから比較する
            out_str1 = neologdn.normalize(out_str1) # neologdnで正規化してから比較する
            if out_str1 != stdout_str1:
                print(f"Error! temp={stdout_str1}, answer={out_str1}, answer_key={answer_key1} input_str={input_string}")
                error_count += 1
            else:
                print(f"OK temp={stdout_str1}, answer={out_str1}")

    print(f"AC ({answer_count}/{answer_count})" if error_count == 0 else f"WA ({answer_count-error_count}/{answer_count} 正解率={100*(answer_count-error_count)/answer_count:.1f}%)")


if __name__ == "__main__":
    try_all(sys.argv[1])
