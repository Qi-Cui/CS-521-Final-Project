# Steps
1. Build with `./docker/docker_build.sh`.
2. Connect with `./docker/docker_connect.sh`.
3. Run `chmod +x scripts/build_dataset.sh`.
4. Run `./scripts/build_dataset.sh` to 
5. Run `python ~/ithemal/learning/pytorch/ithemal/run_ithemal.py   --data ~/haswell_bhive.ithemal.data   --use-rnn train   --experiment-name sanity-check   --experiment-time $(date +%s)   --sgd --threads 2 --trainers 2 --weird-lr --decay-lr --epochs 5`
