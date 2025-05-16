import csv
import uuid
import subprocess
import torch

bhive_csv = "/home/ithemal/bhive/benchmark/throughput/hsw.csv"
tokenizer_path = "/home/ithemal/ithemal/data_collection/build/bin/tokenizer"
output_data_path = "/home/ithemal/haswell_bhive.ithemal.data"
max_samples = 10000
count = 0

results = []
with open(bhive_csv) as f:
    reader = csv.reader(f)
    for row in reader:
        if count >= max_samples:
            break

        hex_code, timing = row[0], row[1]
        if timing.strip() == '':
            continue
        try:
            timing = float(timing)
            proc = subprocess.Popen(
                [tokenizer_path, hex_code, "--token"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = proc.communicate()
            stdout = stdout.decode("utf-8").strip()
            if "<instr>" not in stdout:
                continue
            if proc.returncode != 0 or "<block>" not in stdout:
                continue
            code_xml = stdout
            results.append((str(uuid.uuid4()), timing, None, code_xml))
            count += 1
            print("Finished processing {} of {}".format(count, max_samples))
        except Exception as e:
            print("Skipping {}: {}".format(hex_code, e))

print("Saving {} examples to {}".format(len(results), output_data_path))
torch.save(results, output_data_path)
