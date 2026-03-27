#!/bin/bash
# run_sglang.sh: safe startup script for Qwen3 on 2x RTX A4500
set -e

cd /home/tchen19/LLM

export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:64
export TORCH_CUDA_ALLOC_CONF=garbage_collection_threshold:0.6,max_split_size_mb:64

# write logs to file
LOGFILE=sglang.log
rm -f "$LOGFILE"

/home/tchen19/LLM/.venv/bin/python -m sglang.launch_server \
  --model-path Qwen/Qwen3-14B \
  --reasoning-parser qwen3 \
  --host 0.0.0.0 \
  --port 8000 \
  --device cuda \
  --tensor-parallel-size 2 \
  --dtype half \
  --cpu-offload-gb 48 \
  --offload-mode cpu \
  --mem-fraction-static 0.65 \
  --checkpoint-engine-wait-weights-before-ready \
  --max-running-requests 1 \
  --max-queued-requests 2 \
  --log-level info 2>&1 | tee "$LOGFILE"