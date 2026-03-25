# MedHallTune

**MedHallTune: A Benchmark and Instruction Tuning Dataset for Mitigating Medical Hallucination in Vision-Language Models** 

[![HuggingFace](https://img.shields.io/badge/HuggingFace-Dataset-yellow?logo=huggingface)](https://huggingface.co/datasets/russellyq/MedHallTune)
[![arXiv](https://img.shields.io/badge/arXiv-Paper-red?logo=arxiv)](https://arxiv.org/abs/2502.20780)


[Qiao Yan](https://github.com/russellyq), [Yuchen Yuan](https://scholar.google.com/citations?user=UzPuPRIAAAAJ&hl=en),[Xiaowei Hu](https://xw-hu.github.io/), [Yihan Wang](https://github.com/yiyihan), [Jiaqi Xu](https://jiaqixuac.github.io/), [Jinpeng Li](https://scholar.google.com/citations?user=gnkdhZ0AAAAJ&hl=en), [Chi Wing Fu](https://www.cse.cuhk.edu.hk/~cwfu/), [Pheng Ann Heng](https://www.cse.cuhk.edu.hk/~pheng/)


## Release
- Automatic evaluation platform is available at [MedHallTune-Eval](https://huggingface.co/spaces/russellyq/MedHallTune-Eval).
- Leaderboard is available at [**OpenCompass**](https://hub.opencompass.org.cn/dataset-detail/MedHallTune).
- Dataset is available at [**HuggingFace**](https://huggingface.co/datasets/russellyq/MedHallTune).
- Paper is available on [**arXiv**](https://arxiv.org/abs/2502.20780).

## Usage

1. Download the image data from [MedHallTune](https://huggingface.co/datasets/russellyq/MedHallTune).

2. The validation split annotations are provided under `/results_save_dir/` in this Github Page.

3. Run **inference with your own model** to generate a prediction file in **JSONL format**.

4. Go to the automatic evaluation platform: [MedHallTune-Eval](https://huggingface.co/spaces/russellyq/MedHallTune-Eval)

5. On the evaluation page:
   - Select the task type (**positive** or **negative**).
   - Upload your prediction file in **JSONL** format.
   - Provide your own API key (and base URL if needed).
   - Run the automatic evaluation and obtain the final evaluation summary.

6. After obtaining the evaluation results, please send the results to us by email for leaderboard submission.

<!-- ---

### Why do results need to be submitted by email?

Leaderboard results are **not updated automatically**.  
Please send your evaluation results to us by email so that we can **manually review** each submission before updating the public leaderboard on [OpenCompass](https://hub.opencompass.org.cn/dataset-detail/MedHallTune).

This manual review step is necessary to:

- avoid incorrect evaluations caused by invalid prediction formats or mismatched settings,
- avoid duplicate submissions of the same method,
- ensure the fairness and reliability of the public leaderboard.

--- -->

### Submission Email

If you would like your method to be included in the public leaderboard, please send us:

- your model name,
- a short description of the method,
- the evaluation summary from [MedHallTune-Eval](https://huggingface.co/spaces/russellyq/MedHallTune-Eval),
- and optionally the prediction file for verification.

Please send your submission to: [Qiao Yan](mailto:qiao.yan@link.cuhk.edu.hk)

---

### Detailed Evaluation Procedure

The evaluation platform [MedHallTune-Eval](https://huggingface.co/spaces/russellyq/MedHallTune-Eval) supports automatic scoring for user-submitted predictions.

To evaluate your method:

1. Prepare a prediction file in **JSONL** format.
2. Make sure each line corresponds to one sample in the validation set.
3. Open the evaluation page and choose the correct task split:
   - **positive**
   - **negative**
4. Upload your JSONL file.
5. Enter your API key required by the evaluator.
6. Click **Run Evaluation**.
7. Wait until the evaluation finishes and the summary is displayed on the page.
8. Save the evaluation summary and email it to us if you would like to request leaderboard inclusion.

---

### Example Prediction Format

Each line in the JSONL file should follow the format below:

```json
{
  "question_id": "xxx",
  "image": "xxx",
  "question": "xxx",
  "answer": "Your model answer"
}
```

### Notes
- Please ensure the `question_id` matches the official validation split.
- The uploaded JSONL file should contain one prediction per line.
- If you encounter any problems during the evaluation process, please feel free to contact us: <qiao.yan@link.cuhk.edu.hk>.
- We are happy to help with the evaluation.

## MedHallTune Benchmark Results

Evaluation of close-source proprietary models, open-source general models, and open-source medical models on the MedHallTune benchmark.

- **P**: Non-hallucination samples  
- **N**: Hallucination samples  
- **B.Score**: Balanced score  
- **M.Score**: Mitigation score  

---

### Close-source Proprietary Models

| Method | Clinical Acc (P/N) | Clinical Rel (P/N) | Detail Level (P/N) | Risk Level (P/N) | B.Score (P/N) | M.Score (P/N) |
|------|------|------|------|------|------|------|
| GPT-4o | 6.52 / 5.01 | 7.08 / 5.66 | 6.44 / 5.43 | 7.68 / 6.23 | 0.88 / 0.87 | 0.34 / 0.26 |
| GPT-5 | 6.48 / 5.75 | 7.02 / 6.49 | 6.44 / 6.31 | 7.98 / 7.15 | 0.86 / 0.84 | 0.21 / 0.19 |
| o3 | 6.32 / 5.77 | 6.81 / 6.44 | 6.00 / 5.99 | 7.71 / 7.10 | 0.89 / 0.86 | 0.25 / 0.21 |
| Grok-4 | 6.67 / 5.36 | 7.21 / 5.91 | 6.54 / 5.81 | 7.92 / 6.72 | 0.90 / 0.85 | 0.27 / 0.23 |
| Gemini-2.5 | 6.51 / 5.28 | 6.98 / 5.81 | 6.15 / 5.50 | 8.00 / 6.60 | 0.88 / 0.87 | 0.33 / 0.26 |

---

### Open-source General VLMs

| Method | Clinical Acc (P/N) | Clinical Rel (P/N) | Detail Level (P/N) | Risk Level (P/N) | B.Score (P/N) | M.Score (P/N) |
|------|------|------|------|------|------|------|
| MiniGPT-4 | 4.46 / 3.24 | 4.71 / 3.48 | 4.71 / 4.22 | 5.91 / 4.48 | 0.85 / 0.86 | 0.23 / 0.23 |
| Janus-Pro-7B | 6.17 / 4.12 | 6.73 / 4.51 | 5.53 / 4.61 | 7.43 / 5.21 | 0.91 / 0.89 | 0.39 / 0.22 |
| mPLUG-Owl2-7B | 5.97 / 3.94 | 6.43 / 4.29 | 5.72 / 4.71 | 7.16 / 5.05 | 0.90 / 0.88 | 0.36 / 0.27 |
| LLaVA-Critic-R1-7B | 6.14 / 4.27 | 6.56 / 4.81 | 6.11 / 5.01 | 7.64 / 5.61 | 0.86 / 0.86 | 0.25 / 0.28 |
| LLaVA-OneVision-8B | 6.50 / 4.72 | 7.04 / 5.13 | 5.46 / 4.78 | 7.05 / 5.80 | 0.91 / 0.88 | 0.38 / 0.19 |
| OpenMMReasoner-7B | 6.29 / 4.99 | 6.75 / 5.22 | 5.62 / 5.01 | 7.61 / 5.24 | 0.86 / 0.86 | 0.28 / 0.25 |
| Qwen-VL-Chat | 5.95 / 4.21 | 6.45 / 4.57 | 5.54 / 4.60 | 7.17 / 5.42 | 0.90 / 0.88 | 0.35 / 0.19 |
| Qwen2.5-VL-7B | 6.12 / 4.28 | 6.53 / 4.82 | 6.11 / 4.65 | 7.54 / 5.64 | 0.85 / 0.86 | 0.25 / 0.23 |
| Qwen3-VL-8B | 6.28 / 4.86 | 6.68 / 5.11 | 6.79 / 4.86 | 7.80 / 5.60 | 0.83 / 0.83 | 0.21 / 0.25 |
| InternVL-v1.5-4B | 6.02 / 4.25 | 6.59 / 4.68 | 5.29 / 4.56 | 7.28 / 5.31 | 0.90 / 0.87 | 0.30 / 0.23 |
| InternVL2.5-8B | 6.03 / 4.82 | 6.43 / 5.27 | 5.28 / 4.90 | 7.59 / 5.14 | 0.90 / 0.87 | 0.33 / 0.20 |
| InternVL3-8B | 6.23 / 4.64 | 6.74 / 5.05 | 5.16 / 4.67 | 7.63 / 5.39 | 0.88 / 0.87 | 0.24 / 0.14 |

---

### Open-source Medical VLMs

| Method | Clinical Acc (P/N) | Clinical Rel (P/N) | Detail Level (P/N) | Risk Level (P/N) | B.Score (P/N) | M.Score (P/N) |
|------|------|------|------|------|------|------|
| Med-Flamingo | 4.69 / 3.01 | 4.79 / 3.13 | 3.91 / 3.24 | 6.00 / 4.08 | 0.84 / 0.84 | 0.20 / 0.16 |
| RadFM | 3.81 / 4.42 | 4.17 / 4.92 | 3.70 / 4.03 | 5.12 / 5.65 | 0.86 / 0.81 | 0.10 / 0.04 |
| MedDr | 3.85 / 3.65 | 3.88 / 3.90 | 3.01 / 3.37 | 6.21 / 5.34 | 0.81 / 0.80 | 0.01 / 0.00 |
| Chiron-o1-8B | 6.32 / 5.09 | 6.80 / 5.59 | 6.29 / 5.59 | 7.69 / 6.46 | 0.85 / 0.85 | 0.26 / 0.28 |
| BiomedGPT | 4.25 / 3.67 | 4.13 / 3.73 | 3.92 / 3.94 | 6.40 / 5.24 | 0.85 / 0.84 | 0.22 / 0.15 |
| MedGemma-4B | 4.25 / 3.67 | 4.13 / 3.73 | 3.92 / 3.94 | 6.40 / 5.24 | 0.85 / 0.84 | 0.22 / 0.15 |
| BiMediX2-8B | 6.04 / 4.27 | 6.44 / 4.45 | 5.60 / 4.71 | 6.60 / 5.02 | 0.81 / 0.81 | 0.10 / 0.13 |
| HealthGPT-M3 | 6.55 / 4.49 | 7.09 / 4.87 | 6.14 / 5.09 | 7.70 / 5.66 | 0.90 / 0.89 | 0.37 / 0.26 |
| HuatuoGPT-V-7B | 6.51 / 5.04 | 7.05 / 5.56 | 6.76 / 5.74 | 7.68 / 6.32 | 0.88 / 0.87 | 0.35 / 0.27 |
| InfiMed-RL-3B | 6.03 / 4.53 | 6.49 / 4.96 | 4.87 / 4.44 | 7.53 / 5.90 | 0.84 / 0.83 | 0.08 / 0.09 |
| Lingshu-7B | 6.62 / 5.06 | 7.10 / 5.51 | 6.17 / 5.22 | 7.72 / 6.27 | 0.90 / 0.88 | 0.37 / 0.26 |
| Hulu-Med-7B | 6.50 / 5.01 | 7.03 / 5.49 | 5.88 / 5.14 | 7.70 / 6.22 | 0.90 / 0.88 | 0.36 / 0.25 |
| STLLaVA-Med-7B | 6.11 / 4.75 | 6.54 / 5.12 | 5.48 / 4.88 | 7.50 / 5.91 | 0.90 / 0.88 | 0.37 / 0.24 |
| LLaVA-Med-v1.5-7B | 6.28 / 5.03 | 6.78 / 5.39 | 5.48 / 4.84 | 7.39 / 5.89 | 0.91 / 0.89 | 0.38 / 0.23 |

## Citation

If MedHallTune is useful or relevant to your research, please kindly recognize our contributions by citing our paper:


```bibtex
@misc{yan2025medhalltune,
      title={MedHallTune: An Instruction-Tuning Benchmark for Mitigating Medical Hallucination in Vision-Language Models}, 
      author={Qiao Yan and Yuchen Yuan and Xiaowei Hu and Yihan Wang and Jiaqi Xu and Jinpeng Li and Chi-Wing Fu and Pheng-Ann Heng},
      year={2025},
      eprint={2502.20780},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2502.20780}, 
}
```