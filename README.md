# MedHallTune

**MedHallTune: A Benchmark and Instruction Tuning Dataset for Mitigating Medical Hallucination in Vision-Language Models** [[Paper](https://arxiv.org/abs/2502.20780)][[Huaggingface](https://huggingface.co/datasets/russellyq/MedHallTune)]

[Qiao Yan](https://github.com/russellyq), [Yuchen Yuan](https://scholar.google.com/citations?user=UzPuPRIAAAAJ&hl=en),[Xiaowei Hu](https://xw-hu.github.io/), [Yihan Wang](https://github.com/yiyihan), [Jiaqi Xu](https://jiaqixuac.github.io/), Xiwen Wu, [Jinpeng Li](https://scholar.google.com/citations?user=gnkdhZ0AAAAJ&hl=en), [Chi Wing Fu](https://www.cse.cuhk.edu.hk/~cwfu/), [Pheng Ann Heng](https://www.cse.cuhk.edu.hk/~pheng/)



## Release
- Evaluation data is available at [MedHallTune](https://huggingface.co/datasets/russellyq/MedHallTune). 
- MedHallTune is available on [[arXiv](https://arxiv.org/abs/2502.20780)]. 

## Usage

1. Download the dataset from [MedHallTune](https://huggingface.co/datasets/russellyq/MedHallTune).

2. Run inference with your own model to generate a result file in JSONL format.

3. Run the evaluation.

   3.1 Set your OpenAI API key in `agent.py`.

   3.2 Run the evaluation script:

   ```bash
   python eval.py \
       --input_path "path_to_your_results.jsonl" \
       --output_path "path_to_save_evaluation_results"

```markdown
> **Note:** You may need to slightly modify `eval.py` to adapt it to your own result format.
```

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